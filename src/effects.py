from audioop import add  # allows us to add byte object audio signals together
import numpy as np
import itertools
from scipy import signal


class Effects:
    def delay(self, info, delay=300):
        # Convert from float32 array to int16 buffer
        info.samples = info.samples * 32768
        info.samples = info.samples.astype(np.int16)
        info.samples = info.samples.tobytes()

        # 300 ms delay
        # #http://andrewslotnick.com/posts/audio-delay-with-python.html for buffersize help
        buff_size = info.sampwidth * delay * int(info.framerate/1000)
        buffer = b'\0' * buff_size # must use b for byte literal class for info.samples
        mod_signal = info.samples[:-buff_size]

        info.samples = add(info.samples, buffer + mod_signal,  info.sampwidth)
        # lfo_values = self.LFO(info)
        # samples = [next(lfo_values) for i in range(info.framerate)]
        # #gets every sample for a 20Hz sin wav sampled at 4800Hz(list of floats)

        # Convert from int16 buffer to float32 array
        info.samples = np.frombuffer(info.samples, dtype=np.int16)
        info.samples = info.samples.astype(np.float32)
        info.samples = info.samples / 32768
        return info

    def lfo(self, info, freq=20, amp=1, phase=0):  # returns a generator of a sin value at given step
        # 20hz hardcoded for LFO needs
        phase = (phase / 360) * 2 * np.pi
        step_size = (2 * np.pi * freq) / info.framerate
        return (np.sin(phase + i) * amp for i in itertools.count(start=0, step=step_size))

    # http://www.geofex.com/Article_Folders/phasers/phase.html
    # https://www.dsprelated.com/freebooks/pasp/Time_Varying_Delay_Effects.html
    # https://github.com/wybiral/python-musical/blob/master/musical/audio/effect.py
    def chorus(self, info, freq=1.0, dry=0.50, wet=0.50, delay=25.0, depth=1.0, phase=0.0):
        mil = float(info.framerate) / 1000  # find frames per ms
        delay *= mil  # Correct Delay to match framerate of sample
        depth *= mil  # Same for depth
        lfo = (np.sin(2 * np.pi * freq * np.arange(len(info.samples)) / info.framerate) +
            (phase * 2 * np.pi)) * depth + delay
        samp = info.samples.copy()
        for i in range(len(info.samples)):
            index = int(i - lfo[i])
            if 0 < index < len(info.samples):
                samp[i] = info.samples[i] * dry + info.samples[index] * wet  # Delay Feedback
        info.samples = info.samples.astype(np.float32)
        info.samples = samp
        return info

    # http://www.geofex.com/Article_Folders/phasers/phase.html
    # https://www.dsprelated.com/freebooks/pasp/Time_Varying_Delay_Effects.html
    # https://github.com/wybiral/python-musical/blob/master/musical/audio/effect.py
    def flang(self, info, freq=1.0, dry=0.50, wet=0.50, delay=1.0, depth=20.0, phase=0.0):
        mil = float(info.framerate) / 1000  # find frames per ms
        delay *= mil  # Correct Delay to match framerate of sample
        depth *= mil  # Same for depth
        lfo = ((np.sin(2 * np.pi * freq * (np.arange(len(info.samples)) / info.framerate)) +
               (phase * 2 * np.pi))) * depth + delay
        samp = info.samples
        for i in range(len(info.samples)):
            delay = int(i - lfo[i])
            if 0 < delay < len(info.samples):
                samp[i] = samp[i] * dry + samp[delay] * wet  # Delay Feedback
        info.samples = samp
        return info

    def phaser(self, info, dry=0.70, wet=0.30, passes = 1):
        y = info.samples
        b, a = signal.ellip(4, 0.01, 120, 0.125)
        for i in range(passes):
            y += (signal.filtfilt(b, a, y) * 0.5).astype(np.float32)

        info.samples = (info.samples * dry) + (y * wet)
        return info

    def clipping(self, info, percent):
        info.samples = info.samples * 32768
        info.samples = info.samples.astype(np.int16)
        new_amp = int(percent * 32768)
        for c in np.nditer(info.samples, op_flags=['readwrite']):
            if c >= new_amp:
                c[...] = new_amp
            elif c <= -new_amp:
                c[...] = -new_amp
        info.samples = info.samples.astype(np.float32)
        info.samples = info.samples / 32768
        return info

    # https://github.com/wybiral/python-musical/blob/master/musical/audio/effect.py
    def tremolo(self, info, freq=5, dry=0.50, wet=0.50):
        lfo = (np.sin(2 * np.pi * freq * np.arange(len(info.samples)) / info.framerate))
        samp = info.samples * dry + (info.samples * lfo) * wet
        info.samples = samp.astype(np.float32)
        return info

    def change_amp_rate(self, info, rate=1.0):
        info.samples = info.samples * rate
        info.samples = info.samples.astype(np.float32)
        return info
