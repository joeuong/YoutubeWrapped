def SongHistory():
    import json
    import os
    import csv
    import datetime
    import csv
    import requests

    use_dir = os.getcwd()
    path = os.path.join(use_dir, 'watch-history.json')                      #default json file from Google

    with open(path, 'r') as df:                                                               #Load data to python 
        obj = json.loads(df.read())

    #returnlist = []
    artistlist = []
    songlist = []
    #abcde order: ['songtitle','artist','date','month','hour']
    
    for i in range(len(obj)):
        if obj[i]['header'] == 'YouTube Music' and obj[i]['time'][0:4] == '2022':
            a = obj[i]['title'][8:]                                                                 #cleaning titles and artist names
            a = a.replace(',',' ')
            b = 'no artist'
            c = obj[i]['time'][0:10]
            d = obj[i]['time'][5:7]
            e = obj[i]['time'][11:13]
            try:
                b = obj[i]['subtitles'][0]['name']
                b = b.replace(' - Topic','')
                b = b.replace(',',' ')
            except KeyError:
                continue
            songlist.append(a)
            artistlist.append(b)

    # dictionary for the index of each track. Key is URL, Value is Index
    urllist = {}

    #dictionaries for final info from API. Key is Index from URLLIST, Value is info 
    songdict = {}
    artistdict = {}
    albumdict = {}
    timedict = {}

    # Test artists/songs
    # artistlist = ['illenium','illenium','we the kings','justin bieber','taylor swift']
    # songlist = ['beautiful creatures','beautiful creatures','check yes juliet','what do you mean','22']

    # Main FOR loop
    for i in range(len(artistlist)):

        # replace spaces with + for URL
        artist = artistlist[i]
        artist = artist.replace(' ','+')
        song = songlist[i]
        song = song.replace(' ', '+')

        # Adds in "" for enhanced search capability
        track = '\"' + song + '\"' + '+' + '\"' + artist + '\"'
        url = f"https://itunes.apple.com/search?term={track}&entity=song&limit=1"

        # If the URL has already been sent to iTunes, then just grab the indexed info already passed
        # Prevents duplicates from being sent to the API, but allows for each instance of the song to be counted
        # in case you want to sum up the play time
        if url in urllist:
            urlindex = urllist[url]
            songdict[i] = songdict[urlindex]
            artistdict[i] = artistdict[urlindex]
            albumdict[i] = albumdict[urlindex] 
            timedict[i] = timedict[urlindex] 

        # If the URL HASN'T been passed to the API yet, then try sending it.
        # I got some Response 403 when sending a bunch, but got all 100 that I sent a few minutes later..., so who knows
        else:
            urllist[url] = i
            try:
                response = requests.get(url)
                parsed = json.loads(response.content)
                #print(response)
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

    # Prepare output file
    use_dir = os.getcwd()
    tar_path = os.path.join(use_dir, 'outfile.csv')

    with open(tar_path,'w', newline ='') as outfile:
        music = csv.writer(outfile, delimiter=',')
        music.writerow(['songtitle','artist','album','duration'])
        for z in range(len(urllist)):
            a = songdict[z]
            b = artistdict[z]
            c = albumdict[z]
            d = timedict[z]
            music.writerow([a,b,c,d])

if __name__ == '__main__':
    SongHistory()
