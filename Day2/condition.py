num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 > num2:
    if num1 > num3:
        print(num1, "is the largest number which is ", num1)
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number which is ", num2)
else:
    print(num3, "is the largest number which is ", num3)

# # For odd or even number
# if num1 == 0:
#     print("It is zero.")
# elif num1 % 2 == 0:
#     print(num1, " is an even number.")
# else:
#     print(num1, " is an odd number.")
