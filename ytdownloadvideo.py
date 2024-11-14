# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 21:12:58 2022

@author: Samed
"""

from pytube import YouTube

link = input("Link: ")

yt = YouTube(link)
ys = yt.streams.get_highest_resolution()

print("indiriliyor...")
ys.download()
print("indirildi!")
