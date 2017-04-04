#####################################################################
# This file is part of the 4D Light Field Benchmark.                #
#                                                                   #
# This work is licensed under the Creative Commons                  #
# Attribution-NonCommercial-ShareAlike 4.0 International License.   #
# To view a copy of this license,                                   #
# visit http://creativecommons.org/licenses/by-nc-sa/4.0/.          #
#####################################################################

import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import util
import file_io


def visualize_scene(data_folder):
    params = file_io.read_parameters(data_folder)

    if params["category"] == "test":
        print "Test scenes with hidden ground truth are not visualized."
        return

    light_field = file_io.read_lightfield(data_folder)
    disp_map_highres = file_io.read_disparity(data_folder, highres=True)
    disp_map_lowres = file_io.read_disparity(data_folder, highres=False)
    depth_map_lowres = file_io.read_depth(data_folder, highres=False)

    rows, cols = 1, 4
    cb_shrink = 0.7
    fig = plt.figure(figsize=(20, 4))
    plt.suptitle("%s:%s (%s)" % (params["category"].title(),
                                 params["scene"].title(),
                                 "x".join(str(i) for i in list(np.shape(light_field)))))

    plt.subplot(rows, cols, 1)
    plt.title("Center View")
    plt.imshow(light_field[4, 4, :, :, :])

    plt.subplot(rows, cols, 2)
    plt.title("Depth Map (%dx%d)" % np.shape(depth_map_lowres))
    cc = plt.imshow(depth_map_lowres, cmap=cm.viridis, interpolation="none")
    plt.colorbar(cc, shrink=cb_shrink)

    plt.subplot(rows, cols, 3)
    plt.title("Disparity Map (%dx%d)" % np.shape(disp_map_lowres))
    cc = plt.imshow(disp_map_lowres, cmap=cm.viridis, interpolation="none")
    plt.colorbar(cc, shrink=cb_shrink)

    plt.subplot(rows, cols, 4)
    plt.title("Disparity Map (%dx%d)" % np.shape(disp_map_highres))
    cc = plt.imshow(disp_map_highres, cmap=cm.viridis, interpolation="none")
    plt.colorbar(cc, shrink=cb_shrink)

    fig_name = os.path.join(data_folder, "scene.png")
    plt.savefig(fig_name, dpi=200, bbox_inches='tight')
    fig.clf()
    plt.close(fig)


if __name__ == '__main__':
    data_folders = util.parse_options()

    for data_folder in data_folders:
        print "visualizing: %s" % data_folder
        visualize_scene(data_folder)