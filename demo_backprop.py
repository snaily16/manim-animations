from manimlib.imports import *
from manimlib.mobject.svg.tex_mobject import Tex
import os
import pyclbr

class NN_BackPropagation(Scene):
    def construct(self):
        r=0.3
        fc = ORANGE
        oc = RED
        bd = RED_C
        wc = BLUE
        yc = RED_D
        offset = np.array([-4,-1,0])
        h1 = Circle(fill_color=fc, fill_opacity=2, arc_center=offset+np.array([0,3,0]), radius=r)
        h2 = Circle(fill_color=fc, fill_opacity=2, arc_center=offset+np.array([0,1,0]), radius=r)
        h3 = Circle(fill_color=fc, fill_opacity=2, arc_center=offset+np.array([0,-1,0]), radius=r)
        o1 = Circle(fill_color=oc, color=bd, fill_opacity=2, arc_center=offset+np.array([5,1,0]), radius=r)
        arrow1 = Arrow(LEFT, RIGHT)
        arrow2 = Arrow(LEFT, RIGHT)
        arrow3 = Arrow(LEFT, RIGHT)
        arrow1.next_to(h1, LEFT)
        arrow2.next_to(h2, LEFT)
        arrow3.next_to(h3, LEFT)

        t1 = Tex("x_1")
        t1.next_to(arrow1, UP)
        t2 = Tex("x_2")
        t2.next_to(arrow2, UP)
        t3 = Tex("x_3") 
        t3.next_to(arrow3, UP)
        arrow4 = Arrow(h1, o1)
        arrow5 = Arrow(h2, o1)
        arrow6 = Arrow(h3, o1)
        arrow7 = Arrow(LEFT, RIGHT,color=MAROON_C).next_to(o1, RIGHT)
        
        script = ' \hat y = x1*w1 + x2*w2 + x3*w3'
        t7 = VGroup(Tex("\hat y = x_1\cdot w_1",color=MAROON_C),
                Tex("+x_2\cdot w_2",color=MAROON_C),
                Tex("+x_3\cdot w_3",color=MAROON_C)
                ).arrange(DOWN,aligned_edge=RIGHT).next_to(arrow7,UP)
        

        error = Tex('E = ').next_to(arrow7, RIGHT)
        erreq = Tex('\\frac{1}{2}(\hat y-y)^2').next_to(error, RIGHT).scale(0.8)
        derr = Tex('\\frac{\delta E}{\delta \hat y} = (\hat y - y)').next_to(error, DOWN).scale(0.8).shift(RIGHT)
        dyw = Tex('\\frac{\delta \hat y}{\delta w_i} = x_i').next_to(derr, DOWN).scale(0.8)
        dEw = Tex('\\frac{\delta E}{\delta w_i} =  (\hat y - y) \cdot x_i')
        dEw.bg = SurroundingRectangle(dEw, color=YELLOW, fill_color=RED, fill_opacity=.22)
        dEw_group = VGroup(dEw, dEw.bg).to_corner(DOWN*0.3+RIGHT/8).scale(0.8)
        barrows = [
                Arrow(o1,h1).shift(UP*0.25).set_color(YELLOW_C),
                Arrow(o1,h2).shift(UP*0.25).set_color(YELLOW_C),
                Arrow(o1,h3).shift(DOWN*0.25).set_color(YELLOW_C),
                ]

        barrow_labels = [Tex("\delta w_%d"%(i+1),color=YELLOW_C).next_to(barrows[i],UP).shift(DOWN*0.25) for i in range(len(barrows)-1)]
        barrow_labels.append(Tex("\delta w_%d"%(len(barrows)),color=YELLOW_C).next_to(barrows[len(barrows)-1],DOWN).shift(UP*0.25))

        barrow_updates = [Tex("w_%d-\eta \cdot \\frac{\delta E}{\delta w_%d}"%(i+1,i+1),color=YELLOW_C).next_to(barrows[i],UP).shift(DOWN*0.25).scale(0.8) for i in range(len(barrows)-1)]
        barrow_updates.append(Tex("w_%d-\eta \cdot \\frac{\delta E}{\delta w_%d}"%(len(barrows),len(barrows)),color=YELLOW_C).next_to(barrows[len(barrows)-1],DOWN).shift(UP*0.9).scale(0.8))
        barrow_updates[1].shift(LEFT*1.3)
        #for k in COLOR_MAP:
        #    print(k)
        #    s=Square(color=globals()[k],stroke_width=23)
        #    s.set_fill(globals()[k])
        #    self.play(FadeIn(s))

        self.add(h1,h2,h3)
        self.add(arrow1,t1)
        self.add(arrow2,t2)
        self.add(arrow3,t3)
        self.add(o1)
        self.add(arrow4, arrow5, arrow6) 
        self.add(arrow7, t7)
        self.play(Write(error), Write(erreq))
        self.play(Write(derr))
        self.play(Write(dyw))
        self.play(Write(dEw_group))
        for b,bl in zip(barrows,barrow_labels):
            self.play(GrowArrow(b))
            self.play(Write(bl))
        for bl, bl2 in zip(barrow_labels, barrow_updates):
            self.play(Transform(bl,bl2))
        self.wait(1)
