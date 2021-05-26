import wave as wv
import numpy as np
import pyaudio


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

    def note_gen(self, info, freq=440, time=5, rate=48000):
        info.samplesize = pyaudio.paFloat32
        info.nchannels = 1
        info.sampwidth = 2
        info.framerate = rate
        info.samples = (np.sin(2 * np.pi * np.arange(info.framerate * time) * freq / info.framerate)).astype(np.float32)
        info.samples = info.samples * 0.50
        return info

    def chord_gen(self, info, base_freq = 440, time = 5, rate = 4800):
        info.samplesize = pyaudio.paFloat32
        info.nchannels = 1
        info.sampwidth = 2
        info.framerate = rate

        first = []
        third = []
        fifth = []

        first = (np.sin(2 * np.pi * np.arange(info.framerate * time) * base_freq / info.framerate)).astype(np.float32)
        third = (np.sin(2 * np.pi * np.arange(info.framerate * time) * (base_freq * (5/4)) / info.framerate)).astype(np.float32)
        fifth = (np.sin(2 * np.pi * np.arange(info.framerate * time) * (base_freq * (3/2)) / info.framerate)).astype(np.float32)
        
        info.samples = (first * 0.50) + (third * 0.50) + (fifth * 0.50)

        #for i in range(len(info.samples)):
        #    info.samples[i] = (first * 0.50) + (third * 0.50) + (fifth * 0.50)

        return info

    def play_audio(self, info):
        play = info.samples.tobytes()
        p = pyaudio.PyAudio()
        stream = p.open(format=info.samplesize, channels=info.nchannels, rate=info.framerate, output=True)
        stream.write(play)
        stream.stop_stream()
        stream.close()
        p.terminate()
        return 0
