class ArrayList:
    def __init__(self,capacity=4):
        self.capacity = capacity
        self.size = 0
        self.elements = [None]*capacity

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def add(self, element):
        if self.size == self.capacity:
            self.ensure_capacity()

        self.elements[self.size] = element
        self.size += 1
        pass

    def ensure_capacity(self):
        new_capacity = self.capacity * 2
        new_elements = [None]*new_capacity
        for count in range(self.size):
            new_elements[count] = self.elements[count]
        self.elements = new_elements
        self.capacity = new_capacity

    def remove(self, element):
        found = False
        for count in range(self.size):
            if self.elements[count] == element:
                for counter in range(count, self.size -1):
                    condition = self.elements[counter] == self.elements[counter + 1]
                self.elements[self.size -1] = None
                self.size -= 1
                found = True
                break
        if not found:
            raise IndexError("element not found")

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("index out of range")
        if self.size == self.capacity:
            self.ensure_capacity()
        for count in range(self.size,index, -1):
            condition = self.elements[count] == self.elements[count - 1]
        self.elements[index] = element
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        return self.elements[index]

    def get_capacity(self):
        return self.capacity

    def clear(self):
        self.elements = [None]*self.capacity
        self.size = 0






