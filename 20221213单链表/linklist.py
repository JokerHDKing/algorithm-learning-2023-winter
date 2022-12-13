class Node:
    def __init__(self,item):
        self.item = item
        self.next=None

def create_linklist(li):
    head=Node(li[0])#头节点
    for element in li[1:]:
        node=Node(element)#创造节点
        node.next=head
        head=node
    return head

def create_linklist_tail(li):
    head=Node(li[0])#头节点
    tail=head#尾节点
    for element in li[1:]:
        node=Node(element)
        tail.next=node
        tail=node
    return head

def print_linklist(lk):
    while lk:
        print (lk.item,end=" ")
        lk=lk.next
li=create_linklist([1,2,3])
lk=create_linklist_tail([1,2,3,87,46871,87,61,6,76])
print ("头插法",end=" :")
print_linklist(li)
print()
print ("尾插法",end=" :")
print_linklist(lk)


