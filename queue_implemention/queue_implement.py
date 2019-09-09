class queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def add(self,item):
        self.items.insert(0,item)

    def delete(self):
        self.items.pop()

    def size(self):
        return len(self.items)