from typing import Any, Optional, Iterable


class Node:
    """
    Класс узла

    Args:
        value(Optional[Any]) - значение узла
        next(Optional['Node']) - указатель на сл узел
    """
    
    def __init__(self, value: Optional[Any] = None, next: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next

    def __str__(self):
        """
        Функция получения значения узла

        :return: self.value
        :rtype: str
        """
        return 'Node: {}'.format(str(self.value))


class LinkedList:
    """
    Класс односвязного списка

    Attributes:
        head(Optional[Node]) - голова односвязного списка
        length(int) - длина списка
    """

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length = 0
    
    def __str__(self) -> str:
        """
        Функция получения односвязного списка

        :rtype: str
        """

        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return '[{}]'.format(' '.join(values))
        return 'LinkedList []'
    
    def get(self, index: int) -> Any:
        """
        Функция получения элемента односвязного списка по индексу

        :param index: индекс элемента односвязного списка
        :type index: int
        :return: current.value
        :rtype: Any
        """

        if self.length == 0 or index > self.length or index < 0:
            raise IndexError
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value
    
    def append(self, elem: Any) -> None:
        """
        Функция добавления элемента в односвязный список

        :param elem: элемент списка
        :type elem: Any
        """

        new_elem = Node(elem)
        if self.head is None:
            self.head = new_elem
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_elem
        self.length += 1
    
    def remove(self, index: int) -> None:
        """
        Функция удаления элемента из односвязного списка по индексу

        :param index: индекс элемента односвязного списка
        :type index: int
        """

        cur_node = self.head
        cur_index = 0
        if self.length == 0 or self.length <= index:
            raise IndexError
        if cur_node is not Node:
            if index == 0:
                self.head = cur_node.next
                self.length -= 1
                return
        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1
        prev.next = cur_node.next
        self.length -= 1
    
    def __iter__(self) -> Iterable:
        """
        Итератор списка

        :yield: Итератор для списка
        :rtype: Iterable
        """
        current = self.head
        while current is not None:
            yield current.value
            current = current.next


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
for elem in my_list:
    print(elem, end=' ')
