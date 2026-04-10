class node:
    def __init__(self,val):
        self.val=val
        self.next=none
class singly_linkedlist:
    def __init__(self):
        self.head=none

    def append(self,val):
        new_node=node(val)
        if self.head==none:
            self.head=new_node
        else:
            current=self.head
            while current is not none:
                current=current.next
            current.next=new_node
        def travese(self)
            if self.head is none:
                print("singly linkedlist is empty")
            else:
                while current is not none:
                    print(current.val,end="")
                    current=current.next
sll=singly_linkedlist()
sll.append(10)
sll.append(20)
sll.append(40)
sll.append(80)
sll.travese()