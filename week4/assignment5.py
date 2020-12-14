#!/usr/bin/env python3

from pypovray import pypovray, SETTINGS, models, pdb, logger
from vapory import Scene, Camera

import sys
import math

ETHANOL = None


def molecules():
    """ Creates molecules and contains other constants """
    global ETHANOL

    ETHANOL = pdb.PDBMolecule('{}/pdb/ethanol.pdb'.format(SETTINGS.AppLocation), center=True)


def frame(step):
    """ Renders an Ethanol molecule centered in the scene """
    # Dit is een beetje dubbel maar zonder gaat er opnieuw iets mis met self.atom
    ETHANOL = pdb.PDBMolecule('{}/pdb/ethanol.pdb'.format(SETTINGS.AppLocation), center=True)
    camera = Camera('location', [10, 0, 0], 'look_at', [0, 0, 0])
    nframes = eval(SETTINGS.NumberFrames)
    hele_rotatie = 2 * math.pi

    # When step is below or equal to 40, the ethanol molecule is devided into 2 parts.
    if step <= (nframes / 2):
        y_ass = (1 / (nframes / 2)) * step
        splitsing = ETHANOL.divide([7, 8], 'ethanol', offset=[0, y_ass, 0])

    else:
        # In the second half of the program, last 40 frames we rotate the molecules 360 degrees.
        y_ass = (1 / (nframes / 2)) * 40
        splitsing = ETHANOL.divide([7, 8], 'ethanol', offset=[0, y_ass, 0])
        step = step - 40
        rotatie_per_step = (hele_rotatie / nframes) * step
        ETHANOL.rotate([1, 0, 0], rotatie_per_step)
        splitsing.rotate([1, 0, 0], rotatie_per_step)

    # Return the Scene object for rendering.
    return Scene(camera,
                 objects=[models.default_light] +
                         ETHANOL.povray_molecule + splitsing.povray_molecule,
                 included=['colors.inc'])


def main(args):
    """ Main function performing the rendering """
    # Create static objects
    molecules()

    logger.info(" Total time: %d (frames: %d)", SETTINGS.Duration, eval(SETTINGS.NumberFrames))
    pypovray.render_scene_to_mp4(frame)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))