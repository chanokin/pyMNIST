#! /usr/bin/python

from common import *
  
def read_label_file(filename, max_num_labels = 10000000000000):
  f = open(filename, "rb")
  
  try:
    temp = [f.read(1), f.read(1), f.read(1), f.read(1)]
    magic_number = num_from_byte_array(">I", temp)
    
    temp = [f.read(1), f.read(1), f.read(1), f.read(1)]
    number_of_labels = num_from_byte_array(">I", temp)
    
    lbl_idx = 0 
    labels = {}
    while lbl_idx < number_of_labels and lbl_idx < max_num_labels:
      labels[lbl_idx] = struct.unpack("B", f.read(1))[0]
      lbl_idx += 1
      
  finally:
    f.close()

  return labels



