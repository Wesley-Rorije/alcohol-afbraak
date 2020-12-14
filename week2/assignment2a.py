#!/usr/bin/env python

"""
Assignment 2 Template script
----------------------------

This template contains a single function ('legend') that needs to be completed
to make an importable legend for use in other programs.

* Write the function docstring explaining what it does and its arguments
* Fill in the two dictionaries ('cylinders' and 'cones')

This function stores all objects to render in dictionaries, try to understand
the code in this template:
    * open an Idle or interactive Python session
    * create a 'start_position' list with values [0, 10, 20]
    * copy/ paste code from the template into IDle to see its effects
    * print/ inspect contents of the 'cylinder_coords' and 'cones_coords_*' dictionaries
    * experiment with any other unclear statements

"""

from vapory import Cylinder, Cone, Pigment, Texture, Finish, Scene, LightSource, Camera
from pypovray import pypovray, pdb, models, load_config

def legend(start_position, axis_length):
    """ Function docstring ... """

    # Reduce the AXIS_LENGTH by the length of the Cone (1) so that
    # the total length is exactly the AXIS_LENGTH
    axis_length -= 1

    # Initialize the Cylinder END-position to a COPY of the start position
    cylinder_coords_end = {
        'x': list(start_position),
        'y': list(start_position),
        'z': list(start_position)
    }

    # Add the AXIS_LENGTHs to the corresponding coordinate
    cylinder_coords_end['x'][0] += axis_length
    cylinder_coords_end['y'][1] += axis_length
    cylinder_coords_end['z'][2] += axis_length

    ''' CREATE THE CYLINDERS'''

    style = Texture(Pigment('color', [0.80, 0.00, 1.00], 'filter', 0.7),
                       Finish('phong', 0.6, 'reflection', 0.4))
    linex = Cylinder(start_position, cylinder_coords_end['x'], 0.1, style)
    liney = Cylinder(start_position, cylinder_coords_end['y'], 0.1, style)
    linez = Cylinder(start_position, cylinder_coords_end['z'], 0.1, style)

    cylinders = {
        'x': linex,
        'y': liney,
        'z': linez
    }

    # Cone START is the same as the Cylinder END, so we COPY these lists
    cones_coords_start = {
        'x': list(cylinder_coords_end['x']),
        'y': list(cylinder_coords_end['y']),
        'z': list(cylinder_coords_end['z'])
    }

    # Copy the START as END coordinate
    cones_coords_end = {
        'x': list(cones_coords_start['x']),
        'y': list(cones_coords_start['y']),
        'z': list(cones_coords_start['z'])
    }

    # Extend the tip of the cones with length 1
    cones_coords_end['x'][0] += 1
    cones_coords_end['y'][1] += 1
    cones_coords_end['z'][2] += 1

    ''' CREATE THE CONES '''

    conex = Cone(cones_coords_start['x'], 0.5,cones_coords_end['x'], 0,style)
    coney = Cone(cones_coords_start['y'], 0.5, cones_coords_end['y'], 0, style)
    conez = Cone(cones_coords_start['z'], 0.5, cones_coords_end['z'], 0, style)

    cones = {
        'x': conex,
        'y': coney,
        'z': conez
    }

    # Add ALL objects to a LIST and return
    legend_objects = list(cylinders.values()) + list(cones.values())

    return legend_objects


def frame(step):
    lichtje = LightSource([2, 8, -5], 5.0)
    default_camera = Camera('location', [-5, 8, -20], 'look_at', [-5, 0, -5])
    shapes = legend([-15, 0, 0],5)
    # Return the Scene object for rendering
    return Scene(default_camera,
                 objects=[lichtje] + shapes)

if __name__ == '__main__':
    # pypovray.SETTINGS = load_config('prototype.ini')
    # Render as an image
    pypovray.render_scene_to_png(frame)