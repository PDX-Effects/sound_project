import wave as wv
import numpy as np
import pyaudio
import os
from key_dict import key
from key_dict import just_ratios


class IO:
    max_amp = int(2**15)
    mix_rate = 0.50
    base_freq = 440

    def read_audio(self, info, path):
        try:
            wav_file = wv.open(path + os.path.sep + info.filename + ".wav")
            info.nchannels = wav_file.getnchannels()
            if info.nchannels == 1:
                info.samplesize = pyaudio.paFloat32
                info.nchannels = wav_file.getnchannels()
                info.sampwidth = wav_file.getsampwidth()
                info.framerate = wav_file.getframerate()
                info.frames = wav_file.getnframes()
                info.samples = np.frombuffer(wav_file.readframes(info.frames), dtype=np.int16)
                info.samples = info.samples.astype(np.float32)
                info.samples = info.samples / self.max_amp
            else:
                print("Error: Audio Channels Cannot Be: " + str(info.nchannels))
                info.nchannels = 0
                info.samples = None
        except FileNotFoundError:
            info.filename = ''
            info.samples = None
        return info

    def write_audio(self, info, path):
        # conversion to int16 and normalizing amplitude at 50% volume for pyaudio to process
        save = info.samples * self.max_amp
        save = save.astype(np.int16)
        save = save.tobytes()

        # writing to file
        wf = wv.open(path + os.path.sep + info.filename + ".wav", 'wb')
        wf.setnchannels(info.nchannels)
        wf.setsampwidth(2)  # 1 byte = 8bits so 2 byte = 16 bits
        wf.setframerate(info.framerate)
        wf.writeframes(save)
        wf.close()
        return 0

    def midi_freq(self, midi):
        return self.base_freq * 2 ** (((int(midi) - 69)) / 12)

    def song_gen(self, info, notes, time = 10, rate=48000):
        info.samplesize = pyaudio.paFloat32
        info.nchannels = 1
        info.sampwidth = 2
        info.framerate = rate

        notes = notes.split(' ')
        note_length = time / len(notes)
        song = info

        song.samples = self.chord_gen(song, self.midi_freq(key[notes[0]]), note_length)
        for note in notes[1:]: 
            frequency = self.midi_freq(key[note])
            chord = self.chord_gen(song, frequency, note_length)
            song = self.audio_append(song, chord)

        info.samples = song.samples
        return info

    def audio_append(self, info, new_add, times=1, rate=0.25):
        for t in range(times):
            buff_size = int(info.framerate * rate)
            # Get End of samples relative to buff_size
            first = info.samples[-buff_size:]
            print(first)
            # Cut first out of samples
            info.samples = info.samples[:-buff_size]
            print(info.samples)
            # Get beginning of new_add
            last = new_add[:buff_size]
            # Cut last out of new_add
            new_add = new_add[buff_size:]
            # Mix first and last.
            buff_zone = (first * self.mix_rate) + (last * self.mix_rate)
            # Append back together
            info.samples = np.append(info.samples, buff_zone)
            info.samples = np.append(info.samples, new_add)
        return info

    def chord_gen(self, info, base_freq=440, time=1.0, step_three=4, step_five=7, rate=48000):
        first = (np.sin(2 * np.pi * np.arange(rate * time) * base_freq / rate))
        third = (np.sin(2 * np.pi * np.arange(rate * time) * (base_freq * just_ratios[step_three]) / rate))
        fifth = (np.sin(2 * np.pi * np.arange(rate * time) * (base_freq * just_ratios[step_five]) / rate))

        #info.samples = (first * 0.33) + (third * 0.33) + (fifth * 0.33)
        #info.samples = info.samples.astype(np.float32)
        #return info.samples
        return ((first * 0.33) + (third * 0.33) + (fifth * 0.33)).astype(np.float32)

    def play_audio(self, info):
        play = info.samples.tobytes()
        p = pyaudio.PyAudio()
        stream = p.open(format=info.samplesize, channels=info.nchannels, rate=info.framerate, output=True)
        stream.write(play)
        stream.stop_stream()
        stream.close()
        p.terminate()
        return 0
