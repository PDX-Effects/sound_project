import pyaudio


class IO:
    sample_size = pyaudio.paInt16
    channels = 1
    rate = 48000

    def read_audio(self):
        return 0

    def write_audio(self):
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
