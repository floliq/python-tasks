class Stack:
    """
    Класс стека

    Attributes:
        st(list) - список элементов в стеке
    """

    def __init__(self):
        self.__st = []

    def __str__(self):
        """
        Функция вывода стека
        
        :return: '; '.join(self.__st)
        :rtype: str
        """
        return '; '.join(self.__st)

    def push(self, elem):
        """
        Функция добавления в стек

        :param elem: элемент добавляемый в стек
        :type elem: any
        """
        self.__st.append(elem)

    def pop(self):
        """
        Функция удаления из стека последнего элемента
        """
        if len(self.__st) == 0:
            return None
        else:
            self.__st.pop()


class TaskManager:
    """
    Класс менеджера задач

    Attributes:
        task(dict) - словарь задач
    """

    def __init__(self):
        self.task = dict()

    def __str__(self):
        """
        Функция вывода задач

        :return: ''.join(display)
        :rtype: str
        """
        display = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append('{} {}\n'.format(str(i_priority), self.task[i_priority]))
        return ''.join(display)

    def new_task(self, task, priorety):
        """
        Функция добавления новой задачи

        :param task: название задачи
        :type task: str
        :param priorety: приоритет
        :type priorety: int
        """
        if priorety not in self.task:
            self.task[priorety] = Stack()
        self.task[priorety].push(task)

manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)