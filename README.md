
Collection of support scripts to read/write/process light field data.

Please don't hesitate to contact us for any kind of questions, feedback, wishes, or bug reports.

# Importing the light field data

You may use the provided Python scripts to read light fields, parameter files, disparity maps and depth maps as follows:

```python
import file_io.py
data_folder = "some_path/training/dino"

LF = file_io.read_lightfield(data_folder)
param_dict = file_io.read_parameters(data_folder)
depth_map = file_io.read_depth(data_folder, highres=True)
disparity_map = file_io.read_disparity(data_folder, highres=False)
```

Note that there are no public depth or disparity maps for the test scenes.


# General file io for PFM files

You may use the general IO methods `read_pfm()` and `write_pfm()` to process single channel PFM files such as the provided disparity maps. Call `write_pfm(disp_map, file_path)` to save your algorithm results.


# Creating visualizations and converting to hdf5

You may use our scripts to create figures or convert the data to hdf5.
We assume that the data and the scripts are placed in the same directory:
```javascript
|-- visualize_scenes.py
|-- convert2hdf5.py
|-- training
    |-- dino    
    |-- boxes    
|-- additional
|-- stratified
|-- test
```

To convert/visualize all downloaded scenes, run:
```bash
$ python convert2hdf5.py
$ python visualize_scenes.py
```

To convert/visualize specific scenes, run e.g.
```bash
$ python convert2hdf5.py -d "training/boxes,training/dino"
$ python visualize_scenes.py -d "training/boxes,training/dino"
```


# Dependencies

The scripts are tested with Python 2.7 and the dependencies as listed in the requirements.txt The modules h5py and matplotlib are optional. They are only required for the conversion/visualization.


# License
This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. 
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/. 
 
Authors: Katrin Honauer & Ole Johannsen 

Website: www.lightfield-analysis.net 


The 4D Light Field Benchmark was jointly created by the University of Konstanz and the HCI at Heidelberg University. If you use any part of the benchmark, please cite our paper "A dataset and evaluation methodology for depth estimation on 4D light fields". Thanks! 
 
 @inproceedings{honauer2016benchmark, 
 title={A dataset and evaluation methodology for depth estimation on 
 4D light fields}, 
 author={Honauer, Katrin and Johannsen, Ole and Kondermann, Daniel 
 and Goldluecke, Bastian}, 
 booktitle={Asian Conference on Computer Vision}, 
 year={2016}, 
 organization={Springer} 
 } 
