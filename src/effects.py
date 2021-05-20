from frame import Frame
from scipy import signal
import numpy as np


class Effects:
    def chorus(self, info):
        return info

    def flang(self, info):
        return info

    def phaser(self, info):
        return info

    def delay(self, info, echo=0.1, amp=0.5):
        delay_frame = round(echo * info.framerate)
        delay_frame_zero = np.zeros(delay_frame)
        delay_samp = np.concatenate((delay_frame_zero, info.samples))
        info.samples = np.concatenate((info.samples, delay_frame_zero))
        info.samples = info.samples + delay_samp * amp
        return info

    def floop(self, info):
        return info

    def clipping(self, info):
        return info
