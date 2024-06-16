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

# FOR loop to clean titles, artist names, and call the iTunes API
    for i in range(len(obj)):
# Update the ['time']'s [0:4] if you want to limit to a specific month 
# Ex: obj[i]['time'][0:4] >= '2022-08' is anything starting Aug 1, 2022
        if obj[i]['header'] == 'YouTube Music' and obj[i]['time'][0:4] == '2019':
            try:
                title_url = obj[i]['titleUrl']
                d = re.search(r'\?(.*)', title_url).group(1)
            except:
                print(obj[i])
                pass
            a = str(obj[i]['title'][8:])
            a = a.replace(',',' ')
            b = 'no artist'
            c = obj[i]['time'][0:10]
            try: 
                b = obj[i]['subtitles'][0]['name']
                b = b.replace(' - Topic','')
                b = b.replace(',',' ')
            except KeyError:
                continue
            cur.execute(f"INSERT INTO id_tracker (song_url,json_id) VALUES ('{d}','{str(i)}')")
            con.commit()
# Must commit the SQL statement for it to update the database
        else:
            continue

if __name__ == '__main__':
    itunesAPI()