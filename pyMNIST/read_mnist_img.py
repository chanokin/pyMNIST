#! /usr/bin/python

import struct
import numpy as np
from common import *
  
def read_img_file(filename, start_idx = 0, max_num_images = 10000000000, labels=None):
  f = open(filename, "rb")
  
  try:
    temp = [f.read(1), f.read(1), f.read(1), f.read(1)]
    magic_number = num_from_byte_array(">I", temp)
    
    temp = [f.read(1), f.read(1), f.read(1), f.read(1)]
    number_of_images = num_from_byte_array(">I", temp)
    
    temp = [f.read(1), f.read(1), f.read(1), f.read(1)]
    rows_per_image = num_from_byte_array(">I", temp)
    
    temp = [f.read(1), f.read(1), f.read(1), f.read(1)]
    cols_per_image = num_from_byte_array(">I", temp)

    img_idx = 0 
    images = {}
    max_num_images = start_idx + max_num_images
    while img_idx < number_of_images and img_idx < max_num_images:
      
      if img_idx < start_idx:
        for r in xrange(rows_per_image):
          for c in xrange(cols_per_image):
            t = struct.unpack("B", f.read(1))[0]

        img_idx += 1
        continue
        
      img = np.zeros((rows_per_image, cols_per_image))
      for r in xrange(rows_per_image):
        for c in xrange(cols_per_image):
          img[r, c] = struct.unpack("B", f.read(1))[0]
                    
      if labels is not None:
        images[img_idx] = {'img': img, 'lbl': labels[img_idx]}
      else:
        images[img_idx] = {'img': img}

      img_idx += 1
      
  finally:
    f.close()

  return images





