import wave as wv
import numpy as np
import pyaudio


class IO:
    sample_size = pyaudio.paInt16
    channels = 0
    wid = 0
    rate = 0
    dur = 0
    wav_file = wv.open('gc.wav')

    def read_audio(self):
        self.channels = self.wav_file.getnchannels()
        self.wid = self.wav_file.getsampwidth()
        self.rate = self.wav_file.getframerate()
        self.dur = self.wav_file.getnframes()
        data = np.frombuffer(self.wav_file.readframes(self.dur), dtype=np.int16)
        return data

    def write_audio(self, data):
        wf = wv.open(str("r" + 'gc.wav'), 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(2)  # 1 byte = 8bits so 2 byte = 16 bits
        wf.setframerate(self.rate)
        wf.writeframes(data)
        wf.close()
        return 0

    def play_audio(self, data):
        data = data.tobytes()
        p = pyaudio.PyAudio()
        stream = p.open(format=self.sample_size, channels=self.channels, rate=self.rate, output=True)
        stream.write(data)
        stream.stop_stream()
        stream.close()
        p.terminate()
        return 0
