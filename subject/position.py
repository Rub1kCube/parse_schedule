class SubjectPosition:

    def __init__(self, start, finish, number_subject, start_date: str):
        self.start_cell = start
        self.finish_cell = finish
        self.number_subject = number_subject
        self.start_date = start_date

    def __str__(self):
        return str(f'start: {self.start_cell},\n finish: {self.finish_cell},\n '
                   f'number_subject: {self.number_subject}, start_date: {self.start_date}')

    def __repr__(self):
        return repr((self.start_cell, self.finish_cell, self.number_subject, self.start_date))
