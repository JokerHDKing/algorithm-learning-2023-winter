from collections import deque#双向队列
# q=deque()
# q.append(1)#队尾进队
# print(q.popleft())#队首出队

# #用于双向队列
# q.appendleft(1)#队首入队
# q.pop()#队尾出队 
def tail(n):
    with open("test.txt", "r") as f:
        q=deque(f,n)
    return q
#看后几行有什么数据    
print(tail(5))
for line in tail(5):
    print(line,end="")
