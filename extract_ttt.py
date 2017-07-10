import cv2
import pylab

from pyMNIST.read_mnist_img import *
from pyMNIST.read_mnist_label import *

images_file = "train-images-idx3-ubyte"

labels_file = "train-labels-idx1-ubyte"

mnist_lbls = read_label_file(labels_file)

mnist_imgs = read_img_file(images_file, labels=mnist_lbls)

#fig = pylab.figure()
#pylab.imshow(mnist_imgs[0]["img"])
#pylab.show()

for idx in mnist_imgs.keys():
  label = mnist_imgs[idx]["lbl"]
  out_filename = "train/%s__idx_%06d__lbl_%02d_.png"%(images_file, idx, label)
  
  cv2.imwrite(out_filename, mnist_imgs[idx]["img"])

