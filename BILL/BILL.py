import math
n=int(input())
if n<=100:
    print(n*1000)
else if n<200&&n>100:
    print(n*1000+n*3000)
else if n<300&&n>200:
    print(n*1000+n*3000+n*5000)
else if n>300:
    print(n*1000+n*3000+n*5000+n*10000)
