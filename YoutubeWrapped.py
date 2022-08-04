# Hi Everyone! :) 

def YtMusicCsvConvert():
    from calendar import month
    import json
    import os
    from collections import Counter
    import csv

    use_dir = os.getcwd()

# Update with your filepath:
    path = os.path.join(use_dir, 'watch-history.json') 

#Load data to python
    with open(path, 'r') as df:                                                        
        obj = json.loads(df.read())

#lists for info
    songs = []
    artists = []
    tracks = []
    dates = []
    months = []
    # hours = []

# cleaning titles and artist names
    for i in range(len(obj)):
# Update the ['time']'s [0:4] if you want to limit to a specific month 
# Ex: obj[i]['time'][0:4] >= '2022-08' is anything starting Aug 1, 2022
        if obj[i]['header'] == 'YouTube Music' and obj[i]['time'][0:4] == '2022':
            year = obj[i]['time'][0:4]
            a = obj[i]['title'][8:]
            a = a.replace(',',' ')
            b = 'no artist'
            c = obj[i]['time'][0:10]
            d = obj[i]['time'][5:7]
            # e = obj[i]['time'][11:13]
            try: 
                b = obj[i]['subtitles'][0]['name']
                b = b.replace(' - Topic','')
                b = b.replace(',',' ')
            except KeyError:
                continue
            songs.append(a)
            artists.append(b)
            to_track = a + ' // ' + b
            tracks.append(to_track)
            dates.append(c)
            months.append(d)
            # hours.append(e)

# Edit numbers for different counts
    artistcount = Counter(artists).most_common(20)
    trackcount = Counter(tracks).most_common(20)
    monthcount = Counter(months).most_common(12)
    datescount = Counter(dates).most_common(10)
    
# Option to print to Terminal
    print(f'\nTop Artists of {year}: ')
    for i in range(len(artistcount)):
        print(*artistcount[i], sep=', ')

    print(f'\nTop Tracks of {year}: ')
    for i in range(len(trackcount)):
        print(*trackcount[i], sep=', ')

    print(f'\nTop Months: ')
    for i in range(len(monthcount)):
        print(*monthcount[i], sep=', ')

    print(f'\nTop Dates: ')
    for i in range(len(datescount)):
        print(*datescount[i], sep=', ')

# Option to print to CSV
    # tar_path = os.path.join(use_dir, 'outfile.csv')
    # with open(tar_path,'w', newline ='') as outfile:
    #     music = csv.writer(outfile, delimiter=',')
    #     for i in range(len(trackcount)):
    #         music.writerow(trackcount[i])
    
# Option to see Total Count
    # a=0
    # for i in range(len(monthcount)):
    #    a += int(monthcount[i][1])
    # print('\n','Total Count: ',a)

if __name__ == '__main__':
    YtMusicCsvConvert()
