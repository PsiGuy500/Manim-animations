## In the command terminal type in:

#       python -m manim projects\VectorFields.py VectorFieldExample
#       python -m manim projects\VectorFields.py FlowingVectorField

from manimlib.imports import *
import numpy as np

class VectorFieldExample(Scene):
    def construct(self):
        func = lambda p: np.array([
            2*p[0], #x or i hat
            p[1]**2, #y or j hat
        ])

        field = VectorField(func)
        field.set_color(ORANGE)
        self.play(*[GrowArrow(vec) for vec in field])

class FlowingVectorField(Scene):
    def construct(self):
        func1 = lambda p : np.array([
            1,             # x
            np.sin(p[0])   #y
        ])
        func2 = lambda o : np.array([
            1,              # x
            -np.cos(o[0])   #y
        ])

        field1 = VectorField(func1)
        field1.set_color_by_gradient(BLUE_D, BLUE_E)
        self.add(field1)

        field2 = VectorField(func2)
        field2.set_color_by_gradient(BLUE_E, BLUE_D)

        field1copy = VectorField(func1)
        field1copy.set_color_by_gradient(BLUE_D, BLUE_E)

        for i in range(2,4):
            self.play(Transform(field1, field2))
            self.play(Transform(field1, field1copy))

