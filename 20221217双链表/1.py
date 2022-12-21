nums=[431,922,158,60,192,14,788,146,788,775,772,792,68,143,376,375,877,516,595,82,56,704,160,403,713,504,67,332,26]
maxOperations =80
import math
# if len(nums)==1:
#     return int(math.floor(math.pow(nums[0],1.0/maxOperations)))
while maxOperations:
    nums=sorted(nums)
    print(nums)
    m=nums[-1]
    for i in range(len(nums)):
        if nums[i]*2>=m:
            break
    m2=nums[i]
    x=m-m2
    nums.pop()
    nums.append(x)
    nums.append(m2)
    maxOperations-=1
    print(nums)
