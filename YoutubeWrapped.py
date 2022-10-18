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
            year = obj[i]['time'][0:4]  # Year string
            a = obj[i]['title'][8:]
            a = a.replace(',',' ')
            b = 'no artist'
            c = obj[i]['time'][0:10]    # Full Date string
            d = obj[i]['time'][5:7]     # Month string
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
    artisttop = Counter(artists).most_common(10)
    trackcount = Counter(tracks).most_common(20)
    monthcount = Counter(months).most_common(12)
    datescount = Counter(dates).most_common(10)
    # hourscount = Counter(hours).most_common(24)

# Option to print to Terminal
# Printing Top Stats for the year
    print(f'\nTop Artists of {year}: ')
    for i in range(len(artistcount)):
        print(*artistcount[i], sep=', ')

    print(f'\nTop Tracks of {year}: ')
    for i in range(len(trackcount)):
        print(i+1, *trackcount[i], sep=', ')

#Printing Top Songs for each of the Top Artists identified
    print('Top Songs for Top Artists:')
    for i in range(len(artisttop)):
        art = artisttop[i][0]
        print(f'\nTop songs for {art}: ')
        t = str(f'// {art}')
        matching = [s.split('//')[0] for s in tracks if t in s]
        matchingcount = Counter(matching).most_common(10)
        for j in range(len(matchingcount)):
            print(*matchingcount[j], sep='- ')

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
    #     for i in range(len(tracks)):
    #         music.writerow([songs[i],artists[i],dates[i]])
    #         # music.writerow(trackcount[i])
    
# Option to see Total Count
    # a=0
    # for i in range(len(monthcount)):
    #    a += int(monthcount[i][1])
    # print('\n','Total Count: ',a)

if __name__ == '__main__':
    YtMusicCsvConvert()
