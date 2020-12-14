#!/usr/bin/env python3
"""
Simple template moving a sphere from left to right using Povray

Uses a number of pre-defined Povray objects to simplify scene building

    usage:
        python3 template.py
"""

__author__ = "Wesley Rorije"
__status__ = "development"
__version__ = "2020"

import sys
from pypovray import pypovray, SETTINGS, models, logger
from vapory import Sphere, Scene, Texture, Pigment, Box, Finish,Cylinder, LightSource,Camera
from assignment2a import legend
from math import pi, sin, cos

def frame(step):
    curr_time = step / eval(SETTINGS.NumberFrames) * eval(SETTINGS.FrameTime)
    logger.info(" @Time: %.3fs, Step: %d", curr_time, step)

    nframes = eval(SETTINGS.NumberFrames)

    style = Texture(Pigment('color', [0.80, 0.00, 1.00], 'filter', 0.7),
                       Finish('phong', 0.6, 'reflection', 0.4))

    cylinder = Cylinder([-6, -1, 4], [-6, 7, 4], 3, style)
    sphere = Sphere([6, 2, -2], 3, style)
    leg = legend([-15, 0, 0], 5)

    radius = 25
    z_start = -25
    x_start = 0
    alpha = (-pi / 2) + (step * 2 * pi / nframes)
    x_coord = radius * cos(alpha)
    z_coord = radius * sin(alpha)
    x = x_start + x_coord
    z = z_start - z_coord


    camera_x = 0
    camera_z = -25

    # x gaat links en rechts en z verder de diepte in en terug -25?
    camera = Camera('location', [camera_x, 8, camera_z], 'look_at', [0, 0, 0])



    return Scene(camera,
                 objects=[cylinder,sphere,models.default_light,models.checkered_ground] + shapes, included=['colors.inc'])


def main(args):
    """ Main function performing the rendering """
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

