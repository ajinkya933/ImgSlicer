'''
Image Slicer: create a folder call Data and put all original images .JPG in Data folder. Data folder should be in same directory as this python script.
              create another folder called croppedtemp so all slices will be saved there.

Author: Hoda Gholami
Last Updated:10/17/2017

'''

from PIL import Image
from PIL import ImageDraw, ImageFont
import image_slicer
import time
import os
import sys
from multiprocessing import Pool 


def get_image_paths(folder):
  return (os.path.join(folder, f) 
      for f in os.listdir(folder) 
      if 'JPG' in f)

#image directory (we assume images name are like i.jpg, i from 1 to number of images
def imgslicer(imgpath): #pathtoimg
    if int(sys.argv[1])==1:#images will be sliced normally
        i=1
    elif int(sys.argv[1])==2: #images will be sliced double
        i=2
    img=Image.open(imgpath)
    if img.size >= (4000,4000):
        tiles = image_slicer.slice(imgpath, 36*i , save=False)
    elif img.size >= (2000,2000):
        tiles = image_slicer.slice(imgpath, 25*i , save=False)        
    elif img.size >= (1000,1000):
        tiles = image_slicer.slice(imgpath, 16*i , save=False)
    elif img.size >= (500,500):
        tiles = image_slicer.slice(imgpath, 9*i , save=False)
    else:
        tiles = image_slicer.slice(imgpath, 4*i , save=False)
    image_slicer.save_tiles(tiles, directory='croppedtemp', prefix=imgpath.split('/')[-1].split('.')[0], format='JPG')


start_time_Slicing = time.time()
folder=os.path.abspath("Data")
images=get_image_paths(folder)
pool = Pool() 
result=pool.map(imgslicer, images)
pool.close()
pool.join()
print("--- slicing done in %s seconds ---" % (time.time() - start_time_Slicing))
  
