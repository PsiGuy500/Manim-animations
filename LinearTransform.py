## In the command terminal type in:

#       python -m manim projects\LinearTransform.py Vectors
#       python -m manim projects\LinearTransform.py LinearTransformation

from manimlib.imports import *
import numpy as np

class Vectors(VectorScene):
    CONFIG = {
        "show_basis_vectors": True,
        "foreground_plane_kwargs": {
            "x_max": 10,
            "x_min": -10,
            "y_max": 10,
            "y_min": -10
        },

    }
    def construct(self):
        self.add_axes(animate=False)
        self.add_plane(animate=False)

        BasisVecs = self.get_basis_vectors()
        self.add(BasisVecs)

        myVec = Vector([3,2])
        myVec.set_color(ORANGE)
        self.add_vector(myVec)

        labelVector = vector_coordinate_label(myVec, color = ORANGE)
        self.play(ShowCreation(labelVector))

class LinearTransformation(LinearTransformationScene):
    CONFIG = {
        "show_basis_vectors": True,
        "foreground_plane_kwargs": {
            "x_max": 10,
            "x_min": -10,
            "y_max": 10,
            "y_min": -10
        },

    }
    def construct(self):
        self.setup()

        myVec = Vector([3,2])
        myVec.set_color(ORANGE)
        self.add_vector(myVec)

        labelVector = vector_coordinate_label(myVec, color = ORANGE)
        self.add_moving_mobject(myVec)

        text = TextMobject("Shear")
        text.scale(2)
        self.add_transformable_mobject(text)

        self.apply_matrix([[2,-1], [0,1]])


        







