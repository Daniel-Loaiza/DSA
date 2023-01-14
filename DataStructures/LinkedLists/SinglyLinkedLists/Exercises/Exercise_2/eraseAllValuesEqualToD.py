class Node:
    def __init__(self):
        self.data=None
        self.next=None
    def setData(self,data):
        self.data=data
    def setNext(self,Node):
        self.next=Node
    def getData(self):
        return self.data
    def getNext(self):
        return self.next

class SLL(Node):
    def __init__(self):
        self.head=self.tail=super().__init__()
    def insertData(self,data):
        node=Node()
        node.setData(data)
        if(self.head is None):
            self.head=node
        else:
            current=self.head
            while(current.next):
                current=current.next
            current.next=node
    def show(self):
        current=self.head
        while(current):
            print(current.getData())
            current=current.next

    def deleteAllValuesEqualTo(self, data):
        previous=self.head
        current=self.head        
        while(current):
            if(current.data==data):
                if(current == self.head):
                    self.head=self.head.next
                else:
                    previous.next=current.next
                    current=current.next
            else:
                previous=current
                current=current.next
                

sll=SLL()
sll.insertData(1)
"""
sll.insertData(1)
sll.insertData(2)
sll.insertData(3)
sll.insertData(3)
sll.insertData(4)
sll.insertData(5)
"""
sll.show()
sll.deleteAllValuesEqualTo(5)
sll.show()
