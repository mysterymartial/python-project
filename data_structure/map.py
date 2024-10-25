class Map:
    def __init__(self):
        self.keys = []
        self.values = []

    def is_empty(self):
        return len(self.keys) == 0
    def put(self, key, value):
        if key  in self.keys:
            raise KeyError(f"{key} already exists, use upadte to modify")
        self.keys.append(key)
        self.values.append(value)

    def get(self, key):
        if key in self.keys:
            index = self.keys.index(key)
            return self.values[index]
        return None

    def update(self, key, value):
        if key not in self.keys:
            raise KeyError(f"{key} already exists, use update to modify or use put to add key value pair")
        index = self.keys.index(key)
        self.values[index] = value

    def remove(self, key):
        if key not in self.keys:
            raise KeyError(f"{key} does not exist, use update to modify or use put to add key value pair")
        index = self.keys.index(key)
        self.values.pop(index)
        self.keys.pop(index)

    def clear(self):
        self.keys.clear()
        self.values.clear()


    def size(self):
        return len(self.keys)

    def items(self):
        return list(zip(self.keys, self.values))

    def __repr__(self):
        return f"Map ({self.items()})"


