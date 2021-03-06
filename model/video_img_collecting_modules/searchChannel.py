# -*- coding: utf-8 -*-
"""Collecting Data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HzLOThQz9PFlvIhAjyCq_jXHcTEBrwtM
"""

import pandas as pd
import numpy as np

import requests

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client .tools import argparser

import json
import urllib

class Search_ChannelID:
  def __init__(self, username):
    self.username = username

  def channel_id(self, YOUTUBE_API_SERVICE_NAME = "youtube", YOUTUBE_API_VERSION = "v3", DEVELOPER_KEY):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.channels().list(part="id",
                                            forUsername = str(self.username),
                                            maxResults=1
                                            ).execute()

    channelID = {}

    search_result = search_response.get("items", [])[0]
    if search_result["kind"] == "youtube#channel":
      channelID[self.username] = search_result["id"]
    else:
      return "No exists channel"

    return channelID

class Channel:
  def __init__(self, channelID):
    self.channelID = channelID

  def youtube_search(self,YOUTUBE_API_SERVICE_NAME = "youtube", YOUTUBE_API_VERSION = "v3", DEVELOPER_KEY,  maximum):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(part="id, snippet",
                                            channelId = str(self.channelID),
                                            maxResults=maximum
                                            ).execute()

    videos = {}
    channels = {}
    playlists = {}

   
    for search_result in search_response.get("items", []):
      if search_result["id"]["kind"] == "youtube#video":
        videos[search_result["snippet"]["title"]] = search_result["id"]["videoId"]
      elif search_result["id"]["kind"] == "youtube#channel":
        channels[search_result["snippet"]["title"]] = search_result["id"]["channelId"]
      elif search_result["id"]["kind"] == "youtube#playlist":
        playlists[search_result["snippet"]["title"]] = search_result["id"]["playlistId"]

    return videos, channels, playlists



