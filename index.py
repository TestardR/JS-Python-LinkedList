class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def append(self, value):
        newNode = Node(value)
        self.tail['next'] = newNode
        self.tail = newNode
        self.length + 1
        return self

    def preprend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length + 1
        return self
  

myLinkedList = LinkedList(10)
myLinkedList.append(2)
myLinkedList.preprend(5)
print(myLinkedList)
