import struct
import numpy as np

def num_from_byte_array(fmt, bytes):
  return struct.unpack(fmt, "".join(bytes))[0]
