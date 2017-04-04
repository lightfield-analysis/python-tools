#####################################################################
# This file is part of the 4D Light Field Benchmark.                #
#                                                                   #
# This work is licensed under the Creative Commons                  #
# Attribution-NonCommercial-ShareAlike 4.0 International License.   #
# To view a copy of this license,                                   #
# visit http://creativecommons.org/licenses/by-nc-sa/4.0/.          #
#####################################################################

import os
import file_io

import util


def convert_to_hdf5(data_folder, tgt=None):
    if tgt is None:
        tgt = os.path.join(data_folder, "scene.h5")

    scene = dict()
    scene["LF"] = file_io.read_lightfield(data_folder)
    params = file_io.read_parameters(data_folder)

    if params["category"] != "test":
        scene["disp_highres"] = file_io.read_disparity(data_folder, highres=True)
        scene["disp_lowres"] = file_io.read_disparity(data_folder, highres=False)
        scene["depth_highres"] = file_io.read_depth(data_folder, highres=True)
        scene["depth_lowres"] = file_io.read_depth(data_folder, highres=False)

    file_io.write_hdf5(scene, tgt)


if __name__ == '__main__':
    data_folders = util.parse_options()

    for data_folder in data_folders:
        print "converting: %s" % data_folder
        convert_to_hdf5(data_folder)
