from manimlib.imports import *
import os
import pyclbr

class BasicNeuralNet(Scene):
    def construct(self):
        r=0.5
        fc = ORANGE
        oc = RED
        bd = RED_C
        wc = BLUE
        yc = RED_D
        offset = np.array([-2,-1,0])
        h1 = Circle(fill_color=fc, fill_opacity=2, arc_center=offset+np.array([0,3,0]), radius=r)
        h2 = Circle(fill_color=fc, fill_opacity=2, arc_center=offset+np.array([0,1,0]), radius=r)
        h3 = Circle(fill_color=fc, fill_opacity=2, arc_center=offset+np.array([0,-1,0]), radius=r)
        o1 = Circle(fill_color=oc, color=bd, fill_opacity=2, arc_center=offset+np.array([3,1,0]), radius=r)
        arrow1 = Arrow(LEFT, RIGHT,color=MAROON_C)
        arrow2 = Arrow(LEFT, RIGHT,color=MAROON_C)
        arrow3 = Arrow(LEFT, RIGHT,color=MAROON_C)
        arrow1.next_to(h1, LEFT)
        arrow2.next_to(h2, LEFT)
        arrow3.next_to(h3, LEFT)

        t1 = Text("x1")
        t1.next_to(arrow1, UP)
        t2 = Text("x2")
        t2.next_to(arrow2, UP)
        t3 = Text("x3") 
        t3.next_to(arrow3, UP)
        arrow4 = Arrow(h1, o1,color=MAROON_C)
        arrow5 = Arrow(h2, o1,color=MAROON_C)
        arrow6 = Arrow(h3, o1,color=MAROON_C)
        arrow7 = Arrow(LEFT, RIGHT,color=MAROON_C).next_to(o1, RIGHT)
        t4 = Text("w1", color = wc).next_to(arrow4, UP)
        t5 = Text("w2", color = wc).next_to(arrow5, UP)
        t6 = Text("w3", color = wc).next_to(arrow6, 0.25*DOWN)
        script = '''
        y = x1*w1 + 
            x2*w2 +
            x3*w3
        '''
        t7 = Text(script, color = yc).next_to(arrow7, RIGHT)
        self.play(FadeIn(h2), FadeIn(h3), FadeIn(h1))
        self.play(GrowArrow(arrow1), Write(t1))
        self.play(GrowArrow(arrow2), Write(t2))
        self.play(GrowArrow(arrow3), Write(t3))
        self.play(FadeIn(o1))
        self.play(GrowArrow(arrow4), GrowArrow(arrow5), GrowArrow(arrow6), 
                Write(t4), Write(t5), Write(t6))
        self.play(GrowArrow(arrow7), Write(t7))
