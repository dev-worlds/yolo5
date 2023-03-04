import os
import re

path = 'Фото/'

for (i, img_path) in enumerate(os.listdir(path)):
    name, ext = os.path.splitext(img_path)
    new_name = re.sub("[\s][а-яА-Я]+[\s][а-яА-Я]+", '', name)
    os.rename(f'{path}{img_path}', f'{path}{new_name}{ext}')
