class Queue:
    def __init__(self,size=100):
        self.queue = [0 for _ in range(size)]#队列的大小
        self.size=size#队列的最大长度
        self.rear=0#队尾（进队）
        self.front=0#队首（出队）
    

    #入队
    def push(self,element):
        if not self.is_filled():
            self.rear=(self.rear+1)%self.size#入队的队尾的变化
            self.queue[self.rear] = element#在该位置上添加element元素
        else:
            raise IndexError("Queue is filled.")
    
    #出队
    def pop(self):
        if not self.is_empty():
            self.front=(self.front+1)%self.size#出队的队首的变化
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty.")

    #判断是否对空
    def is_empty(self):
        return self.front == self.rear
    
    #判断是否队满
    def is_filled(self):
        return (self.rear +1)%self.size == self.front

q=Queue(5)
for i in range(4):
    q.push(i)#入队
print(q.pop())#队出




    