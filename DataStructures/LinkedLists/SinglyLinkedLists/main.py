from SinglyLinkedList import SinglyLinkedList

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insertAtBeginning(7)
    sll.insertAtEnd(5)
    sll.showList()
    print(sll.listLength())
    sll.insertAtPos(2,0)
    #sll.showList()