from database.models import Subject
from database.connection import session
from sheet.config import ConfigurationSheet
from sheet.sheet import Sheet

from constants import PATH_FOR_DOWNLOAD, NAME_FILE_XLSX


def main():

    file_name = f'{PATH_FOR_DOWNLOAD}/{NAME_FILE_XLSX}.xlsx'
    conf_schedule = ConfigurationSheet(file_name)

    subject_list = []

    for name in conf_schedule.sheet_names:
        sheet = Sheet(conf_schedule, name)
        subjects = sheet.parse_sheet()
        for subject in subjects:
            subject_list.append(Subject(**subject))

    session.bulk_save_objects(subject_list)
    session.commit()


if __name__ == '__main__':
    main()
