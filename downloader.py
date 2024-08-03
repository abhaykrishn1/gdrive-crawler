import os
import requests
from config import DOWNLOAD_FOLDER

def download_file(file_id, file_name):
    url = f"https://drive.google.com/uc?id={file_id}"
    response = requests.get(url, allow_redirects=True)
    if response.status_code == 200:
        with open(os.path.join(DOWNLOAD_FOLDER, file_name), 'wb') as f:
            f.write(response.content)
        return True
    return False