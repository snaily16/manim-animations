from manimlib.imports import *
import os
import pyclbr

class GAN(Scene):
    CONFIG = {
            "camera_config":{"background_color":WHITE}
            }
    def construct(self):
        grid = NumberPlane((-1,1),(-1,1))
        matrix = [[0.5, 0.5],[0.5, 0.5]]
        self.play(ShowCreation(grid))
        self.wait()
        s = Square(set_length=0.2)
        self.add(s)
        s1 = Square(set_length=0.1)
        s.surround(s1)
        self.add(s1)
