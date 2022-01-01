import json
import os
import csv

use_dir = os.getcwd()
path = os.path.join(use_dir, 'watch-history.json')
tar_path = os.path.join(use_dir, '2021YTWrapped.csv')

print(tar_path)

with open(path, 'r') as df:
    obj = json.loads(df.read())

print(obj[0])
##
##with open(tar_path,'w', newline ='') as outfile:
##    music = csv.writer(outfile, delimiter='^')
##    music.writerow(['songtitle','date','artist','month','hour'])
##    for i in range(len(obj)):
##        if obj[i]['header'] == 'YouTube Music' and obj[i]['time'][0:4] == '2021':        
##            a = obj[i]['title'][8:]
##            a = a.replace(',',' ')
##            b = obj[i]['time'][0:10]
##            c = 'no artist'
##            d = obj[i]['time'][5:7]
##            e = obj[i]['time'][11:13]
##            try: 
##                c = obj[i]['subtitles'][0]['name']
##                c = c.replace(' - Topic','')
##                c = c.replace(',',' ')
##            except KeyError:
##                continue
##            music.writerow([a,b,c,d,e])
