class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
def create_linklist(li):
    head=Node(li[0])#头节点
    for element in li[1:]:
        node=Node(element)#创造节点
        node.next=head
        head=node
    return head
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
LK=[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
lk=create_linklist_tail(LK)
print_linklist(li)
