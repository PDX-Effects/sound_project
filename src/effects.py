from audioop import add #allows us to add byte object audio signals together
import numpy as np
import math
import itertools

class Effects:
    def chorus(self, info):
        # Convert from float32 array to int16 buffer
        info.samples = info.samples * 32768
        info.samples = info.samples.astype(np.int16)
        info.samples = info.samples.tobytes()

        # 300 ms delay
        #http://andrewslotnick.com/posts/audio-delay-with-python.html for buffersize help
        buff_size = info.sampwidth * 300 * int(info.framerate/1000)
        buffer = b'\0' * buff_size # must use b for byte literal class for info.samples
        mod_signal = info.samples[:-buff_size]

        info.samples = add(info.samples ,buffer + mod_signal,  info.sampwidth)
        # info.samples = np.sin(bytearray(info.samples))
        lfo_values = self.LFO(info)
        samples = [next(lfo_values) for i in range(info.framerate)]   #gets every sample for a 20Hz sin wav sampled at 4800Hz(list of floats)
        #samples_obj = bytearray(samples)

        # Convert from int16 buffer to float32 array
        info.samples = np.frombuffer(info.samples, dtype=np.int16)
        info.samples = info.samples.astype(np.float32)
        info.samples = info.samples / 32768
        return info

    def LFO(self,info):  #returns a generator of a sin value at given step
         freq = 20  #20hz hardcoded for LFO needs
         step_size = (2* math.pi * freq )/info.framerate
         for i in itertools.count(0, step_size):
           yield math.sin(i)

    def flang(self, info):
        return info

    def phaser(self, info):
        return info

    def delay(self, info):
        return info

    def floop(self, info):
        return info

    def clipping(self, info):
        return info

    def mix_audio(self, source_one, amp_one, source_two, amp_two):
        return source_one * amp_one + source_two * amp_two

