from Node import Node

class SinglyLinkedList:

    #constructor
    def __init__(self):
        self.head = None
        self.next = None
        self.length = 0

    #Method for printing the list
    def showList(self):
        current = self.head
        while current:
            print(current.data)            
            current = current.getNext()
        
    def listLength(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current= current.getNext()
        return count

    #method for inserting a new node at the beginning of the Linked List (at the head)
    def insertAtBeginning(self,data):
        newNode = Node()
        newNode.setData(data)
    
        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        self.length += 1

    #method for inserting a new node at the end of a Linked List
    def insertAtEnd(self, data):
        newNode = Node()
        newNode.setData(data)

        if self.length == 0:
            self.head = newNode
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()

            current.setNext(newNode)
            
        self.length +=1

    #Method for inserting a new node at any position in a Linked List
    def insertAtPos(self,pos,data):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insertAtBeginning(data)
            else:
                if pos ==self.length :
                    self.insertAtEnd(data)
                else:
                    newNode = Node()
                    newNode.setData(data)
                    count= 0
                    current= self.head
                    while count< pos-1:
                        count+=1
                        current=current.getNext()
                    newNode.setNext(current.getNext())
                    current.setNext(newNode)
                    self.length += 1
            
    #method to delete the first node of the linked list
    def deleteFromBeginning(self):
        if self.length == 0:
            print("The list is empty")
        else:
            self.head = self.head.getNext()
            self.length -= 1

    #Method to delete the last node of the linked list
    def deleteLastNodeFromSinglyLinkedList(self):
        if self.length == 0:
            print("The list is empty")
        else:
            currentnode = self.head
            previousnode = self.head
            while currentnode.getNext() != None:
                previousnode = currentnode
                currentnode = currentnode.getNext()
            
            previousnode.setNext(None)
            self.length -= 1

    ##Delete with node from linked list
    def deleteFromSinglyLinkedListWithNode(self, node):
        if self.length == 0:
            raise ValueError("List is empty")
        else:
            current= self.head
            previous = None
            found = False
            while not found:
                if current == node:
                    found = True
                elif current is None:
                    raise ValueError("Node not in Linked List")
                else:
                    previous = current
                    current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        self.length -= 1

    #Delete with data from linked list
    def deleteValue(self, value):
        currentnode = self.head
        previousnode = self.head
        while currentnode.next != None or currentnode.data != value:
            if currentnode.data == value:
                previousnode.next = currentnode.next
                self.length -= 1
                return
            else:
                previousnode = currentnode
                currentnode = currentnode.next
        print("The value provided is not present")
    
    #Method to delete a node at a particular position
    def deleteAtPosition(self,pos):
        count = 0
        currentnode =self.head
        previousnode = self.head
        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        else:
            while currentnode.next != None or count < pos:
                count = count + 1
                if count== pos:
                    previousnode.next = currentnode.next
                    self.length -= 1
                    return
                else:
                    previousnode = currentnode
                    currentnode = currentnode.next

    # Function to reverse the linked list
    def reverse(self):
        previousnode = None
        currentnode = self.head
        while(currentnode is not None):
            next = currentnode.next
            currentnode.next = previousnode
            previousnode = currentnode
            currentnode = next
            self.head = previousnode
