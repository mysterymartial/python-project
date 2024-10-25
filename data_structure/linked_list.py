from data_structure.node import Node
class Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    def insert_at_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def is_empty(self):
        return self.head is None

    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return  " -> ".join(map(str, elements)) + " -> None"

    def contains(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            else:
                return False
    def search(self,value):
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def clear(self):
        self.head = None

    def delete(self,value):
        current = self.head
        previous = None

        if current is None:
            return
        if current.data == value:
            self.head = current.next
            current = None
            return
        while current is not None:
            if current.data == value:
                break
            previous = current
            current = current.next
        if current is None:
            return

        previous.next = current.next
        current = None

    def insert_at_index(self, index, value):
        if index < 0:
            raise IndexError("Index cannot be negative")
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for count in range(index -1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next

        if current is None:
            raise IndexError("Index out of range")
        new_node.next = current.next
        current.next = new_node

    def delete_at_index(self, index):
        if index < 0:
            raise IndexError("Index cannot be negative")
        if self.head is None:
            raise IndexError("Position out of bound")
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for count in range(index - 1):
            if current is None or current.next is None:
                raise IndexError("Position out of bounds")
            current = current.next
        current.next = current.next.next



