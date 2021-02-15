from manimlib.imports import *
import os
import pyclbr

class MultiLayer(Scene):
    def construct(self):
        r=0.5
        h1c = ORANGE
        h2c = TEAL_C
        oc = RED
        bd = RED_C
        wc = BLUE
        yc = RED_D
        offset = np.array([-3,0,0])
        hidden1 = [
                Circle(arc_center=offset+np.array([0,2,0]), radius=r, fill_color=h1c, color=h1c, fill_opacity=2),
                Circle(arc_center=offset+np.array([0,-1,0]),radius=r, fill_color=h1c, color=h1c, fill_opacity=2)
                ]

        hidden2 = [
                Circle(arc_center=offset+np.array([3,2,0]), radius=r, fill_color=h2c, color=h2c, fill_opacity=2),
                Circle(arc_center=offset+np.array([3,-1,0]),radius=r, fill_color=h2c, color=h2c, fill_opacity=2)
                ]        
        o1 = Circle(fill_color=oc, color=bd, fill_opacity=2, arc_center=offset+np.array([6,0.5,0]), radius=r)
        
        for i in range(len(hidden1)):
            arw = Arrow(LEFT,RIGHT).next_to(hidden1[i],LEFT)
            #inpArrows.append(arw)
            txt=Tex('x_{}'.format(i+1)).next_to(arw, UP)

            self.play(FadeIn(hidden1[i]))
            self.play(GrowArrow(arw), Write(txt))

        dirt = [UP, DOWN]
        for i in range(len(hidden1)):
            self.play(FadeIn(hidden2[i]))
            for j in range(len(hidden2)):
                arw = Arrow(hidden1[i], hidden2[j])
                txt =Tex('w_{%d%d}'%(i+1,j+1)).next_to(arw, dirt[i])
                self.play(GrowArrow(arw), Write(txt))
        
        for i in range(len(hidden2[i])):
            arw = Arrow(hidden1[i], o1)
            txt = Tex('w_{%d}'%(i+1)).next_to(arw,UP) 
            self.play(FadeIn(o1))
            self.play(GrowArrow(arw), Write(txt))
