class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = node()
    
    def append(self, data):
        newNode = node(data)
        current = self.head

        while current.next != None:
            current = current.next
        current.next = newNode

    def length(self):
        current = self.head
        total = 0
        while  current.next != None:
            total += 1
            current = current.next
        return total

    def display (self):
        elements = []
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
            elements.append(currentNode.data)
        print (elements)

    def get(self, index):
        if index >= self.length():
            print ("ERROR: 'Get' index out of range!")
            return None
        currentIndex = 0
        currentNode = self.head
        while True:
            currentNode = currentNode.next
            if currentIndex == index: return currentNode.data
            currentIndex += 1

    def erase(self, index):
        if index >= self.length():
            print ("ERROR: 'Erase' Index out of range!")
            return
        currentIndex = 0
        currentNode = self.head
        while True:
            lastNode = currentNode
            currentNode = currentNode.next
            if currentIndex == index:
                lastNode.next = currentNode.next
                return
            currentIndex += 1


myList = linkedList()

myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)

myList.display()

myList.erase(1)
myList.display()

print( "element at 2nd index: %d" % myList.get(2) )

stop = True