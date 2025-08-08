import math 
 
# Hàm kiểm tra số nguyên tố 
def kiemtra(number):
    if number <= 1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False 
    return True 

a=int(input())
if kiemtra(a) == True:
    print("Đây là số nguyên tố")
else: print("Đây không phải là số nguyên tố")
