#!/usr/bin/env python3

from pypovray import pypovray, SETTINGS, models, pdb
from vapory import Scene, Camera


def molecules():
    ''' Creates molecules and contains other constants '''
    global Molecule_name
    Molecule_name = pdb.PDBMolecule('{}/pdb/nameofyourmolecule.pdb'.format(SETTINGS.AppLocation), center=True)


def frame(step):
    ''' Renders an molecule centered in the scene '''
    camera = Camera('location', [10, 0, 0], 'look_at', [0, 0, 0])

    # Return the Scene object for rendering
    return Scene(camera,
                 objects=[models.default_light] +
                         Molecule_name.povray_molecule, included=['colors.inc'])


if __name__ == '__main__':
    # Create molecule(s)
    molecules()

    # Render as a single image
    pypovray.render_scene_to_png(frame)
