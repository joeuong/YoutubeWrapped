# Hi Everyone! :) 

def itunesAPI():
    from calendar import month
    import json
    import os
    import re
    import sqlite3
    import requests
    import datetime
    import time
    import random

    use_dir = os.getcwd()

# Update with your filepath:
# MacOS Path    
    path = os.path.join(use_dir, '/Users/josephuong/Dropbox/Desktop Python/YT Wrapped/2022/2022-11-23_watch-history.json') 

# Load data to python
    with open(path, 'r') as df:                                                        
        obj = json.loads(df.read())

# Establish SQLite connection to local database file
    con = sqlite3.connect('/Users/josephuong/Library/CloudStorage/Dropbox/Home-VSCode/Apps/YT Wrapped/SQL/music_data.db')
    cur = con.cursor()

# Find a random number between 0 and 5000
    # r = random.randrange(5000)
    r = 20907

# FOR loop to clean titles, artist names, and call the iTunes API
    for i in range(r,r+10,1):
        # print('+---+')
# Update the ['time']'s [0:4] if you want to limit to a specific month 
# Ex: obj[i]['time'][0:4] >= '2022-08' is anything starting Aug 1, 2022
        if obj[i]['header'] == 'YouTube Music' and obj[i]['time'][0:4] >= '2020':
            try:
                title_url = obj[i]['titleUrl']
                d = re.search(r'\?(.*)', title_url).group(1)
            except:
                print('Pass')
                pass
            a = str(obj[i]['title'][8:])
            a = a.replace(',','')
            a = a.replace('\'','')
            b = 'no artist'
            c = obj[i]['time'][0:10]
            try: 
                b = obj[i]['subtitles'][0]['name']
                b = b.replace(' - Topic','')
                b = b.replace(',',' ')
                b = b.replace('\'','')                
            except KeyError:
                continue
            ret = cur.execute(f"SELECT * FROM music_info where song_url = '{d}'")
            if ret.fetchone() == None:
                track = '\"' + a + '\"' + '+' + '\"' + b + '\"'
                print(track)
                url = f"https://itunes.apple.com/search?term={track}&entity=song&limit=1"
                try:
                    response = requests.get(url)
                    parsed = json.loads(response.content)
                    print(parsed)
                    song = (parsed['results'][0]['trackName'])
                    # print('song parsed')
                    song = song.replace('\'','')
                    # print(song)
                    artist = (parsed['results'][0]['artistName'])
                    # print('artist parsed')
                    artist = artist.replace('\'','')
                    # print(artist)
                    album = (parsed['results'][0]['collectionName'])
                    album = album.replace('\'','')                    
                    # print('album parsed')
                    # print(album)
                    timems = int(parsed['results'][0]['trackTimeMillis'])
                    # print('time parsed')
                    # print(timems)
                    timems = str(datetime.timedelta(milliseconds=timems))
                    # print('time divided')
                    # print(timems)
                    trackid = (parsed['results'][0]['trackId'])
                    # print('trackid parsed')
                    # print(trackid)
                    sql = f"INSERT INTO music_info (song_url,song_title,song_length,song_artist,song_album,itunes_id,g_title,g_artist) VALUES ('{d}','{song}','{timems}','{artist}','{album}','{trackid}','{a}','{b}')"
                    print(sql)
                    cur.execute(sql)
                    con.commit()
                    print(str(i) + '- ' + a + ' by ' + b + ' added')
                    time.sleep(3)
                except:
                    print(str(i) + '- no api response/results')
                    continue
            else:
                print(str(i) + '- Already in database')
                continue
# Must commit the SQL statement for it to update the database
        else:
            print(str(i) + '- Not YT Music')
            continue
    tot = cur.execute(f"Select Count(*) from music_info")
    print(tot.fetchone())

if __name__ == '__main__':
    itunesAPI()