from i_o import IO
from effects import Effects
from frame import Frame
import threading

audio = IO()
eff = Effects()
info = Frame()


def play(t_info):
    audio.play_audio(t_info)


# https://stackoverflow.com/questions/41371815/how-can-i-stop-my-tkinter-gui-from-freezing-when-i-click-my-button
def play_background():
    play_thread = threading.Thread(target=play)
    play_thread.daemon = True
    play_thread.start()


if __name__ == "__main__":
    info.filename = 'gc.wav'
    info = audio.read_audio(info)
    info = eff.delay(info)
    #play(info)
    audio.write_audio(info)
