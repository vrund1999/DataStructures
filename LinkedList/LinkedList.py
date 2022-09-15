class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertEnd(self, value):
        newNode = Node(value)


        if(self.head == None):
            self.head = newNode

        else:
            curr = self.head
            
            while(curr.next != None):
                curr = curr.next

            curr.next = newNode
    
    def insertFront(self, value):
        newNode = Node(value)

        newNode.next = self.head
        self.head = newNode
    
    def removeFirst(self):
        if(self.head == None):
            return
        elif(self.head.next == None):
            self.head = None
        else:
            self.head = self.head.next

    def removeLast(self):
        if(self.head == None):
            return
        elif(self.head.next == None):
            self.head = None
        else:
            curr = self.head

            while(curr.next.next != None):
                curr = curr.next
            
            curr.next = None
    
    def contains(self, value):
        curr = self.head

        while(curr != None):
            if(curr.value == value):
                return True
            curr = curr.next
        
        return False

    def print(self):
        
        curr = self.head

        if(curr == None):
            print("List is empty")
            
        else:
            while(curr != None):
                print(curr.value, end=' ')
                curr = curr.next
        
        print("")
    
    def indexOf(self, value):
        curr = self.head
        index = 0

        while(curr != None):
            if(curr.value == value):
                return index
            curr = curr.next
            index += 1
        
        return -1




if __name__ == '__main__':
    list = LinkedList()

    list.insertEnd(5)
    list.insertEnd(10)
    list.insertEnd(20)
    list.insertEnd(30)

    list.insertFront(1)
    list.insertFront(21)

    # list.print()
    list.removeFirst()
    list.removeFirst()
    # list.print()
    

    newList = LinkedList()
    newList.print()
    newList.insertFront(1)
    newList.insertFront(2)
    newList.insertEnd(3)
    newList.removeLast()
    newList.print()


    print(newList.contains(3))
    print(newList.contains(2))

    thirdList = LinkedList()
    thirdList.insertEnd(10)
    thirdList.insertEnd(20)
    thirdList.insertEnd(30)

    print(thirdList.indexOf(10))
    print(thirdList.indexOf(11))
    print(thirdList.indexOf(30))