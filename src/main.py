from tkinter import *
import wave as wv

root = Tk()
wavefile = wv.open('gc.wav')

# Discovering Screen Resolution
width = root.winfo_screenwidth() / 3
height = root.winfo_screenheight() / 2

# Setup Window
root.title("80s Synth Environment")
root.configure(background='white')
root.geometry(str(int(width))+'x'+str(int(height)))

# Display .Wav Info
sz = 8; chan = wavefile.getnchannels(); wid = wavefile.getsampwidth(); rate = wavefile.getframerate(); dur = wavefile.getnframes()

Label(root, text= "File Name: " + "gc.wav", fg = "black", font = "none" + str(sz) + "bold").grid(row = 0, column = 0, sticky = W)
Label(root, text= "Channels: " + str(chan), fg = "black", font = "none" + str(sz) + "bold").grid(row = 1, column = 0, sticky = W)
Label(root, text= "Width: " + str(wid), fg = "black", font = "none" + str(sz) + "bold").grid(row = 2, column = 0, sticky = W)
Label(root, text= "Rate: " + str(rate) + "ps", fg = "black", font = "none" + str(sz) + "bold").grid(row = 3, column = 0, sticky = W)
Label(root, text= "Duration: " + str(dur/rate) + "ps", fg = "black", font = "none" + str(sz) + "bold").grid(row = 4, column = 0, sticky = W)
root.mainloop()

