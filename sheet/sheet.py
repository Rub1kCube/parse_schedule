import re

from sheet.config import ConfigurationSheet
from subject.subject import Subject
from subject.position import SubjectPosition
import constants as const


class Sheet:

    def __init__(self, wb: ConfigurationSheet, sheet_name: str,):
        self.ws = wb.wb[sheet_name]
        self.sheet_name = sheet_name

    def __get_list_cell(self) -> list:
        """"""
        list_cell = []

        for row in self.ws.values:
            for cell in row:
                list_cell.append(cell)

        return list_cell

    def __get_groups(self) -> list:
        """ Поиск групп в таблице """
        groups = []
        for row in self.ws.values:
            for cell in row:
                groups = re.findall(r'\w{2,10}\s?\d{2}-\d{2}-?\d?', cell) if cell is not None else []
                if len(groups) != 0:
                    return groups
        if not groups:
            assert Exception('Не корректная страница')

    def __search_date_list(self) -> list:
        """ Поиск даты занятий в таблице """
        search_date = re.compile(r'\d{2}(-|.|/)\d{2}(-|.|/)\d{4}$')
        date_schedule = [date_value for date_value in self.__get_list_cell()
                         if type(date_value) is str and re.search(search_date, date_value) is not None]
        date_schedule = list(map(lambda x: re.search(search_date, x)[0].replace('.', '-'), date_schedule))
        return date_schedule

    def __start_increment(self) -> int:
        for row in range(1, self.ws.max_row):
            if self.ws[row][0].value == const.ITEM:
                return row
        return 0

    def __where_groups(self) -> list:
        """
        Функция для, определение ячейки по названию группы если она существует
        """
        list_position_group = []
        start_increment = self.__start_increment()
        for title_group in self.__get_groups():
            for title in range(1, self.ws.max_column, 2):
                data = self.ws[start_increment][title].value
                if data == title_group and not (data is None):
                    list_position_group.append(title + 1)
        return list_position_group

    def __count_subject_all_days(self) -> list:
        """ Функция для определения количества предметов во всех учебных днях """
        list_count_subject_in_day = []
        count = 0

        for subject in range(self.__start_increment() + 1, self.ws.max_row + 1):

            if type(self.ws.cell(row=subject, column=1).value) is int:
                count += 1
            elif self.ws.cell(row=subject, column=1).value == const.ITEM:
                list_count_subject_in_day.append(count)
                count = 0

            if subject == self.ws.max_row:
                list_count_subject_in_day.append(count)

        return list_count_subject_in_day

    def __range_cells(self) -> list:
        """ Функция для формирования коллекции из словарей с диапазоном клеток в одном предмете """
        count_cell = self.__start_increment()
        eq = False
        start_cell = 0
        list_size_subject = []

        date_in_sheet = self.__search_date_list()
        for index, count_subject in enumerate(self.__count_subject_all_days()):
            for number in range(1, count_subject + 1):
                for cell in range(count_cell, self.ws.max_row + 2):
                    if cell == self.ws.max_row:
                        finish_cell = cell
                        subject_position = SubjectPosition(start_cell, finish_cell - 1, number, date_in_sheet[index])
                        list_size_subject.append(subject_position)

                    elif self.ws.cell(row=cell, column=1).value is None:
                        continue

                    elif type(self.ws.cell(row=cell, column=1).value) is int and eq is False:
                        eq = True
                        start_cell = cell

                    elif eq:
                        finish_cell = cell
                        subject_position = SubjectPosition(start_cell, finish_cell - 1, number, date_in_sheet[index])
                        list_size_subject.append(subject_position)

                        eq = False
                        save_count_cell = cell
                        count_cell = save_count_cell
                        break

        return list_size_subject

    @staticmethod
    def __eq_teacher(line: str) -> bool:

        teacher_name = line.strip()
        if len(re.findall(r'\D\.', teacher_name)) == 2 and teacher_name[0].isupper:
            return True
        return False

    def parse_sheet(self) -> list:
        """
        Цикл для формирования коллекции из словарей с названием предмета,
        именем учителя, номером кабинета, номером предмета
        """
        position_groups = self.__where_groups()
        day_with_subjects = []
        for index, position_group in enumerate(position_groups):
            for subject in self.__range_cells():

                start = subject.start_cell
                finish = subject.finish_cell
                date = subject.start_date
                size_cell = finish - start + 1
                count_empty_cells = 0
                number_subject = subject.number_subject

                name_teachers = []
                number_cabinets = []
                title_subjects = []

                for number in range(start, finish + 1):
                    data = self.ws.cell(row=number, column=position_group).value
                    number_cabinet = self.ws.cell(row=number, column=position_group + 1).value

                    if data is None:
                        count_empty_cells += 1

                    else:

                        if not (number_cabinet is None):
                            number_cabinets.append(number_cabinet)

                        if not self.__eq_teacher(data):
                            title_subjects.append(data)

                        else:
                            name_teachers.append(data)

                if count_empty_cells == size_cell:
                    subject = Subject(number_subject, empty_subject=True,
                                      date_subject=date, group=self.__get_groups()[index])
                    day_with_subjects.append(subject.get_dict_format())

                else:
                    subject = Subject(number_subject, title_subjects=title_subjects, name_teachers=name_teachers,
                                      number_cabinets=number_cabinets,
                                      date_subject=date, group=self.__get_groups()[index])
                    day_with_subjects.append(subject.get_dict_format())

        return day_with_subjects
