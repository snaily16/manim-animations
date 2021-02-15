from manimlib.imports import *
import os
import pyclbr
from manimlib.scene.moving_camera_scene import MovingCameraScene
class ChangingCameraWidthAndRestore(MovingCameraScene):
    def construct(self):
        text = Text("Hello World").set_color(BLUE)
        self.add(text)
        self.camera_frame.save_state()
        self.play(self.camera_frame.animate.set_width(text.get_width() * 1.2))
        self.wait(0.3)
        self.play(Restore(self.camera_frame))
