from authentication import authenticate_drive
from downloader import download_file
from config import DRIVE_FOLDER_ID

def list_files(service, folder_id):
    results = service.files().list(q=f"'{folder_id}' in parents", fields="nextPageToken, files(id, name)").execute()
    return results.get('files', [])

def main():
    service = authenticate_drive()
    
    downloaded_files = []
    pending_files = []

    files = list_files(service, DRIVE_FOLDER_ID)

    for file in files:
        if file['name'].endswith(('.mp4', '.avi', '.mov')):
            print(f"Downloading {file['name']}...")
            if download_file(file['id'], file['name']):
                downloaded_files.append(file['name'])
            else:
                pending_files.append(file['name'])

    with open('downloaded_files.txt', 'w') as df:
        df.write('\n'.join(downloaded_files))

    with open('pending_files.txt', 'w') as pf:
        pf.write('\n'.join(pending_files))

if __name__ == '__main__':
    main()