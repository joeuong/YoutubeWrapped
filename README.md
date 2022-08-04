# musicstats
Music Stats from iTunes API and YouTube Music data

1. Grab Youtube Music stats from Google Takeout in JSON
## https://takeout.google.com/settings/takeout
### Click DESELECT ALL
###	Scroll to the bottom
### Click the checkbox next to "YouTube and YouTube Music"
### Click "Multiple Formats"
### Change "History" to "JSON" and Click "OK"

2. Run code to compile YT data into lists to call iTunes API for other stats on music
3. Returns CSV file "outfile" with data such as song title, artist, album, and run-time
