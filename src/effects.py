from frame import Frame
from audioop import add
import numpy as np

#TODO: use bytes object itself not 1d array of byte sample
class Effects:
    def chorus(self, info): 
      #delay, change freq with filter.
      #3 second delay
      buff_size = info.sampwidth * 3 * int(info.framerate)
      buffer = b'\0' * buff_size # must use b for byte literal class for info.samples
      mod_signal = info.samples[:-buff_size] #compensate for buffer size
      info.samples = add(info.samples ,buffer + mod_signal,  info.sampwidth)
      return info

    def flang(self, info):
        return info

    def delay(self, info):
        return info

    def floop(self, info):
        return info

    def clipping(self, info):
        return info
