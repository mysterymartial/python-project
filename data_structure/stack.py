class Stack:
    def __init__(self,capacity=4):
        self.capacity = capacity
        self.size = 0
        self.elements = [None]*capacity

    def is_empty(self):
        return self.size == 0
    def get_size(self):
        return self.size
    def __increase_capacity(self):
        self.capacity =self.capacity *2
        new_elements = [None]*self.capacity
        new_elements[:self.size ] = self.elements
        self.elements = new_elements
    def push(self, element):
        if self.size == self.capacity:
            self.__increase_capacity()
        self.elements[self.size] = element
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        self.size -= 1
        element = self.elements[self.size]
        self.elements[self.size] = None
        return element

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.elements[self.size -1]

    def get_capacity(self):
        return self.capacity





