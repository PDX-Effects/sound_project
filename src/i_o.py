import wave as wv
import numpy as np
import pyaudio


class IO:

    def read_audio(self, info):
        wav_file = wv.open(info.filename)
        info.samplesize = pyaudio.paFloat32
        info.nchannels = wav_file.getnchannels()
        info.sampwidth = wav_file.getsampwidth()
        info.framerate = wav_file.getframerate()
        info.frames = wav_file.getnframes()
        #info.samples = np.frombuffer(wav_file.readframes(info.frames), dtype=np.int16)
        info.samples = wav_file.readframes(info.frames)
        return info

    def write_audio(self, info):
        # conversion to int16 and normalizing amplitude at 50% volume for pyaudio to process
        info.samples = (info.samples * int((2 ** 15) / 2))
        info.samples = info.samples.astype(np.int16).tobytes()

        # writing to file
        wf = wv.open(str("r" + info.filename), 'wb')
        wf.setnchannels(info.nchannels)
        wf.setsampwidth(2)  # 1 byte = 8bits so 2 byte = 16 bits
        wf.setframerate(info.framerate)
        wf.writeframes(info.samples)
        wf.close()
        return 0

    def play_audio(self, info):
#        info.samples = info.samples.tobytes()
        p = pyaudio.PyAudio()
        stream = p.open(format=info.samplesize, channels=info.nchannels, rate=info.framerate, output=True)
        stream.write(info.samples)
        stream.stop_stream()
        stream.close()
        p.terminate()
        return 0
