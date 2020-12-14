#!/usr/bin/env python3

"""

"""

__author__ = 'Job Maathuis'

import sys
from pypovray import pypovray, SETTINGS, models, logger
from vapory import Sphere, Scene, Texture, Pigment, Box, Finish


def frame(step):
    curr_time = step / eval(SETTINGS.NumberFrames) * eval(SETTINGS.FrameTime)
    logger.info(" @Time: %.3fs, Step: %d", curr_time, step)

    n_frames = eval(SETTINGS.NumberFrames)
    n_frames_loop = n_frames / 5  # amount of frames per loop

    x_start = -10
    x_end = x_start + 4
    x_distance = x_end - x_start
    x_distance_per_frame = (x_distance / (n_frames_loop / 2))

    y_start = -4
    y_end = 4
    y_distance = y_end - y_start
    y_distance_per_frame = (y_distance / (n_frames_loop / 2))

    # determine loop step
    if step - 1 // n_frames_loop == 0:
        loop = 0
    else:
        loop = step // n_frames_loop

    frame_in_loop = step - (loop * n_frames_loop)

    if frame_in_loop <= (n_frames_loop / 2):
        x_coord = x_start + (loop * 4) + frame_in_loop * x_distance_per_frame
        y_coord = y_start + frame_in_loop * y_distance_per_frame
    else:
        x_coord = x_end + (loop * 4)
        y_coord = y_end - (frame_in_loop - (n_frames_loop / 2)) * y_distance_per_frame

    sphere = Sphere([x_coord, y_coord, 0], 0.5, models.default_sphere_model)

    return Scene(models.default_camera,
                 objects=[sphere, models.default_ground, models.default_light])


def main(args):
    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
