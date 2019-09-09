class node:

    def __init__(self, value):
        self.value = value
        self.next_node = None


class singlylinkedlist:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insertend(self, value):
        newnode = node(value)
        if (self.tail == self.head == None):
            self.head = self.tail = newnode
        else:
            self.tail.next_node = newnode
            self.tail = newnode
            self.length = self.length + 1

    def insertbegin(self, value):
        newnode = node(value)
        if (self.head == self.tail == None):
            self.head = self.tail = newnode
        else:
            newnode.next_node = self.head
            self.head = newnode
            self.length = self.length + 1

    def insertnlocation(self, value, n):
        if (n > self.length):
            return "Wrong position"
        if (n == 1):
            self.insertbegin(value)
        else:
            newnode = node(value)
            if (self.head == self.tail == None):
                self.head = self.tail = newnode
            else:
                count = 1
                temp = self.head
                while (count != n - 1):
                    temp = temp.next_node
                    count = count + 1
                newnode.next_node = temp.next_node
                temp.next_node = newnode
                if (n == 5):
                    self.tail = newnode

    def printnnode(self, n):
        if (self.head == self.tail == None):
            return "No nodes in the list to print location"
        if (n > self.length):
            return "wrong position"
        temp = self.head
        count = 0
        while (count != n - 1):
            temp = temp.next_node
            count = count + 1
        return temp.value

    def printlist(self):
        if (self.head == self.tail == None):
            return "no list to print"
        temp = self.head
        ourlist = []
        while temp != None:
            ourlist.append(temp.value)
            temp = temp.next_node
        return ourlist

    def deleteend(self):
        if (self.head == self.tail == None):
            return "no nodes to delete"
        temp = self.head
        while temp.next_node != self.tail:
            temp = temp.next_node
        temp.next_node = None
        self.tail = temp

    def deletebegin(self):
        if (self.head == self.tail == None):
            return "no nodes to delete"
        temp = self.head
        self.head = self.head.next_node
        temp = None

    def deletennode(self, n):
        if (self.head == self.tail == None):
            return "no nodes to delete"
        if (n > self.length):
            return "Wrong position"
        count = 1
        temp = self.head
        while (count != n - 1):
            temp = temp.next_node
            count = count + 1
        var = temp.next_node
        temp.next_node = var.next_node
        var = None

    def searchnode(self, a):
        temp = self.printlist()
        for i in range(0, len(temp)):
            if temp[i] == a:
                return "position : " + str(i + 1)
        else:
            print("No " + str(a) + " in the list")



