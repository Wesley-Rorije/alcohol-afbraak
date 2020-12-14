#!/usr/bin/env python3
"""
A python script using pypovray to create a scene with a rotating camera.

Uses a number of pre-defined vapory objects to simplify scene building

    usage:
        python3, pypovray, vapory library, legend object from previous assignment
"""

__author__ = "Wesley Rorije & Adrian Wilhelm"
__status__ = "development"
__version__ = "2020"

import sys
from pypovray import pypovray, models, SETTINGS, logger
from vapory import Sphere, Cylinder, Scene, Camera, Texture, Pigment, Finish
from assignment2a import legend
from math import pi, sin, cos


def frame(step):
    """ Returns the scene at step number (1 step per frame) """

    curr_time = step / eval(SETTINGS.NumberFrames) * eval(SETTINGS.FrameTime)
    logger.info(" @Time: %.3fs, Step: %d", curr_time, step)

    nframes = eval(SETTINGS.NumberFrames)

    style = Texture(Pigment('color', [0.80, 0.00, 1.00], 'filter', 0.7),
                    Finish('phong', 0.6, 'reflection', 0.4))

    cylinder = Cylinder([-6, -1, 4], [-6, 7, 4], 3, style)
    sphere = Sphere([6, 2, -2], 3, style)
    leg = legend([-15, 0, 0], 5)
    radius = 25
    z_start = 0
    x_start = 0

    alpha = (-pi/2) + (step * 2 * pi / nframes)
    # For each step, de difference in the x and z positions is equal to the radius time the sin and cos of alpha.
    x_coord = radius * cos(alpha)
    z_coord = radius * sin(alpha)
    # Adding or subtracting the difference of the position for each step from the original camera position.
    x = x_start + x_coord
    z = z_start - z_coord
    return Scene(Camera('location', [x, 8, z], 'look_at', [0, 0, 0]),
                 objects=[models.checkered_ground, models.default_light, cylinder, sphere] + leg)


def main(args):
    """ Main function performing the rendering """
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
