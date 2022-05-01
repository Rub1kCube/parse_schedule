from database.models import conn
from sheet.config import ConfigurationSheet
from sheet.sheet import Sheet
from database import models

from constants import PATH_FOR_DOWNLOAD, NAME_FILE_XLSX


def main():

    file_name = f'{PATH_FOR_DOWNLOAD}/{NAME_FILE_XLSX}.xlsx'
    conf_schedule = ConfigurationSheet(file_name)
    for name in conf_schedule.sheet_names:
        sheet = Sheet(conf_schedule, name)
        subjects = sheet.parse_sheet()
        for subject in subjects:
            insert_subject = models.table_subject.insert().values(**subject)
            conn.execute(insert_subject)


if __name__ == '__main__':
    main()
