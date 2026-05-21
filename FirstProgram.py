num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a number: "))
num3 = int(input("Please enter a number: "))
num4 = int(input("Please enter a number: "))

if(num1 >= num2 and num1 >= num3 and num1 >= num4):
    print("Num1 is the greatest")
elif(num2 >= num3 and num2 >= num4):
    print("Num2 is the greatest")
elif(num3 >= num4):
    print("Num3 is the greatest")
else:
    print("Num4 is the greatest")