# -*- coding: utf-8 -*-
"""Collecting Data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HzLOThQz9PFlvIhAjyCq_jXHcTEBrwtM
"""

"""## Video Download"""

pip install pytube3

pip install --upgrade pytube

from pytube import YouTube
import os
from os.path import join

class videoDownload:
  def __init__(self, videoID_dict):
    self.videoIDlist = videodict.values()

  def downloads(self, base_path, folder):
    path = join(base_path, folder)
    link1 = "https://www.youtube.com/watch?v="

    for id in self.videoIDlist:
      link = link1 + str(id)
      yt = YouTube(link)

      # downloads "mp4" & "webm" files
      ys = yt.streams.filter(only_video=True)

      for s in ys :
        try :
          s.download(path)  
        except :
          print(f"Where id {id} stream {s}")
