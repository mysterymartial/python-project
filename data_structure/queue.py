class Queue:
    def __init__(self,capacity=4):
        self.capacity = capacity
        self.size = 0
        self.elements = [None] * self.capacity

    def is_empty(self):
        return self.size == 0
    def get_size(self):
        return self.size

    def enequeue(self, element):
        if self.size == self.capacity:
            self.__ensure_capacity()
        self.elements[self.size] = element
        self.size += 1

    def __ensure_capacity(self):
        self.capacity *=2
        self.elements = self.elements + [None] * self.capacity

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        element = self.elements[0]
        for count in range(1,self.size):
            self.elements[count - 1] = element
        self.elements[self.size -1] = None
        self.size -= 1
        return element

    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.elements[0]
    def get_capacity(self):
        return self.capacity




