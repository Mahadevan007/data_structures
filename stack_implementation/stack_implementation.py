class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(selfs):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

