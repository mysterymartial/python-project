class Set(object):
    def __init__(self):
        self.elements = []
    def is_empty(self):
        return len(self.elements) == 0
    def add(self, element):
        if element  in self.elements:
            raise ValueError('Element already added.')
        self.elements.append(element)
    def remove(self, element):
        if element not in self.elements:
            raise ValueError('Element not found.')
        self.elements.remove(element)

    def contains(self, element):
        return element in self.elements

    def clear(self):
        self.elements.clear()


    def size(self):
        return len(self.elements)

    def __repr__(self):
        return f"Set({self.elements})"

