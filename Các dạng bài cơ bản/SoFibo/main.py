import math
 
def CheckFibo(number):
    if number < 0:
        return False
    a,b = 0,1 #Khởi tạo a và b là 2 số đầu của dãy fibo 
    while a < number: #Duyệt đến khi a>= số 
        a,b = b, a+b #Cập nhật các số Fibo tiếp theo 
    return a == number

#Check đấp án 
print(CheckFibo(177))
print(CheckFibo(5))
