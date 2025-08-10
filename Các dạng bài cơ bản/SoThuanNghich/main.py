import math 

def kiemtra(number):
    # Chuyển số thành chuỗi 
    s = str(number)
    return s == s[::-1]

# Kiểm tra số 
print(kiemtra(121))
print(kiemtra(123))
