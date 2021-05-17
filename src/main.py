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


# https://stackoverflow.com/questions/41371815/how-can-i-stop-my-tkinter-gui-from-freezing-when-i-click-my-button
def play_background():
    play_thread = threading.Thread(target=play)
    play_thread.daemon = True
    play_thread.start()

#fills info object with frame data
if __name__ == "__main__":
    info.filename = 'gc.wav'
    info = audio.read_audio(info)
    chorus_effect(info)
    play(info)


