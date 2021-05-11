from i_o import IO
from effects import Effects
import threading

audio = IO()
eff = Effects()

data = audio.read_audio()


def play():
    audio.play_audio(data)


# https://stackoverflow.com/questions/41371815/how-can-i-stop-my-tkinter-gui-from-freezing-when-i-click-my-button
def play_background():
    play_thread = threading.Thread(target=play)
    play_thread.daemon = True
    play_thread.start()


if __name__ == "__main__":
    play()
