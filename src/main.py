from tkinter import *
from tkinter.ttk import Progressbar
from i_o import IO
from effects import Effects
import threading
import wave as wv
import numpy as np
import time

root = Tk()
audio = IO()
eff = Effects()

wav_file = wv.open('gc.wav')

# Discovering Screen Resolution

width = root.winfo_screenwidth() / 3
height = root.winfo_screenheight() / 2

# Setup Window
root.title("80s Synth Environment")
root.configure(background='white')
root.geometry(str(int(width)) + 'x' + str(int(height)))

# Display .Wav Info
sz = 8
channels = wav_file.getnchannels()
wid = wav_file.getsampwidth()
rate = wav_file.getframerate()
dur = wav_file.getnframes()
data = np.frombuffer(wav_file.readframes(dur), dtype=np.int16)


def play():
    audio.play_audio(data)


def prog():
    print(int(100 / int(dur / rate)))
    print(int(dur / rate))
    incr = 100 / (dur / rate)
    for i in range(int(dur / rate)):
        root.update_idletasks()
        progress['value'] += incr
        time.sleep(1)
        print(progress['value'])
    progress['value'] = 0

# https://stackoverflow.com/questions/41371815/how-can-i-stop-my-tkinter-gui-from-freezing-when-i-click-my-button
def play_background():
    play_thread = threading.Thread(target=play)
    play_thread.daemon = True
    play_thread.start()
    prog_thread = threading.Thread(target=prog)
    prog_thread.daemon = True
    prog_thread.start()

print(dur/rate)
play_button = Button(root, text="Play", command=play_background).grid(row=0, column=0)
progress = Progressbar(root, orient=HORIZONTAL, length=100, mode="determinate")
progress.grid(row=2, column=0)
chorus_button = Button(root, text="Chorus", command=NONE).grid(row=10, column=0)
flang_button = Button(root, text="Flang", command=NONE).grid(row=11, column=0)
delay_button = Button(root, text="Delay", command=NONE).grid(row=12, column=0)
floop_button = Button(root, text="Floop", command=NONE).grid(row=13, column=0)
clipping_button = Button(root, text="Clipping", command=NONE).grid(row=14, column=0)

root.mainloop()
