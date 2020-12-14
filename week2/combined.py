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
from vapory import Sphere, Scene, LightSource, Camera, Texture,Pigment,Finish,Box,Cone
from pypovray import pypovray, pdb, models, load_config
from assignment2a import legend

def frame(step):
    lichtje = LightSource([2, 8, -5], 5.0)
    default_camera = Camera('location', [0, 4, -40], 'look_at', [0, 2, -5])

    ''' Creates a sphere and places this in a scene '''
    stylebox = Texture(Pigment('color', [0.80, 0.00, 1.00], 'filter', 0.7),
                        Finish('phong', 0.6, 'reflection', 0.4))
    boxright = Box([3, -2, -3], [5, 6, 4], stylebox)
    boxleft = Box([-5, -2, -3], [-3, 6, 4], stylebox)
    boxupper = Box([-5, 6, -3], [5, 8, 4], stylebox)
    boxbottom = Box([-5, -4, -3], [5, -2, 4], stylebox)

    styleball = Texture(Pigment('color', [0.80, 0.00, 1.00], 'filter', 0.7))
    centerball = Sphere([0, 2, 0], 3, styleball)

    conetop =Cone([0, 8, 0], 3,
                  [0, 12, 0], 0,
                    stylebox)
    conebottom = Cone([0, -4, 0], 3,
                      [0, -8, 0], 0,
                    stylebox)
    coneleft = Cone([-5, 2, 0], 3,
                    [-11, 2, 0], 0,
                    stylebox)
    coneright = Cone([5, 2, 0], 3,
                     [11, 2, 0], 0,
                    stylebox)
    shapes = legend([-15, 0, 0],5)
    # Return the Scene object for rendering
    return Scene(default_camera,
                 objects=[lichtje, centerball,
                          boxright,boxleft,
                          boxupper,boxbottom,
                          conetop,conebottom,coneleft,coneright] +shapes,included = ['colors.inc'])
    # return Scene(models.default_camera,
    #              objects=[models.default_light, sphere])


if __name__ == '__main__':
    # pypovray.SETTINGS = load_config('prototype.ini')
    # Render as an image
    pypovray.render_scene_to_png(frame)


