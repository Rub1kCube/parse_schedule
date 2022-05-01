from google_drive_downloader import GoogleDriveDownloader as Downloader
import requests
import bs4
import datetime
import re

from constants import URL_FOR_DOWNLOAD_FILE, PATH_FOR_DOWNLOAD, NAME_FILE_DOCX, NAME_FILE_XLSX


def get_file_id() -> dict:

    url = URL_FOR_DOWNLOAD_FILE
    page = requests.get(url)

    soup = bs4.BeautifulSoup(page.text, 'lxml')
    page_schedule = soup.find_all('div', class_='d-flex flex-column sheulde-content')[0]
    block_schedule_files = page_schedule.find_all('a', href=True)[1:]
    id_files = [re.search(r'/d/\w+/', file['href'])[0][3:-1] for file in block_schedule_files]

    return {
        NAME_FILE_XLSX: (id_files[0], 'xlsx'),
        NAME_FILE_DOCX: (id_files[1], 'docx'),
    }


def download_files(**file_id) -> None:

    for key, file in file_id.items():
        Downloader.download_file_from_google_drive(file_id=file[0],
                                                   dest_path=f'../{PATH_FOR_DOWNLOAD}/{key + "." + file[1]}')


if __name__ == '__main__':
    download_files(**get_file_id())
