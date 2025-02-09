import os
import listen_add
import add_to_db_google_only 

use_dir = os.getcwd()
path = os.path.join(use_dir, '/Users/josephuong/Library/CloudStorage/Dropbox/Home-VSCode/Apps/YouTube_Wrapped/json_data/watch_history/2025-02-08_watch-history.json') 
beg_date = '2024-12'
end_date = '2025-01'

listen_add.listen(path,beg_date,end_date)
add_to_db_google_only.itunesAPI(path,beg_date,end_date)