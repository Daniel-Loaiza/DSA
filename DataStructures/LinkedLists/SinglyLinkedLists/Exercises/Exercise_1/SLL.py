from Node import Node

class SLL:

    # Constructor
    def __init__(self):
        self.head = None
        self.next = None
        self.length = 0

    # Method for getting the length of the list
    def listLength(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current= current.getNext()
        return count    

    #Method for inserting values at the end of the list from command line
    def insertValues(self):
        value = input("Insert a value or simply\nwrite 'quit' to exit the program\n")
        while(value!="quit"):      
            temp=Node()
            number = int(value)
            temp.setData(number)                
            if self.length == 0:
                self.head = temp
            else:
                current = self.head
                while current.next is not None:
                    current = current.next 
                current.next = temp               
            self.length +=1
            value = input("Insert a value or simply\nwrite 'quit' to exit the program\n")

    #Method for printing the list
    def showList(self):
        current = self.head
        while current:
            print(current.data)            
            current = current.getNext()
    
    #Method for calculating the average of the list values
    def getAverage(self):
        sumOfvalues=0
        current=self.head
        while(current):
            sumOfvalues+=current.getData()
            current = current.getNext()
        return sumOfvalues/self.length
