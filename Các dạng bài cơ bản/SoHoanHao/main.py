import math 

# Hàm kiểm tra số hoàn hảo(số mà có tổng ước bằng chính số đó)
def kiemtra(number):
    if number <= 1:
        return False
    sum = 1    #1 là ước của mọi số 
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            sum=sum+i #i là ước của số thì thêm vào tổng 
            if i != number//i:
                sum=sum+number//i # nếu i khác số/i thì cộng thêm số/i vào tổng 
    return sum == number
# Kiểm tra thử số của hàm 
a=int(input())
if kiemtra(a) == True:
    print("Đây là số hoàn hảo ")
else: print("Đây không là số hoàn hảo")
            
