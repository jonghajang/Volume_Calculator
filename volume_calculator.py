#!/usr/bin/env python
# coding: utf-8

# In[184]:


import os
import os.path as path
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
import pandas as pd
import glob


# In[185]:


def print_progressbar(total, i):
    """
    total : total iteration number.
    i : iteration count, starting from 0.
    """
    import math
    step = 25 / total

    # Print the progress bar
    print('\r' + f'Progress: '
        f"[{'=' * int((i+1) * step) + ' ' * (25 - int((i+1) * step))}]"
        f"({math.floor((i+1) * 100 / (total))} %) ({i+1}/{total})",
        end='')
    if (i+1) == total: print("")


# ## image path

# In[186]:


IMAGE_PATH = 'segment_image_file'
file_paths = glob.glob(path.join(IMAGE_PATH,'*nii.gz'))


# In[187]:


file_paths


# ## image  load

# In[188]:


seg_images = [nib.load(path) for path in file_paths]


# In[189]:


## image shape example X x Y x Z

seg_images[0].shape


# ## volume calculate

# In[190]:


df = pd.DataFrame(columns=['img_name','voxel_count', 'Volume_mm^3', 'Volume_cc'])

for i in range(0,len(seg_images)):
    
    img = file_paths[i].split("/")[1]
    
    img_header = seg_images[i].header
    img_header_zooms = img_header.get_zooms()
    
    np_images = seg_images[i].get_data()
    np_images.shape  ## 512(x) x 512(y) x 50(z)images
    
    ## count number of voxel

    num_vox = np.sum(np_images > 0)
    

    ## 3D image has 3 dimension, so distinguish 2D from the calculation.

    if len(img_header_zooms)==3 :
        volume_mm = img_header_zooms[0]*img_header_zooms[1]*img_header_zooms[2]*num_vox
    else :
        volume_mm = img_header_zooms[0]*img_header_zooms[1]**num_vox
    
    ## calculate cc

    volume_cc = volume_mm*0.001


    ## save to dataframe

    df = df.append({
        'img_name' : img,
        'voxel_count' : num_vox,
        'Volume_mm^3' : volume_mm,
        'Volume_cc' : volume_cc
    }, ignore_index=True)
    print_progressbar(len(seg_images), i)


# ## dataframe_result

# In[191]:


os.mkdir("result")

df.to_csv("./result/result.csv")


# In[ ]:




