from manimlib.imports import *
import os
import pyclbr

class NeuralNet_Eg(Scene):
    def construct(self):
        #self.set_pixel_height(14)
        r=0.2
        h1c = ORANGE
        h2c = TEAL_C
        oc = RED
        bd = RED_C
        wc = BLUE
        yc = RED_D
        GRshades = [GREEN_A, GREEN_B, GREEN_C, GREEN_D, GREEN_E]
        REDshades = [RED_A, RED_B, RED_C, RED_D, RED_E]
        IPshades = [ORANGE, YELLOW_D]
        WTshades = [TEAL_E, ORANGE, BLUE_E, YELLOW]
        offset = np.array([-3,0,0])
        w = [0.2, 0.3]
        dirt = [UP, DOWN]
        n=0.1
        th=0.6
        iterations = 2
        #x = [[1,1],[0,1],[1,0],[0,0]]
        #y = [1,1,1,0]
        #y = [1,0,0,0]
                
        x = [[0.1,0.2],[0.2,0.3],[0.6,0.6],[0.8,0.5]]
        y = [0,0,1,1]

        #scene_title = Tex('AND\\ GATE').to_corner(UP+ORIGIN)
        #scene_title = Tex('OR\\ GATE').to_corner(UP+ORIGIN)
        scene_title = Tex('An\\ Example').to_corner(UP+ORIGIN)
        self.play(Write(scene_title))
        hidden1 = [
                Circle(arc_center=offset+np.array([0,2,0]), radius=r, fill_color=h1c, color=h1c, fill_opacity=2),
                Circle(arc_center=offset+np.array([0,0,0]),radius=r, fill_color=h1c, color=h1c, fill_opacity=2)
                ]

        o1 = Circle(fill_color=oc, color=bd, fill_opacity=2, arc_center=offset+np.array([3,1,0]), radius=r)
        
        xtxt = []
        xarw = []
        wtxt = []
        harw = []
        for i in range(len(hidden1)):
            arw = Arrow(LEFT,RIGHT).next_to(hidden1[i],LEFT)
            txt=Tex('x_{}'.format(i+1)).next_to(arw, LEFT)
            xtxt.append(txt)
            xarw.append(arw)
            self.play(FadeIn(hidden1[i]))
            self.play(GrowArrow(arw), Write(xtxt[i]))

        self.play(FadeIn(o1))
        for i in range(len(hidden1)):
            arw2 = Arrow(hidden1[i], o1)
            txt2 = Tex('w_{}'.format(i+1)).next_to(arw2,dirt[i]) 
            wtxt.append(txt2)
            harw.append(arw2)
            self.play(GrowArrow(arw2), Write(txt2))

        arw3 = Arrow(LEFT, RIGHT).next_to(o1, RIGHT)
        txt3 = Tex('\hat y').next_to(arw3, RIGHT)
        self.play(GrowArrow(arw3), Write(txt3))
        eq1_text=["0",";","\sum","x_i","\cdot","w_i","<","\\theta"]
        eq2_text=["1",";","\sum","x_i","\cdot","w_i","\ge","\\theta"]
        eq1 = Tex(*eq1_text)
        eq2 = Tex(*eq2_text)
        for i, item in enumerate(eq2):
            item.align_to(eq1[i],LEFT)
        eq11=VGroup(*eq1)
        eq22=VGroup(*eq2)
        eq22.shift(DOWN)
        eq_grp = VGroup(eq11,eq22).to_corner(DOWN+RIGHT)
        braces=Brace(eq_grp,LEFT)
        eq_text=braces.get_text("$\hat y=$")
        self.play(GrowFromCenter(braces),Write(eq_text))
        self.play(Write(eq11),Write(eq22))
        error = Tex('Error =').next_to(txt3, DOWN).set_color(RED).shift(RIGHT*0.5+DOWN*0.6)
        erreq = Tex('\\frac{1}{2} \\times (\hat y-y)^2').next_to(error, RIGHT).set_color(RED)
        self.play(Write(error), Write(erreq))
        delta=[]
        for i in range(len(w)):
            j = len(w) - i
            di = Tex('\delta w_{} = \eta \\times \Delta E \cdot x_{}'.format(i+1,i+1)).to_corner(LEFT+DOWN*(j))
            delta.append(di)
            self.play(Write(di))
            temp_dw = []
            for i in range(len(w)):
                temp_dw.append(Tex('').next_to(di, RIGHT))
        dErr = Tex('\Delta E = (\hat y - y)').next_to(delta[0], UP).shift(LEFT*0.5)
        temp_derr = Tex('').next_to(dErr, RIGHT)
        self.play(Write(dErr))
        labels = Tex('\eta = {}, \\theta ={}'.format(n,th)).to_corner(UP+RIGHT)
        labels.bg=SurroundingRectangle(labels,color=BLUE,fill_opacity=.5)
        labels_group = VGroup(labels.bg, labels)
        self.play(FadeIn(labels_group))
        
        for itr in range(iterations):
            iteration = Tex('Iteration: {}'.format(itr+1)).to_corner(UP+LEFT).set_color(MAROON_C)
            self.play(iteration.scale, 0.8)
            for inp in range(len(x)):
                #erreq1 = Tex('\\frac{1}{2} \\times (y-\hat y)^2').next_to(error, RIGHT).set_color(RED)
                #self.play(Transform(erreq,erreq1))
                x_ = x[inp]
                yhat=0
                for i in range(len(xtxt)):
                    xnew = Tex('x_{}={}'.format(i+1, x_[i])).next_to(xarw[i],LEFT).set_color(IPshades[inp%2])
                    self.play( Transform(xtxt[i], xnew))
                for i in range(len(wtxt)):
                    wnew = Tex('w_{}={:.2f}'.format(i+1,w[i])).next_to(harw[i],dirt[i]).set_color(WTshades[inp%4])
                    self.play(Transform(wtxt[i], wnew))
                    yhat += x_[i]*w[i]
                summ = Tex('\sum w_i \cdot x_i = {:.2f}'.format(yhat)).next_to(arw3,UP)
                self.play(summ.scale, 0.6)
                yhat = 0 if yhat<th else 1
                ynew = Tex('\hat y = {}'.format(yhat)).next_to(arw3, RIGHT)
                self.play(Transform(txt3, ynew))
                err = (yhat-y[inp])
                #self.play(Write(error), Write(erreq))
                #nerror = Tex('\\frac{1}{2} \\times (%d-%d)^2'%(yhat,y[inp])).set_color(REDshades[inp%5]).scale(0.8).next_to(error, RIGHT)
                #self.play(Transform(erreq, nerror))
                #nerror = Tex('\\frac{1}{2} \\times (%d-%d)^2=%.1f'%(yhat,y[inp],(err**2)/2)).set_color(REDshades[inp%5]).scale(0.8).next_to(error, RIGHT)
                #self.play(Transform(erreq, nerror))
                dw = [0 for _ in range(len(w))]
                #dE = Tex('=(%d - %d)'%(yhat, y[inp])).next_to(dErr, RIGHT).set_color(REDshades[inp%5])
                #self.play(FadeOut(dE))
                dE = Tex('=(%d-%d) = %d'%(yhat, y[inp], err)).next_to(dErr, RIGHT).set_color(REDshades[inp%5])
                self.play(FadeOut(temp_derr))
                temp_derr = dE
                self.play(dE.scale, 1/1.2)
                for i in range(len(w)):
                    dw[i] = err*n*x_[i]
                    w[i] = w[i] - dw[i]
                    dw_ = float('{:.2f}'.format(dw[i]))
                    if dw_ == 0:
                        dw_ = abs(dw_)
                    dww = Tex(' = {:.2f}'.format(dw_)).next_to(delta[i], RIGHT).set_color(GRshades[inp%5]).scale(1.2)
                    self.play(FadeOut(temp_dw[i]))
                    self.play(dww.scale, 1/1.2)
                    temp_dw[i]=dww
                self.play(FadeOut(summ))
            self.play(FadeOut(iteration))
        self.wait(2)
        self.clear()
        final_ans = Tex('After\\ Iteration\\ {},\\ The\\ final\\ weights\\ are: '.format(iterations))
        self.play(Write(final_ans))
        dirt = [LEFT, RIGHT]
        for i in range(len(w)):
            weights = Tex('w_{} = {:.2f}'.format(i+1,w[i])).next_to(final_ans, DOWN).shift(dirt[i]*1.4)
            self.play(Write(weights))

        self.wait(2)
