# Hi Everyone! :) 
# Adds song information to music_data.db - music_info_google_only if it isn't already there

def itunesAPI(path,beg_date,end_date):
    from calendar import month
    import json
    import os
    import re
    import sqlite3
    import requests
    import datetime
    import time
    import random

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
        if obj[i]['header'] == 'YouTube Music' and obj[i]['time'][0:7] >= beg_date and obj[i]['time'][0:7] <= end_date:
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
            ret = cur.execute(f"SELECT * FROM MUSIC_INFO_GOOGLE_ONLY where SONG_URL = '{d}'")
            if ret.fetchone() == None:
                sql = f"INSERT INTO MUSIC_INFO_GOOGLE_ONLY (SONG_URL,G_TITLE,G_ARTIST) VALUES ('{d}','{a}','{b}')"
                print(sql)
                cur.execute(sql)
                con.commit()
                print(str(i) + '- ' + a + ' by ' + b + ' added')
            else:
                # print(str(i) + '- Already in database')
                continue
# Must commit the SQL statement for it to update the database
        else:
            # print(str(i) + '- Not YT Music')
            continue
    tot = cur.execute(f"Select Count(*) from MUSIC_INFO_GOOGLE_ONLY")
    print(tot.fetchone())

if __name__ == '__main__':
    itunesAPI()