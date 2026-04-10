class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def append(self, val):
        new_node = Node(val)  
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:   
                current = current.next
            current.next = new_node

    def traverse(self):  
        if self.head is None:
            print("Singly linked list is empty")
        else:
            current = self.head 
            while current is not None:
                print(current.val, end=" -> ")
                current = current.next
            print("None")
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(40)
sll.append(80)

sll.traverse()