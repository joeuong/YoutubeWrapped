from YoutubeWrapped import YtMusicCsvConvert
from itunes_api_v2 import itunesApiFromInfo

YtMusicCsvConvert()

# Fixing in an later update:
    # You will need to update the CSV before uncommenting the next function call
    # Do a Text to Column for the (^) character then remove the results you don't want.
    # I had 6000 or so rows in my 2021 file, but only tested the iTunes API with up to 100 calls. 

# itunesApiFromInfo()
