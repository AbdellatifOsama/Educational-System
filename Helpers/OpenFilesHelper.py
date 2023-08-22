import datetime
from tkinter import *
from PIL import Image

import os
def open(path):
    os.startfile(path)

def GetAbsPath(filepath):
    dir = os.path.abspath(__file__).split("\\")
    path = ""
    for i in dir[0:-2]:
        path += f"{i}/"
    path += filepath[2:]
    return path
