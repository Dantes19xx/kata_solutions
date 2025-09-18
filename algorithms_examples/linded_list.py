class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Вставка в начало
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Удаление по значению
    def delete(self, key):
        temp = self.head

        #  проверяем особый случай: список не пустой (temp не None) и первый узел содержит искомое значение.
        if temp and temp.data == key:
            # если ключ в голове, просто сдвигаем head на следующий узел. Старый первый узел исключается из списка.
            self.head = temp.next
            return

        # устанавливаем переменную для хранения предыдущего узла (перед temp).
        prev = None
        # идём по списку, пока не найдём узел с data == key или не дойдём до конца (temp станет None).
        while temp and temp.data != key:
            # prev = temp — запоминаем текущий узел как предыдущий.
            prev = temp
            # temp = temp.next — двигаем temp на следующий узел.
            temp = temp.next

        if temp:
            prev.next = temp.next

    # Поиск
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    

lst = LinkedList()

lst.push(10)
lst.push(20)
lst.search(1)
lst.push(30)
lst.search(2)
lst.push(40)
lst.delete(20)