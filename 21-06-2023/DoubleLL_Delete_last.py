class Node:
    def __init__(self,data):
        self.data=data
        self.pprev=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                if temp.next is None:
                    print(temp.data,end=" ")
                else:
                    print(temp.data,"<-->",end=" ")
                temp=temp.next

    def delete_last(self):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.prev.next=None

        
    
obj=dll()

n1=Node(100)
obj.head=n1

n2=Node(200)
n1.next=n2
n2.prev=n1

n3=Node(300)
n2.next=n3
n3.prev=n2

obj.display()
print()
obj.delete_last()
obj.display()
