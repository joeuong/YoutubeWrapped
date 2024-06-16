import os
import listen_add
import add_to_db_google_only 

use_dir = os.getcwd()
path = os.path.join(use_dir, '/Users/josephuong/Library/CloudStorage/Dropbox/Home-VSCode/Apps/YT Wrapped/json_data/2024/2024-03-30_watch-history.json') 
beg_date = '2024-04'
end_date = '2024-04'

listen_add.listen(path,beg_date,end_date)
add_to_db_google_only.itunesAPI(path,beg_date,end_date)