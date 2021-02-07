## In the command terminal type in:

#       python -m manim projects\Graphing.py Intro1
#       python -m manim projects\Graphing.py Intro2
#       python -m manim projects\Graphing.py RightRiemann
#       python -m manim projects\Graphing.py LeftRiemann
#       python -m manim projects\Graphing.py RiemannSum

## This website has some more information on Graphing with manim:

#       https://elteoremadebeethoven.github.io/manim_3feb_docs.github.io/html/tree/scenes/graph_scene.html#riemann-rectangles


from manimlib.imports import *
import numpy as np
class Intro1(Scene):
    def construct(self):
        T1 = TextMobject("In Integral Calculus, we are interested in finding the area between a given graph and the x-axis on a given interval, [a,b]")
        T1.shift(UP)
        T1.scale(0.75)
        self.play(Write(T1), run_time = 7)




class Intro2(GraphScene):
    CONFIG = {
        "y_max": 6,
        "y_min": -1,
        "x_max": 6,
        "x_min": -1,
        "x_axis_width": 9,
        "y_tick_frequency": 1,
        "x_tick_frequency": 1,
        "axes_color": GREY,
        "graph_origin": 2 * DOWN + 4 * LEFT,
        "x_label_direction": DOWN,
        "y_label_direction": LEFT
    }

    def construct(self):
        self.setup_axes(animate=False)

        myGraph = self.get_graph(lambda x: 0.5*(x-2)**3-x+np.sin(x)+5, color = RED, x_min = 0, x_max = 6)
        rectangles = self.get_area(myGraph, 0, 3)

        self.play(ShowCreation(myGraph), run_time = 3)
        self.play(ShowCreation(rectangles), run_time = 3)

        T2 = TextMobject("We can approximate the area by summing up the areas of the rectangles contained within the area that we want to find")
        T2.shift(UP)
        T2.scale(0.75)
        self.play(Write(T2), run_time = 7)





class RightRiemann(Scene):
    def construct(self):
        T1 = TexMobject(r"\Delta x = \frac{b-a}{n}")
        T2 = TextMobject(" is the width of each individual rectangle")
        ME1 = TexMobject(r"S_{Right}=\Sigma_{i=1}^{n}f(a+(i)\Delta x)\Delta x")
        T3 = TextMobject("Right Riemann sum across interval [a,b] with n rectangles:")

        box1 = SurroundingRectangle(ME1)
        box1.set_stroke(BLUE)

        ME1.shift(0.5*UP)
        box1.shift(0.5*UP)
        T1.shift(1.5*DOWN)
        T1.shift(4*LEFT)
        T2.next_to(T1)
        T3.shift(2*UP)

        self.play(Write(T3), run_time = 3)
        self.play(ShowCreation(box1), run_time = 3)
        self.play(ShowCreation(ME1), run_time = 6)
        self.play(Write(T1), run_time = 3)
        self.play(Write(T2), run_time=3)





class LeftRiemann(Scene):
    def construct(self):
        ME1 = TexMobject(r"S_{Left}=\Sigma_{i=1}^{n}f(a+(i-1)\Delta x)\Delta x")
        T3 = TextMobject("Left Riemann sum across interval [a,b] with n rectangles:")

        box1 = SurroundingRectangle(ME1)
        box1.set_stroke(RED)

        ME1.shift(0.5*UP)
        box1.shift(0.5*UP)
        T3.shift(2*UP)

        self.play(Write(T3), run_time = 3)
        self.play(ShowCreation(box1), run_time = 3)
        self.play(ShowCreation(ME1), run_time = 6)





class RiemannSum(GraphScene):

    CONFIG ={
        "y_max": 10,
        "y_min": -1,
        "x_max": 10,
        "x_min": -1,
        "x_axis_width": 9,
        "y_tick_frequency": 1,
        "x_tick_frequency": 1,
        "axes_color": GREY,
        "graph_origin": 2*DOWN +4*LEFT,
        "x_label_direction": DOWN,
        "y_label_direction": LEFT,
    }
    def construct(self):
        self.setup_axes(animate=False)

        myGraph = self.get_graph(lambda x: 0.5*(x-2)**3-x+np.sin(x)+5, color = RED, x_min = 0, x_max = 6)
        rectangles = self.get_area(myGraph, 0, 3)

        self.play(ShowCreation(myGraph), run_time = 3)

        kwargs = {
            "x_min": 1,
            "x_max": 5,
            "fill_opacity": 0.9,
            "stroke_width": 0.05
        }

        iterations = 6

        self.rect_list = self.get_riemann_rectangles_list(myGraph, iterations, start_color = PURPLE, end_color = ORANGE, **kwargs)

        flat_rects = self.get_riemann_rectangles(
            self.get_graph(lambda x: 0), dx = 0.5, start_color = invert_color(PURPLE), end_color = invert_color(PURPLE), **kwargs
        )

        rects = self.rect_list[0]

        self.transform_between_riemann_rects(
            flat_rects, rects,
            replace_mobject_with_target_in_scene = True,
            run_time = 1
            )

        for i in range(1,6):
            self.transform_between_riemann_rects(
                self.rect_list[i-1], self.rect_list[i],
                dx = 1, replace_mobject_with_target_in_scene = True,
                run_time = 1
            )







