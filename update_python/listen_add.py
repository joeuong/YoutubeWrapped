# Hi Everyone! :) 
# Adds 3 months' worth of listen history 

def listen(path, beg_date,end_date):
    from calendar import month
    import json
    import os
    import re
    import sqlite3

# Load data to python
    with open(path, 'r') as df:                                                        
        obj = json.loads(df.read())

# Establish SQLite connection to local database file
    con = sqlite3.connect('/Users/josephuong/Library/CloudStorage/Dropbox/Home-VSCode/Apps/YT Wrapped/SQL/music_data.db')
    cur = con.cursor()

# cleaning titles and artist names
    for i in range(len(obj)):
# Update the ['time']'s [0:4] if you want to limit to a specific month 
# Ex: obj[i]['time'][0:4] >= '2022-08' is anything starting Aug 1, 2022
        if obj[i]['header'] == 'YouTube Music' and obj[i]['time'][0:7] >= beg_date and obj[i]['time'][0:7] <= end_date:
            try:
                title_url = obj[i]['titleUrl']
                d = re.search(r'\?(.*)', title_url).group(1)
            except:
                d = 'asdfcnyusasrvrbsdlfghs'
            a = str(obj[i]['title'][8:])
            a = a.replace(',',' ')
            b = 'no artist'
            c = obj[i]['time'][0:10]    # Full Date string
            try: 
                b = obj[i]['subtitles'][0]['name']
                b = b.replace(' - Topic','')
                b = b.replace(',',' ')
            except KeyError:
                continue
            try:
                cur.execute(f"INSERT INTO LISTEN_HISTORY (SONG_URL,LISTEN_DATE) VALUES ('{d}','{c}')")
            except:
                continue

# Must commit the SQL statement for it to update the database
    con.commit()

if __name__ == '__main__':
    listen()