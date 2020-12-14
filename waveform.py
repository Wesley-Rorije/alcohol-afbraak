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
from vapory import Sphere, Scene, Texture, Pigment, Box, Finish

def frame(step):
    curr_time = step / eval(SETTINGS.NumberFrames) * eval(SETTINGS.FrameTime)
    logger.info(" @Time: %.3fs, Step: %d", curr_time, step)

    nframes = eval(SETTINGS.NumberFrames)
    n_frames_loop = nframes / 5  # 16 frames per wave

    stylebox = Texture(Pigment('color', [0.80, 0.00, 1.00], 'filter', 0.7),
                       Finish('phong', 0.6, 'reflection', 0.4))

    x_start = -10
    x_end = 10
    x_distance = x_end - x_start
    distance_per_frame = x_distance / nframes

    y_start = 0
    y_end = 4
    y_distance = y_end - y_start
    #delen door 2 want we willen omhoog maar ook weer naar beneden
    y_distance_per_frame = y_distance / n_frames_loop
    iteratie = step // n_frames_loop

    x_coord = x_start + step * distance_per_frame
    correctie = iteratie * n_frames_loop # 1 * 16
    print(iteratie)
    step = step - correctie
    if step <= (n_frames_loop/2):
        y_coord = y_start + step * y_distance_per_frame
    else:
        y_coord = y_end - step * y_distance_per_frame

    box = Box([x_coord, y_coord, 0], [x_coord + 2, y_coord + 2, 2], stylebox)

    return Scene(models.default_camera,
                 objects=[box, models.default_ground, models.default_light])


def main(args):
    """ Main function performing the rendering """
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

