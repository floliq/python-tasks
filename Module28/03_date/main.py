class Date:
    """
    Класс даты

    Args:
        day(int) - день недели
        month(int) - месяц
        year(int) - год
    """

    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        '''
        Функция вывода даты

        :return: дата
        :rtype: str
        '''

        return 'День: {}\tМесяц: {}\tГод: {}'.format(
            self.day,
            self.month,
            self.year
        )

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        '''
        Классовый метод проверки корректности даты

        :return: коректна дата или нет
        :rtype: bool
        '''

        day, month, year = map(int, date.split('-'))
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999
    
    @classmethod
    def from_string(cls, date: str) -> 'Date':
        '''
        Классовый метод перевода строки с датой в объект

        :return: date_obj
        :rtype: 'Date'
        '''

        day, month, year = map(int, date.split('-'))
        date_obj = cls(day, month, year)
        return date_obj


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
