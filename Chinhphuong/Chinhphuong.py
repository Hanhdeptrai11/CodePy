import math

n=int(input())

check = False

for i in range(1, n + 1 ):
    if (i**2 == n):
        check=True
        break

if (check==True):
    print( "yes")
else:
    print( "no")
