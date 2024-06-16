# Hi Everyone! :) 

def YtMusicCsvConvert():
    from calendar import month
    import json
    import os
    from collections import Counter
    import csv

    use_dir = os.getcwd()

# Update with your filepath:
# MacOS Path    
    path = os.path.join(use_dir, '/Users/josephuong/Library/CloudStorage/Dropbox/Home-VSCode/Apps/YT Wrapped/2024/2024-03-30_watch-history.json') 

# Windows Path
    # path = r'C:\Users\juong42\Dropbox (Personal)\Desktop Python\YT Wrapped\2022\2022-11-23_watch-history.json'

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

    time_frame = '2024-01'

# cleaning titles and artist names
    for i in range(len(obj)):
# Update the ['time']'s [0:4] if you want to limit to a specific month 
# Ex: obj[i]['time'][0:4] >= '2022-08' is anything starting Aug 1, 2022
        if obj[i]['header'] == 'YouTube Music' and obj[i]['time'][0:7] >= time_frame:
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

# Define variables for each of the counts
    artistcount = Counter(artists).most_common(20)
    trackcount = Counter(tracks).most_common(20)
    artisttop = Counter(artists).most_common(15)
    monthcount = Counter(months).most_common(12)
    datescount = Counter(dates).most_common(10)
    # hourscount = Counter(hours).most_common(24)

# Option to print to Terminal
# Printing Top Stats for the year
    print(f'\nTop Artists of {time_frame}: ')
    for i in range(len(artistcount)):
        print(*artistcount[i], sep=', ')

    print(f'\nTop Tracks of {time_frame}: ')
    for i in range(len(trackcount)):
        print(i+1, *trackcount[i], sep=', ')

#Printing Top Songs for each of the Top Artists identified
    print(f'\nTop Songs for Top Artists:')
    for i in range(len(artisttop)):
        art = artisttop[i][0]
        print(f'\nTop songs for {art}: ')
        t = str(f'// {art}')
        matching = [s.split('//')[0] for s in tracks if t in s]
        matchingcount = Counter(matching).most_common(10)
        for j in range(len(matchingcount)):
            print(*matchingcount[j], sep='- ')

    print(f'\n*WORKING*Top Songs for each Month:')
# Identify top 3 songs or artists for each month
    for month_num in range(1, 13):  # Iterate through each month
        month_str = f'{year}-{month_num:02d}'  # Convert month number to string, e.g., '2023-01'
        print(f'\nTop 3 Songs for {month_str}:')
# Filter tracks for the current month
        monthly_tracks = [track for track, date in zip(tracks, dates) if date.startswith(month_str)]
# Get count of each track in the current month
        monthly_trackcount = Counter(monthly_tracks).most_common(3)
        for i, (track, count) in enumerate(monthly_trackcount):
            print(f'{i + 1}. {track} - {count} plays')

    print(f'\nTop Months: ')
    for i in range(len(monthcount)):
        print(*monthcount[i], sep=', ')

    print(f'\nTop Dates: ')
    for i in range(len(datescount)):
        print(*datescount[i], sep=', ')


    print(f'\nTop Months: ')
    for i in range(len(monthcount)):
        print(*monthcount[i], sep=', ')
        
    print(f'\nTop Dates: ')
    for i in range(len(datescount)):
        print(*datescount[i], sep=', ')

# Option to print to CSV
    tar_path = rf'/Users/josephuong/Library/CloudStorage/Dropbox/Home-VSCode/Apps/YT Wrapped/{time_frame}_outfile.csv'
    with open(tar_path,'w', newline ='') as outfile:
        music = csv.writer(outfile, delimiter=',')
        for i in range(len(tracks)):
            music.writerow([songs[i],artists[i],dates[i]])
            # music.writerow(trackcount[i])
    
# Option to see Total Count
    # a=0
    # for i in range(len(monthcount)):
    #    a += int(monthcount[i][1])
    # print('\n','Total Count: ',a)

if __name__ == '__main__':
    YtMusicCsvConvert()