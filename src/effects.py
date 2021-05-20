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

    def delay(self, info):
        return info

    def floop(self, info):
        return info

    def clipping(self, info):
        return info

    def mix_audio(self, source_one, amp_one, source_two, amp_two):
        return source_one * amp_one + source_two * amp_two

