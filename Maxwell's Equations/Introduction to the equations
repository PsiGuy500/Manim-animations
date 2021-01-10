#in the command terminal type in:

#       python -m manim projects\LatexForm.py MaxwellEqDiff
#       python -m manim projects\LatexForm.py MaxwellEqInt
#       python -m manim projects\LatexForm.py Intro

from manimlib.imports import *
import numpy as np

class MaxwellEqDiff(Scene):
    def construct(self):
        T = TextMobject("These are Maxwell's equations in differential form")

        ME1 = TexMobject(r"\nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0}")
        B1 = Brace(ME1, DOWN)
        t1 = B1.get_text("Gauss' law")
        box1 = SurroundingRectangle(ME1)
        box2 = SurroundingRectangle(ME1)
        box1.set_stroke(BLUE)
        box2.set_stroke(BLUE)

        ME2 = TexMobject(r"\nabla \cdot \vec{B} = 0")
        B2 = Brace(ME2, UP)
        t2 = B2.get_text("Gauss' law for magnetism")
        box3 = SurroundingRectangle(ME2)
        box4 = SurroundingRectangle(ME2)
        box3.set_stroke(BLUE)
        box4.set_stroke(BLUE)

        ME3 = TexMobject(r"\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}")
        B3 = Brace(ME3, UP)
        t3 = B3.get_text("Faraday's law of induction")
        box5 = SurroundingRectangle(ME3)
        box6 = SurroundingRectangle(ME3)
        box5.set_stroke(BLUE)
        box6.set_stroke(BLUE)

        ME4 = TexMobject(r"\nabla \times \vec{B} = \mu_0 (\vec{J} +\epsilon_0 \frac{\partial \vec{E}}{\partial t})")
        B4 = Brace(ME4, DOWN)
        t4 = B4.get_text("Ampere's law")
        box7 = SurroundingRectangle(ME4)
        box8 = SurroundingRectangle(ME4)
        box7.set_stroke(BLUE)
        box8.set_stroke(BLUE)

        G1 = VGroup(ME1, box1)
        G2 = VGroup(box2, B1, t1)
        t1.scale(0.6)
        G2.to_edge(UP + LEFT)

        G3 = VGroup(ME2, box3)
        G4 = VGroup(box4, B2, t2)
        t2.scale(0.4)
        G4.to_edge(DOWN+LEFT)

        G5 = VGroup(ME3, box5)
        G6 = VGroup(box6, B3, t3)
        t3.scale(0.45)
        G6.to_edge(DOWN+RIGHT)

        G7 = VGroup(ME4, box7)
        G8 = VGroup(box8, B4, t4)
        t4.scale(0.6)
        G8.to_edge(UP + RIGHT)

        self.play(ShowCreation(G1), G1.to_edge, UP+LEFT, run_time = 4)
        self.play(ShowCreation(G2), run_time = 5)
        self.play(ShowCreation(G3), G3.to_edge, DOWN+LEFT, run_time = 4)
        self.play(ShowCreation(G4), run_time = 5)
        self.play(ShowCreation(G5), G5.to_edge, DOWN+RIGHT, run_time = 4)
        self.play(ShowCreation(G6), run_time = 5)
        self.play(ShowCreation(G7), G7.to_edge, UP+RIGHT, run_time = 4)
        self.play(ShowCreation(G8), run_time = 5)
        self.play(Write(T), run_time = 5)

class MaxwellEqInt(Scene):
    def construct(self):
        T = TextMobject("These are Maxwell's equations in integral form")

        ME1 = TexMobject(r"\oiint_S{\textbf{E} \cdot d\textbf{A}} = \frac{Q_{enclosed}}{\epsilon_0}")
        B1 = Brace(ME1, DOWN)
        t1 = B1.get_text("Gauss' law")
        box1 = SurroundingRectangle(ME1)
        box2 = SurroundingRectangle(ME1)
        box1.set_stroke(BLUE)
        box2.set_stroke(BLUE)

        ME2 = TexMobject(r"\oint{\textbf{E} \cdot d\textbf{s}} = -\frac{d\Phi_B}{dt}")
        B2 = Brace(ME2, UP)
        t2 = B2.get_text("Gauss' law for magnetism")
        box3 = SurroundingRectangle(ME2)
        box4 = SurroundingRectangle(ME2)
        box3.set_stroke(BLUE)
        box4.set_stroke(BLUE)

        ME3 = TexMobject(r"\oiint_S{\textbf{B} \cdot d{\textbf{A}}} = 0")
        B3 = Brace(ME3, UP)
        t3 = B3.get_text("Faraday's law of induction")
        box5 = SurroundingRectangle(ME3)
        box6 = SurroundingRectangle(ME3)
        box5.set_stroke(BLUE)
        box6.set_stroke(BLUE)

        ME4 = TexMobject(r"\oint{\textbf{B} \cdot d\textbf{s}} = \mu_0 I + \frac{1}{c^2}\frac{d\Phi_E}{dt}")
        B4 = Brace(ME4, DOWN)
        t4 = B4.get_text("Ampere's law")
        box7 = SurroundingRectangle(ME4)
        box8 = SurroundingRectangle(ME4)
        box7.set_stroke(BLUE)
        box8.set_stroke(BLUE)

        G1 = VGroup(ME1, box1)
        G2 = VGroup(box2, B1, t1)
        t1.scale(0.6)
        G2.to_edge(UP + LEFT)

        G3 = VGroup(ME2, box3)
        G4 = VGroup(box4, B2, t2)
        t2.scale(0.6)
        G4.to_edge(DOWN+LEFT)

        G5 = VGroup(ME3, box5)
        G6 = VGroup(box6, B3, t3)
        t3.scale(0.55)
        G6.to_edge(DOWN+RIGHT)

        G7 = VGroup(ME4, box7)
        G8 = VGroup(box8, B4, t4)
        t4.scale(0.6)
        G8.to_edge(UP + RIGHT)

        self.play(ShowCreation(G1), G1.to_edge, UP+LEFT, run_time = 4)
        self.play(ShowCreation(G2), run_time = 5)
        self.play(ShowCreation(G3), G3.to_edge, DOWN+LEFT, run_time = 4)
        self.play(ShowCreation(G4), run_time = 5)
        self.play(ShowCreation(G5), G5.to_edge, DOWN+RIGHT, run_time = 4)
        self.play(ShowCreation(G6), run_time = 5)
        self.play(ShowCreation(G7), G7.to_edge, UP+RIGHT, run_time = 4)
        self.play(ShowCreation(G8), run_time = 5)
        self.play(Write(T), run_time = 5)

class Intro(Scene):
    def construct(self):
        r = TextMobject("But what do these equations mean conceptually?")
        u = TextMobject("Lets visualize them.")
        u.next_to(r, DOWN)
        ru = VGroup(r, u)
        self.play(Write(ru), run_time = 7)












