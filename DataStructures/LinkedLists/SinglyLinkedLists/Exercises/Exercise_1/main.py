from Node import Node
from SLL import SLL

if __name__=="__main__":
    sll=SLL()
    sll.insertValues()
    #sll.showList()
    #print(sll.listLength())
    print(f"The average of the values of the SinglyLinked list is: {sll.getAverage()}")