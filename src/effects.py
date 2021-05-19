from frame import Frame
from audioop import add #allows us to add byte object audio signals together
import numpy as np

class Effects:
    def chorus(self, info): 
      #300 ms delay
      #http://andrewslotnick.com/posts/audio-delay-with-python.html for buffersize help
      buff_size = info.sampwidth * 300 * int(info.framerate/1000)
      buffer = b'\0' * buff_size # must use b for byte literal class for info.samples
      mod_signal = info.samples[:-buff_size] 

      info.samples = add(info.samples ,buffer + mod_signal,  info.sampwidth)
#      info.samples = np.sin(bytearray(info.samples))

      #add LFO

      #modify amplitude of mod_signal?
      return info

    def flang(self, info):
        return info

    def delay(self, info):
        return info

    def floop(self, info):
        return info

    def clipping(self, info):
        return info
