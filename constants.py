import os, sys

if getattr(sys, 'frozen', False):
        # running in a bundle
        DATA_LOC = os.path.join(sys._MEIPASS, 'data')
else :
        # running live
        DATA_LOC = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'data')

VERSION = 'v3.3.0'

# list of image extensions that imageio can write to
EXT_LIST = ['tif', 'tiff', 'stk', 'lsm', 'bmp', 'ps', 'eps', 'gif',
            'ico', 'im', 'jfif', 'jpe', 'jpg', 'jpeg', 'mpo', 'pcx',
            'png', 'pbm', 'pgm', 'ppm', 'bw', 'rgb', 'rgba', 'sgi',
            'tga', 'bsdf', 'npz']

# list of color spaces that colorspacious can correctly perform a deltaE calculation in
CSPACE_LIST = ['CAM02-UCS', 'CAM02-LCD', 'CAM02-SCD',
               'CIELab', 'sRGB1', 'sRGB1-linear', 'XYZ1']