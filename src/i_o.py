import wave as wv
import numpy as np
import pyaudio
from key_dict import key
from key_dict import just_ratios


class IO:
    def read_audio(self, info):
        try:
            wav_file = wv.open(info.filename)
        except FileNotFoundError:
            info.samples = None
            return info
        info.samplesize = pyaudio.paFloat32
        info.nchannels = wav_file.getnchannels()
        info.sampwidth = wav_file.getsampwidth()
        info.framerate = wav_file.getframerate()
        info.frames = wav_file.getnframes()
        info.samples = np.frombuffer(wav_file.readframes(info.frames), dtype=np.int16)
        info.samples = info.samples.astype(np.float32)
        info.samples = info.samples / 32768
        return info

    def write_audio(self, info):
        # conversion to int16 and normalizing amplitude at 50% volume for pyaudio to process
        save = info.samples * 32768
        save = save.astype(np.int16)
        save = save.tobytes()

        # writing to file
        wf = wv.open(str("new_" + info.filename), 'wb')
        wf.setnchannels(info.nchannels)
        wf.setsampwidth(2)  # 1 byte = 8bits so 2 byte = 16 bits
        wf.setframerate(info.framerate)
        wf.writeframes(save)
        wf.close()
        return 0

    def midi_freq(self, midi):
        return 440 * 2 ** ((midi - 69) / 12)

    def song_gen(self, info, notes, time, rate=48000):

        return info

    def chord_gen(self, info, base_freq=440, time=1.0, step_three=4, step_five=7, rate=48000):
        first = (np.sin(2 * np.pi * np.arange(rate * time) * base_freq / rate)).astype(np.float32)
        third = (np.sin(2 * np.pi * np.arange(rate * time) * (base_freq * just_ratios[step_three]) / rate)).astype(np.float32)
        fifth = (np.sin(2 * np.pi * np.arange(rate * time) * (base_freq * just_ratios[step_five]) / rate)).astype(np.float32)

        info.samples = (first * 0.33) + (third * 0.33) + (fifth * 0.33)
        return info.samples

    def play_audio(self, info):
        play = info.samples.tobytes()
        p = pyaudio.PyAudio()
        stream = p.open(format=info.samplesize, channels=info.nchannels, rate=info.framerate, output=True)
        stream.write(play)
        stream.stop_stream()
        stream.close()
        p.terminate()
        return 0
