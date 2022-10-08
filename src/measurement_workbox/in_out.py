#import csv
#import gzip
#import json
#import pickle
#import xml
#import h5py
#import nibabel
#import imageio
import os
import sys


class InOut:
    def __init__(self) -> None:
        self.file = ''

    def read(self):
        self.loaded = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
