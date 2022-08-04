# YouTube Music Stats
# We can't let the Spotify users have all the fun! 

Music Stats from YouTube Music data via Google Takeout

Download YoutubeWrapped.py (and main.py if you want) 

No exteral libraries are needed for this to run

## 1. Grab Youtube Music data via Google Takeout in JSON format
https://takeout.google.com/settings/takeout
- Click "Deselct All"
- Scroll to the bottom
- Click the checkbox next to "YouTube and YouTube Music"
- Click "Multiple Formats"
- Change "History" to "JSON" and Click "OK"
- (optional) Click "All YouTube Data Included" and select only History
- Click "Next Step"
- Click "Create Export"
- You will receive an email when the export is ready

## 2. Once downloaded, place the "watch-history.json" somewhere and copy the filepath

## 3. Update the .py code included here with that filepath (Comments indicate location)

### Note: 
iTunes API is inconsistent. Code is available, but not maintained by me at this time. 
