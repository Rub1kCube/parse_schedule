import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
HOST = os.environ.get('HOST')
NAME = os.getenv('NAME')
PASSWORD = os.getenv('PASSWORD')
USER = os.getenv('USER_DB')
PORT = os.getenv('PORT')
PATH_FOR_DOWNLOAD = os.getenv('PATH_FOR_DOWNLOAD')
NAME_FILE_XLSX = os.getenv('NAME_FILE_XLSX')
NAME_FILE_DOCX = os.getenv('NAME_FILE_DOCX')

ITEM = '№'
TOKEN_EMPTY = '-'
URL_FOR_DOWNLOAD_FILE = 'https://kcpt72.ru/schedule/'

CALL_SCHEDULE_ON_WEEKDAYS = {
    1: '8:15-9:00',
    2: '9:00-9:45',
    3: '9:55-10:40',
    4: '10:40-11:25',
    5: '11:40-12:25',
    6: '12:25-13:10',
    7: '13:30-14:15',
    8: '14:15-15:00',
    9: '15:15-16:00',
    10: '16:00-16:45',
    11: '16:55-17:40',
    12: '17:40-18:25',
}

CALL_SCHEDULE_ON_WEEKEND = {
    1: '8:15-9:00',
    2: '9:00-9:45',
    3: '9:50-10:35',
    4: '10:35-11:20',
    5: '11:35-12:20',
    6: '12:20-13:05',
    7: '13:20-14:05',
    8: '14:05-14:50',
    9: '15:05-15:50',
    10: '15:50-16:35',
    11: '16:40-17:25',
    12: '17:25-18:10',
}
