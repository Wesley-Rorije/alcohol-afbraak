#!/usr/bin/env python3

"""
Simple example script for rendering an ATP molecule originating from a PDB file,
splitting a phosphate (Pi) group resulting in ADP + Pi.

Note: the resulting ADP molecule is not in a realistic conformation.

Uses a number of pre-defined Povray objects to simplify scene building
"""

__author__ = "wesley rorije"
__status__ = "Template"
__version__ = "2020"
from vapory import Sphere, Scene, LightSource, Camera, Texture,Pigment,Finish,Box,Cone,Cylinder
from pypovray import pypovray, pdb, models, load_config


def frame(step):
    lichtje = LightSource([2, 8, -5], 5.0)
    default_camera = Camera('location', [-5, 8, -20], 'look_at', [-5, 0, -5])
    style = Texture(Pigment('color', [0.80, 0.00, 1.00], 'filter', 0.7),
                       Finish('phong', 0.6, 'reflection', 0.4))

    linex = Cylinder([-15, 0, 0], [-10, 0, 0.5],0.1, style)
    liney = Cylinder([-15, 0, 0], [-15, 5, 0.2],0.1, style)
    linez = Cylinder([-15, 0, 0], [-15, 0.2, 5],0.1, style)


    conex = Cone([-10, 0, 0.5], 0.5,
                [-9, 0, 0.5], 0,
                style)
    coney = Cone([-15, 5, 0], 0.5,
                 [-15, 6, 0], 0,
                 style)
    conez = Cone([-15, 0, 5], 0.5,
                 [-15, 0, 6], 0,
                 style)

    # Return the Scene object for rendering
    return Scene(default_camera,
                 objects=[lichtje,linex,liney,linez,conex,coney,conez])


if __name__ == '__main__':
    # pypovray.SETTINGS = load_config('prototype.ini')
    # Render as an image
    pypovray.render_scene_to_png(frame)


