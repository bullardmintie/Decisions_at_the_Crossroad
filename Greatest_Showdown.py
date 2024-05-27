#Task 1
Number = ("Enter 3 numbers. ")
num1 = input("Enter first number.")
num2 = input("Enter second number.")
num3 = input("Enter third number.")

if (num1 > num2) and (num1 > num3):
    print("The largest number is " + num1)
elif (num2 > num1) and (num2 > num3):
    print("The largest number is " + num2)
else:
    print("The largest number is " + num3)


#Task 2
if (num1 < num2) and (num1 < num3):
    print("The smallest number is " + num1)
elif (num2 < num1) and (num2 < num3):
    print("The smallest number is " + num2)
else:
    print("The smallest number is " + num3)


#Task 3
Number = ("Enter 3 numbers. ")
num1 = input("Enter first number. ")
num2 = input("Enter second number. ")
num3 = input("Enter third number. ")


if (num1 >= num2) and (num1 >= num3):
    print("The largest number is " + num1)
elif (num2 >= num1) and (num2 >= num3):
    print("The largest number is " + num2)
else:
    print("The largest number is " + num3)


if ((num1 <= num2) and (num1 <= num3)):
    print("The smallest number is " + num1)
elif ((num2 <= num1) and (num2<= num3)):
    print("the smallest number is " + num2)
elif ((num3 <= num1) and (num3 <= num2)):
    print("the smallest number is " + num3)


if ((num1 == num2)):
    print(num1 + " is equal to " + num2)
elif ((num1 == num3)):
    print((num1 + " is equal to " + num3))
elif ((num2 == num1)):
    print(num2 + " is equal to " + num1)
elif ((num2 == num3)):
    print(num2 + " is equal to " + num3)
elif ((num3 == num1)):
    print(num3 + " is equal to " + num1)
elif ((num3 == num2)):
    print(num3 + " is equal to " + num2)
else:
    print("None are equal!")


if (num1 == num2 == num3):
    print("All the numbers are equal!")