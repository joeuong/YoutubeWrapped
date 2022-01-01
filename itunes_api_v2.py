import os
import requests
import json
import datetime
import csv

with open('Book1.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

artistlist = []
songlist = []

for k in range(len(data)):
    artistlist.append(data[k][1])
    songlist.append(data[k][0])

"""
Sample iTunes API URL
https://itunes.apple.com/search?term=jack+johnson&entity=musicVideo
"""

##artistlist = ['illenium','illenium','we the kings','justin bieber','taylor swift']
##songlist = ['beautiful creatures','beautiful creatures','check yes juliet','what do you mean','22']

songdict = {}
artistdict = {}
albumdict = {}
timedict = {}

urllist = {}
a = 0

for i in range(len(artistlist)):
    
    artist = artistlist[i]
    artist = artist.replace(' ','+')
    song = songlist[i]
    song = song.replace(' ', '+')

    track = '\"' + song + '\"' + '+' + '\"' + artist + '\"'
    url = f"https://itunes.apple.com/search?term={track}&entity=song&limit=1"

    if url in urllist:
        urlindex = urllist[url]
        songdict[i] = songdict[urlindex]
        artistdict[i] = artistdict[urlindex]
        albumdict[i] = albumdict[urlindex] 
        timedict[i] = timedict[urlindex] 
        
    else:
        urllist[url] = i
        try:
            response = requests.get(url)
            parsed = json.loads(response.content)
            print(response)
            songdict[i] = (parsed['results'][0]['trackName'])
            artistdict[i] = (parsed['results'][0]['artistName'])
            albumdict[i] = (parsed['results'][0]['collectionName'])
            timems = int(parsed['results'][0]['trackTimeMillis'])
            timedict[i] = str(datetime.timedelta(milliseconds=timems))

        except:
            songdict[i] = 'no response'
            artistdict[i] = 'no response'
            albumdict[i] = 'no response'
            timedict[i] = 'no response'


use_dir = os.getcwd()
tar_path = os.path.join(use_dir, 'outfile.csv')

with open(tar_path,'w', newline ='') as outfile:
    music = csv.writer(outfile, delimiter=',')
    music.writerow(['songtitle','artist','album','duration'])
    for z in range(99):
        a = songdict[z]
        b = artistdict[z]
        c = albumdict[z]
        d = timedict[z]
        music.writerow([a,b,c,d])

print(urllist)
print(songdict)
print(artistdict)
print(albumdict)
print(timedict)
