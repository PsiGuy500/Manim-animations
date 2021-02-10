## In the command terminal type in:

#       python -m manim projects\DivAndCurl.py Div
#       python -m manim projects\DivAndCurl.py Curl

from manimlib.imports import *
import numpy as np


class Div(Scene):
    def construct(self):
        func = lambda p: np.array([
            p[0], #x or i hat
            p[1], #y or j hat
        ])

        field = VectorField(func)
        field.set_color(ORANGE)
        F1 = TexMobject(r"\nabla \cdot \vec{F} > 0")
        c4 = Circle(color=BLUE_E, radius = 1)
        F1.shift(2*UP)

        self.play(*[GrowArrow(vec) for vec in field])
        self.play(ShowCreation(c4))
        self.play(ShowCreation(F1), run_time = 3)

class Curl(Scene):
    def construct(self):
        func = lambda p: np.array([
            -p[1], #x or i hat
            p[0], #y or j hat
        ])

        field = VectorField(func)
        field.set_color(ORANGE)
        F1 = TexMobject(r"\nabla \times \vec{F} > 0")
        c4 = Circle(color=BLUE_E, radius = 1)
        F1.shift(2*UP)

        self.play(*[GrowArrow(vec) for vec in field])
        self.play(ShowCreation(c4))
        self.play(ShowCreation(F1), run_time = 3)

