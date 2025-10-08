from node import Node

class Singlylinkedlist:
    def __init__(self):
        self.head=None
    def is_empty(self):
        return self.head is None
    
    def append(self,data):
        node2= Node(data)
        if self.is_empty():
            self.head=node2
        else:
            current= self.head
            while current.next is not None:
                current=current.next
            current.next= node2
            
    def insert(self,position,data):
        node2=Node(data)
        if position==0:
            node2.next=self.head
            self.head=node2
            return
        current = self.head
        for i in range(position-1):
            if current is None:
                print('invalid index')
                return
            current=current.next
        if current is not None:
            node2.next=current.next
            current.next= node2
            
    def pop(self,index=None):
        if self.is_empty():
            print('list is empty')
            return
        if index == 0:
            self.head=self.head.next
            return
        current= self.head
        if index is None:
            prev = None
            while current.next:
                prev=current
                current=-current.next
            if prev:
                prev.next=None
            else:
                self.head=None
            return
        count=0
        prev=None
        while current and count<index:
            prev =current
            current = current.next
            ocunt +=1
        if not current:
            print('index out of range')
            return
        prev.next=current.next             
        
    def search(self,data):
        current= self.data
        posi = 0
        while current:
            if current.data == data:
                return posi
            current= current.next
            posi +=1
        return None
    
    def display(self):
        if self.is_empty():
            print('list is empty')
            return 
        current= self.head
        while current:
            print(f'{current.data}->',end = '')
            current=current.next
        print('None')
        
if  __name__ == "__main__":
    linked_list = Singlylinkedlist()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.display()
    linked_list.insert(1, 15)
    linked_list.display()
    linked_list.pop()
    linked_list.display()
    linked_list.pop(0)
    linked_list.display()
    pos = linked_list.search(20)
    print("Found at index:", pos)
