import math

n,k=map(long,input().split())
d=0
i=1
for i in n:
if i%k==0 :
    d+=i
print(d)
