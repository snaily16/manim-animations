from manimlib.imports import *
from manimlib.mobject.svg.tex_mobject import Tex
import os
import pyclbr

class Graph_OR(GraphScene):
    maxx = 2
    CONFIG = {
            'x_min':-maxx,
            'x_max':maxx,
            'y_min':-maxx,
            'y_max':maxx,
            'graph_origin':ORIGIN
            }
    def construct(self):
        self.setup_axes(animate=True)
        # Example
        #wtdata = [[0.2,0.3],[0.4,0.5],[0.4,0.7],[0.6,0.7]]
        #data = [[0.1,0.2],[0.2,0.3],[0.6,0.6],[0.8,0.5]]
        #label = [0,0,1,1]
        #new_data = [0.5, 0.2]
        # And gate
        #wtdata = [[0.0,0.9],[0.0,0.7],[0.0,0.5],[0.2,0.7],[0.2,0.5]]
        #data = [[0,0],[0,1],[1,0],[1,1]]
        #label = [0,0,0,1]

        # Or gate
        wtdata = [[0.2,0.3],[0.4,0.5],[0.6,0.7]]
        data = [[0,0],[0,1],[1,0],[1,1]]
        label = [0,1,1,1]
        c = [RED_E, GREEN]
        for i,(x,y) in enumerate(zip(data,label)):
            d = Dot().move_to(self.coords_to_point(x[0], x[1])).set_color(c[y])
            t = Tex('({},{})'.format(x[0],x[1])).next_to(d, LEFT+DOWN*0.2)
            self.add(d)
            self.add(t.scale(0.6))
        
        self.w = wtdata[0]
        gt = self.get_graph(self.line_func)
        eq1 = Tex('{} x_1 + {} x_2 = 0.6'.format(self.w[0],self.w[1])).to_corner(LEFT+DOWN)
        self.play(Write(eq1))
        self.play(ShowCreation(gt))
        for wt in wtdata[1:]:
            self.w = wt
            g = self.get_graph(self.line_func)
            eq = Tex('{} x_1 + {} x_2 = 0.6'.format(wt[0],wt[1])).to_corner(LEFT+DOWN)
            self.wait(1)
            self.play(Transform(gt,g), Transform(eq1,eq))


        #d = Dot().move_to(self.coords_to_point(new_data[0], new_data[1])).set_color(YELLOW)
        #self.add(d)
        #true = Tex('True').next_to(gt,UP*0.1).set_color(GREEN)
        #false = Tex('False').next_to(gt,DOWN*0.8).set_color(RED)
        #self.add(true, false)
        self.wait(2)

    
    def line_func(self, t):
        th = 0.6
        if self.w[1]==0:
            return th
        return ((th-self.w[0]*t)/self.w[1])
