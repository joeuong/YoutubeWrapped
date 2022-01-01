def YtMusicCsvConvert():
    import json
    import os
    import csv

    use_dir = os.getcwd()
    path = os.path.join(use_dir, 'watch-history.json')               #default json file from Google
    tar_path = os.path.join(use_dir, '2021YTWrapped_1.csv')   #name file whatever you would like

    with open(path, 'r') as df:                                                        #Load data to python 
        obj = json.loads(df.read())

    with open(tar_path,'w', newline ='') as outfile:
        music = csv.writer(outfile, delimiter='^')                          #lots of commas in artist names, so I used a character that I didn't see ^
        music.writerow(['songtitle','date','artist','month','hour'])
        for i in range(len(obj)):
            if obj[i]['header'] == 'YouTube Music' and obj[i]['time'][0:4] == '2021':        
                a = obj[i]['title'][8:]                                                      #cleaning titles and artist names
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
                music.writerow([a,b,c,d,e])                                         #write to CSV

if __name__ == '__main__':
    YtMusicCsvConvert()
