# Volume Calculator

![imag](https://user-images.githubusercontent.com/66405055/101341321-41959680-38c4-11eb-9b58-046df56947d5.PNG)



## Introduction

Use volume_calculator.py to measure the 2D,3D volume of the Nii image that needs to be measured, such as the image segmentation result.
The "nii.gz" file in the "segment_image_file" folder is input, and the output is saved in the "result" folder in csv format.

## Requirements

* [os](https://pypi.org/project/os-sys/)
* [numpy](https://pypi.org/project/numpy/)
* [matplotlib](https://pypi.org/project/matplotlib/)
* [nibabel](https://pypi.org/project/nibabel/)
* [pandas](https://pypi.org/project/pandas/)
* [glob](https://pypi.org/project/glob2/)

numpy = 1.18.4, nibabel = 2.4.0, pandas = 0.24.2:



## How to Use

> 1. Insert the image to measure the volume in the segment_image_file.

> 2. Enter python ./volume_calculator.py

> 3. The output csv file in "result"
