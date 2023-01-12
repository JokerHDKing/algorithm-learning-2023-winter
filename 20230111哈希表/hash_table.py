class  linklist:
    class Node:# 节点类（单链表）
        def __init__(self,item=None):
            self.item = item
            self.next=None
    class LinklistIterator:##迭代器类
        def __init__(self,node):
            self.node=node
        def __next__(self):
            if self.node :#
                curnode=self.node
                self.node=curnode.next
                return curnode.item
            else:
                raise StopIteration

        def __iter__(self):#返回自己
            return self
        
    def __init__(self,iterable=None):#允许传一个列表
        self.head=None
        self.tail=None
        if iterable:
            self.extend(iterable)
    #插入
    def append(self,obj):
        s=linklist.Node(obj)#插入的节点
        if not self.head:#当头节点为空时差插入节点
            self.head=s
            self.tail=s
        else:#当链表部不为空时
            self.tail.next=s
            self.tail=s

    def extend(self,iterable):
        for obj in iterable:
            self.append(obj)
    
    # 查找该值是否存在
    def find(self,obj):
        for n in self:
            if n==obj:
                return True
        else:
            return False
        
    def __iter__(self):#让链表支持迭代
        return self.LinklistIterator(self.head)
    
    def __repr__(self) :
        return "<<" +",".join(map(str, self)) + " >>"
class HashTable:
    def __init__(self,size=101):
        self.size=size
        self.T=[linklist() for i in range(self.size)]
    def h(self,k):
        return k % self.size
    #插入
    def insert(self,k):
        i=self.h(k)
        if self.find(k): #当查找到时。表示重复差如·
            print("Duplicated Insert.")
        else:
            self.T[i].append(k)

    #查找
    def find(self,k):
        i=self.h(k)
        return  self.T[i].find(k)


lk=linklist([1,2,3,4,5])
for element in lk:
    print (element)
print(lk)

ht=HashTable()
ht.insert(0)
ht.insert(1)
ht.insert(3)
ht.insert(101)
print(ht.T)
print(ht.find(101))


