from i_o import IO
from effects import Effects
from frame import Frame
import threading
import pyaudio

audio = IO()
eff = Effects()
info = Frame()

def chorus_effect(frame_data):
    eff.chorus(frame_data)


def play(t_info):
    audio.play_audio(t_info)


if __name__ == "__main__":
    info.filename = 'gc.wav'
    info = audio.read_audio(info)
    info = eff.chorus(info)
    #play(info)
    audio.write_audio(info)
