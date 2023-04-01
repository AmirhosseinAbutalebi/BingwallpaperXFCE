#!/usr/bin/python3

import json, os, urllib.request
from urllib.request import urlopen


BingURL = 'https://www.bing.com' # base url 
URL = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-Us'
# url for get information of image

pageData = json.loads(urlopen(URL).read().decode("utf-8")) # get information of image

imageDate = pageData['images'] # just get information image 
link = imageDate[0]['url'] # get url 
name = imageDate[0]['copyright'].split(" (")[0] # get name of image
name = name + ".jpg" # add extention

outputdirectory = "~/Pictures/" # directory of save image
output = outputdirectory + name # prepare of directory

urllib.request.urlretrieve(BingURL + link, output) # download image
