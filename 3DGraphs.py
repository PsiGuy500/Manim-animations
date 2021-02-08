## In the command terminal type in:

#       python -m manim projects\ThreeDGraphs.py Hello3dWorld
#       python -m manim projects\ThreeDGraphs.py MoveCamera
#       python -m manim projects\ThreeDGraphs.py ParametricCurve3D
#       python -m manim projects\ThreeDGraphs.py transformingCurves
#       python -m manim projects\ThreeDGraphs.py ParametricSurfacesAnimation
#       python -m manim projects\ThreeDGraphs.py ParametricSurfaceTransform

from manimlib.imports import *
import numpy as np



class Hello3dWorld(ThreeDScene):
    def construct(self):
        axis_config = {
            "x_min": -5,

            "x_max": 5,
            "y_min": -5,
            "y_max": 5,
            "z_min": -5,
            "z_max": 5,
        }
        axes = ThreeDAxes(**axis_config)
        self.set_camera_orientation(phi = 80*DEGREES, theta = -40*DEGREES, distance = 6)

        text3d = TextMobject("Hello 3d World").scale(2)
        text3d.rotate(PI/2, axis = RIGHT)

        text2d = TextMobject("Hello Viewer").scale(2)
        text2d.to_edge(UP+RIGHT)
        self.add_fixed_in_frame_mobjects(text2d)

        self.play(ShowCreation(axes))
        self.play(ShowCreation(text3d))



class MoveCamera(ThreeDScene):
    def construct(self):
        axis_config = {
            "x_min": -5,
            "x_max": 5,
            "y_min": -5,
            "y_max": 5,
            "z_min": -5,
            "z_max": 5,
        }
        axes = ThreeDAxes(**axis_config)
        self.set_camera_orientation(phi = 60*DEGREES, theta = 60*DEGREES, distance = 8)
        self.add(axes)
        self.wait(2)
        self.move_camera(phi = -45*DEGREES, theta = 45*DEGREES, distance = 6)
        self.begin_ambient_camera_rotation(rate = 2)
        self.wait(5)
        self.stop_ambient_camera_rotation()



class ParametricCurve3D(ThreeDScene):
    def construct(self):
        axis_config = {
            "x_min": -5,
            "x_max": 5,
            "y_min": -5,
            "y_max": 5,
            "z_min": -5,
            "z_max": 5,
        }
        axes = ThreeDAxes(**axis_config)
        self.set_camera_orientation(phi = 75*DEGREES, theta = 45*DEGREES, distance = 8)
        self.add(axes)

        curve = ParametricFunction(lambda t: np.array([
            np.cos(t), np.sin(3*t), np.cos(5*t)
        ]), color = RED, t_min = -TAU, t_max = TAU)

        self.begin_ambient_camera_rotation(rate=0.9)
        self.play(ShowCreation(curve), run_time = 3)



class transformingCurves(ThreeDScene):
    def construct(self):
        axis_config = {
            "x_min": -5,
            "x_max": 5,
            "y_min": -5,
            "y_max": 5,
            "z_min": -5,
            "z_max": 5,
        }
        axes = ThreeDAxes(**axis_config)
        self.set_camera_orientation(phi = 45*DEGREES, theta = 45*DEGREES, distance = 4)
        self.add(axes)

        curve1 = ParametricFunction(lambda t: np.array([
            np.cos(t), np.sin(3*t), np.cos(5*t)
        ]), color = RED, t_min = -TAU, t_max = TAU)

        curve2 = ParametricFunction(lambda t: np.array([
            np.exp(-0.1*t)*np.cos(t), np.exp(-0.1*t)*np.sin(t), 2
        ]), color = BLUE, t_min = -TAU, t_max = TAU)

        self.begin_ambient_camera_rotation(rate=0.9)
        self.play(ShowCreation(curve1), run_time = 2)
        self.play(Transform(curve1, curve2))



class ParametricSurfacesAnimation(ThreeDScene):
    def construct(self):
        axis_config = {
            "x_min": -5,
            "x_max": 5,
            "y_min": -5,
            "y_max": 5,
            "z_min": -5,
            "z_max": 5,
        }
        axes = ThreeDAxes(**axis_config)
        self.set_camera_orientation(phi = 70*DEGREES, theta = 70*DEGREES, distance = 10)
        self.add(axes)
        self.begin_ambient_camera_rotation(rate=0.2)

        curvature = ParametricSurface(
            lambda u, v: np.array([
                u, v, -1*2.7**(-(u**2)-(v**2))
            ]), v_max = 3, v_min = -3, u_max =3, u_min = -3, resolution=(10,10), checkerboard_colors = [DARK_GREY, DARKER_GREY]
        )

        planet = ParametricSurface(
            lambda u, v: np.array([
                np.cos(u)*np.cos(v),
                np.cos(u)*np.sin(v),
                np.sin(u)
            ]), v_max = TAU, v_min = 0, u_max =PI/2, u_min = -PI/2, resolution=(10,10), checkerboard_colors = [GREEN_E, BLUE_D]
        )

        self.play(ShowCreation(curvature.scale(2)), run_time = 5)
        self.play(ShowCreation(planet.scale(2)), run_time = 5)





class ParametricSurfaceTransform(ThreeDScene):
    def construct(self):
        axis_config = {
            "x_min": -5,
            "x_max": 5,
            "y_min": -5,
            "y_max": 5,
            "z_min": -5,
            "z_max": 5,
        }
        axes = ThreeDAxes(**axis_config)
        self.set_camera_orientation(phi = 70*DEGREES, theta = 70*DEGREES, distance = 10)
        self.add(axes)
        self.begin_ambient_camera_rotation(rate=0.2)

        HeatedSurface = ParametricSurface(
            lambda u, v: np.array([
                u,v,np.sin(v)+np.cos(u)
            ]), v_max = 5, v_min = -5, u_max =5, u_min = -5, resolution=(10,10), checkerboard_colors = [RED, RED]
        )

        self.add(HeatedSurface)

        CooledSurface = ParametricSurface(
            lambda u, v: np.array([
                u,v, 0.1*np.cos(v)+0.2*np.sin(u)
            ]), v_max = 5, v_min = -5, u_max = 5, u_min = -5, resolution=(10,10), checkerboard_colors = [BLUE, BLUE]
        )

        self.play(Transform(HeatedSurface, CooledSurface), run_time = 5)





