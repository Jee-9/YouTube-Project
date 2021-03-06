# -*- coding: utf-8 -*-
"""movefiles.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NZiEuQa1hZk04uzbh7REm4Odus5i-4_h
"""

import os
from os.path import join
import cv2
import glob

base_dir = "/content/drive/MyDrive"
im_dir = "project_share/imageData"
cur = "PROJECT"
folder = "education_images"
files = "*.jpg"
im_path = join(base_dir, im_dir, folder, files)
f_path = join(base_dir, cur)

"""여러 폴더로 나눠서 저장하기"""
# 실행 후 기존 데이터는 삭제 필요..

images = glob.glob(im_path)

def extractname(filepath):
  path_list = filepath.split("/")
  img_name = path_list[-1].split(".")[0]
  return img_name

def makedir(directory):
  if not os.path.exists(directory):
    os.mkdir(directory)

for i, p in enumerate(images):
  dir = join(base_dir, "PROJECT", str(ind))
  makedir(dir)

  im_n = extractname(p)
  ind = im_n.split("_")[0]
  save_path = join(dir, im_n.split("_")[1]+".jpg")
  im = cv2.imread(p)
  cv2.imwrite(save_path, im)


"""파일 옮겨서 저장하기"""
# 다시 하나의 파일로 합치기
# 실행 후 기존 데이터는 삭제필요..

def move_im(to_path,filelist):
  for f in filelist:
    image = cv2.imread(f)

    splited = f.split("/")
    to_name = splited[-2]+"_"+splited[-1]

    save_path = join(to_path, to_name)
    cv2.imwrite(save_path, image)

for i in range(47):
  folder_path = join(f_path, str(i))
  file_type = "*.jpg"
  to_path = join(base_dir, im_dir, folder)

  if os.path.exists(folder_path):
    filepath = join(folder_path, file_type)
    images = glob.glob(filepath)
    move_im(to_path, images)
  else:
    pass

