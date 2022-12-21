s ="abceabcabc"
k =1
if len(s)==1:
    print(s)
if k==1:
    indexs=[]
    min1=min(s)
    for i in range(len(s)):
        if s[i]== min1:
            indexs.append(i)#收集该字符串中最小值的索引
    if len(indexs)==1:
        print(s[indexs[0]:]+s[0:indexs[0]]) 
    else:
        s1=[]
        for i in range(len(indexs)-1):
            M=min(len(s),indexs[i+1]-indexs[i])
        M=min(M,len(s)-indexs[-1]+indexs[0])
        print(M)
        for i in indexs:
            if M>len(s)-i-1:
                s1.append(s[i:]+s[:1+M+i-len(s)])
            else:
                s1.append(s[i:i+1+M])
        s1=s1.index(min(s1))
        print(s[indexs[s1]:]+s[:indexs[s1]]) 
    
# return "".join(sorted(s))#当k>1时，那么就可以将每个字母进行选择性排序，就可以称为一个有序的队列