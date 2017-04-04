#####################################################################
# This file is part of the 4D Light Field Benchmark.                #
#                                                                   #
# This work is licensed under the Creative Commons                  #
# Attribution-NonCommercial-ShareAlike 4.0 International License.   #
# To view a copy of this license,                                   #
# visit http://creativecommons.org/licenses/by-nc-sa/4.0/.          #
#####################################################################

import optparse
import os


def get_all_data_folders(base_dir=None):
    if base_dir is None:
        base_dir = os.getcwd()

    data_folders = []
    categories = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    for category in categories:
        for scene in os.listdir(os.path.join(base_dir, category)):
            data_folder = os.path.join(*[base_dir, category, scene])
            if os.path.isdir(data_folder):
                data_folders.append(data_folder)

    return data_folders


def get_comma_separated_args(option, opt, value, parser):
    values = [v.strip() for v in value.split(',')]
    setattr(parser.values, option.dest, values)


def parse_options():
    parser = optparse.OptionParser()
    parser.add_option('-d', '--date_folder', type="string", action="callback", callback=get_comma_separated_args,
                      dest="data_folders", help="e.g. stratified/dots,test/bedroom")
    options, remainder = parser.parse_args()

    if options.data_folders is None:
        options.data_folders = get_all_data_folders(os.getcwd())
    else:
        options.data_folders = [os.path.abspath("%s") % d for d in options.data_folders]
        for f in options.data_folders:
            print f

    return options.data_folders