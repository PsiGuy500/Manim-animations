## In the command terminal type in:

#       python -m manim projects\ParametricPolar.py parametric
#       python -m manim projects\ParametricPolar.py polar

from manimlib.imports import *
import numpy as np

class parametric(GraphScene):
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

        curve = ParametricFunction(lambda t: np.array([np.exp(np.sin(3*t)), 3*(np.cos(t+1))**2, 0

        ]), color = PURPLE, t_min = -0.1, t_max = 6.2)

        self.play(ShowCreation(curve), run_time = 4)




## To graph polar functions, you need to turn the polar coordinates into their respective parametric coordinates.

## For example:      r = 2*cos(3theta)          x = r*cos(theta)        y = r*sin(theta)
## Ergo:                              x(t) = 2*cos(3t)*cos(t)      y(t) = 2*cos(3t)*sin(t)


class polar(GraphScene):
    CONFIG = {
        "y_max": 4,
        "y_min": -4,
        "x_max": 5,
        "x_min": -5,
        "x_axis_width": 9,
        "y_tick_frequency": 1,
        "x_tick_frequency": 1,
        "axes_color": GREY,
        "graph_origin": ORIGIN,
        "x_label_direction": DOWN,
        "y_label_direction": LEFT
    }

    def construct(self):
        self.setup_axes(animate=False)

        curve = ParametricFunction(lambda t: np.array([2*np.cos(3*t)*np.cos(t), 2*np.cos(3*t)*np.sin(t), 0

        ]), color = PURPLE, t_min = 0, t_max = 2*PI)

        self.play(ShowCreation(curve), run_time = 4)