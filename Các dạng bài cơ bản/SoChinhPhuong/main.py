import math 

# Hàm kiểm tra số chính phương 
def kiemtra(number):
    if number < 0 :
        return False 
    So=math.sqrt(number)
    if So*So == number:
        return True

a=int(input())
if kiemtra(a) == True:
    print("Đây là số chính phương")
else: print("Đây không phải là số chính phương")
