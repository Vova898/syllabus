class Discipline:
    '''Класс для хранения информации об одной дисциплине'''
    
    def __init__(self, name, start_semester, duration, total_hours, assessment_type, department):
        '''Конструктор класса Discipline'''

        self.name = name
        self.start_semester = int(start_semester)
        self.duration = int(duration)
        self.total_hours = int(total_hours)
        self.assessment_type = assessment_type
        self.department = department
    
    def __str__(self):
        '''Возвращает строковое представление дисциплины для вывода'''
        return f"{self.name:30} | {self.start_semester:2} | {self.duration:2} | {self.total_hours:4} | {self.assessment_type:10} | {self.department}"
    
    def to_file_string(self):
        '''Возвращает строковое представление дисциплины для записи в файл'''
        return f"{self.name};{self.start_semester};{self.duration};{self.total_hours};{self.assessment_type};{self.department}"


