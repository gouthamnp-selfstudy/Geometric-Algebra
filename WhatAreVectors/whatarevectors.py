from math import ceil

from manim import *

config.pixel_width = 540
config.pixel_height = 540
config.frame_width = 14.0
config.frame_height = 14.0
config.frame_rate = 60


class VectorScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        plane = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-7, 7, 1],
            x_length=12,
            y_length=12,
            background_line_style=
            {
                "stroke_color": GRAY_C,
                "stroke_width": 2,
                "stroke_opacity": 0.6,
            },
            axis_config=
            {
                "color": BLACK,
                "include_tip": True,
            },
        )
        
        i_mult = ValueTracker(1)
        j_mult = ValueTracker(1)
        
        i_hat = always_redraw(
            lambda: Vector(
                plane.c2p(i_mult.get_value(), 0, 0) - plane.c2p(0, 0, 0),
                color=GREEN)
        )
        
        j_hat = Vector(
            plane.c2p(0, 1, 0) - plane.c2p(0, 0, 0),
            color=RED
        )
        j_hat_attached = always_redraw(
            lambda: Vector(
                plane.c2p(0, j_mult.get_value(), 0) - plane.c2p(0, 0, 0),
                color=RED
            ).shift(i_hat.get_end())
        )
        
        label_i = always_redraw(
            lambda: MathTex(
                ((f"{round(i_mult.get_value())}" if round(i_mult.get_value()) != 1 else "-" if round(i_mult.get_value()) == -1 else "") + r"\hat{\imath}") if round(i_mult.get_value()) != 0 else r"\vec{0}",
                color=BLACK
            ).next_to(i_hat.get_end(), DOWN)
        )
        
        label_j = MathTex(r"\hat{\jmath}", color=BLACK).next_to(j_hat.get_end(), LEFT)
        label_j_attached = always_redraw(
            lambda: MathTex(
                ((f"{round(j_mult.get_value())}" if round(j_mult.get_value()) != 1 else "-" if round(j_mult.get_value()) == -1 else "") + r"\hat{\jmath}") if round(j_mult.get_value()) != 0 else r"\vec{0}",
                color=BLACK
            ).next_to(j_hat_attached.get_end(), LEFT)
        )

        self.play(FadeIn(plane))
        self.play(GrowArrow(i_hat), Write(label_i))
        self.play(GrowArrow(j_hat), Write(label_j))
        
        self.play(ReplacementTransform(j_hat, j_hat_attached), ReplacementTransform(label_j, label_j_attached))
        
        self.play(
            i_mult.animate.set_value(6),
            run_time=4,
            rate_func=smooth
        )
        
        self.play(
            i_mult.animate.set_value(0),
            j_mult.animate.set_value(6),
            run_time=2,
            rate_func=smooth
        )
        self.play(
            i_mult.animate.set_value(-6),
            j_mult.animate.set_value(-6),
            run_time=2,
            rate_func=smooth
        )
        
        self.play(
            i_mult.animate.set_value(3),
            j_mult.animate.set_value(4),
            run_time=2,
            rate_func=smooth
        )
        self.play(
            i_mult.animate.set_value(0),
            j_mult.animate.set_value(0),
            run_time=2,
            rate_func=smooth
        )
