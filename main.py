import utils
from IPython.display import Image, clear_output  # to display images

clear_output()
import os
import matplotlib.pyplot as plt
import shutil
import json
import numpy as np
import io
from PIL import Image
import cv2
import numpy as np
from tqdm import tqdm_notebook
from moviepy.editor import *
from base64 import b64encode
from train import main

# Определим количество классов из yaml файла
import yaml

num_classes = 1

# Для записи шаблонов в файл определим библиотеку
from IPython.core.magic import register_line_cell_magic

def writetemplate(line, cell):
    with open(line, 'w') as f:
        f.write(cell.format(**globals()))

    # --local_rank
os.system(
    "python train.py --img 512 --batch 16 --epochs 500 --data content/data.yaml --cfg ./models/yolov5m.yaml --weights '' --name yolov5m_results --cache --patience 100")



# os.system(
#     "python detect.py --weights yolov5l_results/weights/best.pt --img 512 --conf 0.25 --source content/data/valid/images --hide-labels")
