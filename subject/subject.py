from constants import CALL_SCHEDULE_ON_WEEKDAYS, CALL_SCHEDULE_ON_WEEKEND
import datetime


class Subject:

    def __init__(self, number_subject: int, date_subject: str, group: str, empty_token: str = '-',
                 title_subjects: list = None, name_teachers: list = None, number_cabinets: list = None,
                 empty_subject: bool = False):

        self.number_subject = number_subject
        self.empty_subject = empty_subject
        self.empty_token = empty_token
        self.date_subject = date_subject
        self.time_start, self.time_end = self.__time_weekday()
        self.group = group

        if empty_subject and empty_token is None:
            raise ValueError('Wrong set of arguments')

        self.title_subjects = title_subjects
        self.name_teachers = name_teachers
        self.number_cabinets = number_cabinets

    def __time_weekday(self):
        date = tuple(map(lambda n: int(n), self.date_subject.split('-')[::-1]))
        weekday = datetime.datetime(*date).weekday()
        if weekday in (0, 1, 2, 3, 4):
            time = CALL_SCHEDULE_ON_WEEKDAYS[self.number_subject].split('-')
            time_start = time[0]
            time_end = time[1]
            return time_start, time_end
        else:
            time = CALL_SCHEDULE_ON_WEEKEND[self.number_subject].split('-')
            time_start = time[0]
            time_end = time[1]
            return time_start, time_end

    def __str__(self):
        return f'{self.number_subject}, {self.title_subjects}'

    def get_dict_format(self) -> dict:
        subject = {'number_cabinet': self.number_cabinets,
                   'title_subject': self.title_subjects,
                   'name_teacher': self.name_teachers,
                   'group_faculty': self.group,
                   'number_subject': self.number_subject,
                   'date_subject': self.date_subject,
                   'time_start': self.time_start,
                   'time_end': self.time_end}
        return subject

    def __repr__(self):
        if self.empty_subject:
            return repr(f'{self.number_subject}, {self.time_start}')
        else:
            return repr(f'{self.number_subject}, {self.title_subjects}, {self.name_teachers}, {self.number_cabinets}'
                        f' {self.time_start}, {self.group}')
