# num1 = int (input("Enter the value of num1: "))
# num2 = int (input("Enter the value of num2: "))
# num3 = int (input("Enter the value of num3: "))
# num4 = int (input("Enter the value of num4: "))
# num5 = int (input("Enter the value of num5: "))
# num6 = int (input("Enter the value of num6: "))
# num7 = int (input("Enter the value of num7: "))
# num8 = int (input("Enter the value of num8: "))
num = []
for i in range (0, 8):
    ele = int(input("Enter the value: "))
    num.append(ele)
print("Entered value =", num)
num1 = num[0]
num2 = num[1]
num3 = num[2]
num4 = num[3]
num5 = num[4]
num6 = num[5]
num7 = num[6]
num8 = num[7]
s = {num1, num2, num3, num4, num5, num6, num7, num8}
print("Unique set = ", s)