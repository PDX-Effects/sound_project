from frame import Frame
import audioop
import numpy as np

class Effects:
    def chorus(self, info): 
      #delay, change freq with filter.
      buff_size = int(np.size(info.samples)/3) 
      buffer = b'0' * buff_size # must use b for byte literal class for info.samples
      mod_signal = info.samples[:-buff_size]
      audioop.add(info.samples ,mod_signal,  info.sampwidth)
      return info

    def flang(self, info):
        return info

    def delay(self, info):
        return info

    def floop(self, info):
        return info

    def clipping(self, info):
        return info
