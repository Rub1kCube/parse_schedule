from database.models import conn
from sheet.config import ConfigurationSheet
from sheet.sheet import Sheet
from database import models


def main():

    file_name = 'src/schedule_1.xlsx'
    conf_schedule = ConfigurationSheet(file_name)
    for name in conf_schedule.sheet_names:
        sheet = Sheet(conf_schedule, name)
        subjects = sheet.parse_sheet()
        for subject in subjects:
            insert_subject = models.table_subject.insert().values(**subject)
            conn.execute(insert_subject)


if __name__ == '__main__':
    main()
