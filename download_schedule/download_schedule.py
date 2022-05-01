from google_drive_downloader import GoogleDriveDownloader as gdd
import requests
import bs4


def get_file_id():

    url = 'https://kcpt72.ru/schedule/'
    page = requests.get(url)

    soup = bs4.BeautifulSoup(page.text, 'lxml')
    a = soup.find_all('div', class_='d-flex flex-column sheulde-content')

    for af in a:
        b = af.find_all('a', href=True)


def download_files(*file_id) -> None:
    gdd.download_file_from_google_drive(file_id='1JIFYzzY_7RUjrmWvu7DjnhxDRkZ8UEnS',
                                    dest_path='./data/schedule.xlsx')


if __name__ == '__main__':
    get_file_id()