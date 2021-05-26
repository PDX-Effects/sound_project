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
        info
        return 0

    def note_gen(self, info, freq=440, time=5, rate=48000):
        info.samplesize = pyaudio.paFloat32
        info.nchannels = 1
        info.sampwidth = 2
        info.framerate = rate
        info.samples = (np.sin(2 * np.pi * np.arange(info.framerate * time) * freq / info.framerate)).astype(np.float32)
        info.samples = info.samples * 0.50
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
