import math 
def kiemtra(number):
    # Chuyển số thành chuỗi để lấy các chữ số
    digits = [int(d) for d in str(number)]
    # Lấy số chữ số
    k = len(digits)
    # Tính tổng luỹ thừa bậc k
    total = sum(d**k for d in digits)
    return total == number

#Test 
print(kiemtra(153))
print(kiemtra(177))
