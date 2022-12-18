from SinglyLinkedList import SinglyLinkedList

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insertAtBeginning(7)
    sll.insertAtEnd(5)
    sll.showList()
    #print(sll.listLength())
    sll.insertAtPos(1,0)
    sll.showList()
    sll.insertAtPos(0,-1)
    sll.showList()
    sll.insertAtPos(4,-1)
    sll.showList()