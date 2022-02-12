## Fundamental data types and storing one value into a variable.
# Store an integer value into a variable named integer_variable.

# integer_variable = int(input("Enter a number - "))

# Store an float value into a variable named float_variable.

# float_variable = float(input("Enter a number - "))

# Store an string into a variable named string_variable.

# string_variable = input("Enter whatever as you want - ")

# Store an boolean value into a variable named boolean_variable.

# boolean_variable = bool(input("Enter a boolean number - "))

## Type casting
# Convert float_variable to integer and print the result.

# x = int(float_variable)
# print(x)

# Convert boolean_variable to integer and print the result.

# y = int(boolean_variable)
# print(y)

# Add integer_variable and boolean_variable. Print the result and explain why this result came.
# print(integer_variable + boolean_variable)

## Some operations on integer.
# Take an integer from user and store it in a variable.

# y = int(input("Enter a number - "))

# Add 2 to the variable and print the result.

# print(y+2)

# Calculate the remainder when the variable is divided by 5.

# a = y%5
# print(a)

# Calculate square of the value stored in the variable.

# print(y**2)

## Collection type of data types and storing multiple values into a variable.
# Create a set of 5 elements.

# l = [1,2,4,5,6]

# Create a list of 7 elements.

# m = [3,4,5,6,7,8,9]

# Take a number from user and add this number at the last of the list.

# list = []
# y = int(input("Enter number of elements : "))
# l.append(y) #l.pop() to remove last element.
# print(l)

# Print length of the list.

# print(len(l))
# print(len(m))

## Some operations on list.
# Store a list of length 5 in a variable.

# z = len(l)

# Print second element of the list.

# print(l[1])

# Calculate sum of second and third element of the list.

# print(l[1]+l[2])

# Calculate product of first and fifth element.

# print(l[0]*l[4])

# Print last element of the list.

# y = len(l)
# print(l[y-1])

# Print second last element of the list.

# y = len(l)
# print(l[y-2])

## For loop
# Print 0 to 10.

# for i in range(0,11):
#     print(i)

# Print 1 to 10.

# for i in range(1,11):
#     print(i)

# Print 10 to 14.

# for i in range(10,15):
#     print(i)

# Take an integer from user and print from 0 upto that digit. For example: if user gives input 5 then, print 0 to 5 in console.

# x = int(input("Enter a number - "))
# for i in range(0,x+1):
#     print(i)

# Take an integer from user and print from 1 upto that digit. For example: if user gives input 5 then, print 1 to 5 in console.

# x = int(input("Enter a number - "))
# for i in range(1,x+1):
#     print(i)

# Take an integer from user and print from that digit to 1. For example if user gives input 5 then in console print 5, 4, 3, 2, 1.

# x = int(input("Enter a number - "))
# for i in range(1,x+1):
#     print(x+1-i)

# Take an integer from user. Calculate sum of 1 to that digit. For example if user gives input 5 then sum of 1, 2, 3, 4, 5.

# x = int(input("Enter a number - "))
# y = 0
# for i in range(1,x+1):
#     y = y + i
# print(y)

# Take an integer from user. Calculate product of 1 to that digit. For example if user gives input 5 then product of 1, 2, 3, 4, 5.


# x = int(input("Enter a number - "))
# y = 1
# for i in range(1,x+1):
#     y = y * i
# print(y)

# Take an integer from user. Print multiplication table for that number.

# x = int(input("Enter a number - "))
# y = int(input("Till which number table - "))
# for i in range(1,y+1):
#     print(x*i)

# Take an integer from user. Print factorial of that number.

# x = int(input("Enter a number - "))
# y = 1
# for i in range(1,x+1):
#     y = y * i
# print(y)

## If-else condition
# Take a number from user. If the number is greater than 5 print "Number is greater than 5".

# x = int(input("Enter a number - "))
# if x>5:
#     print("Number is greater than 5")
# else:
#     print("Number is less than 5")

# Take a string from user. If the string is equal to 'A' print "You have written A".

# string =input("pls input whatever you want - ")

# if string in ['A','a']:
#     print("You have writtent A")
# else:
#     print("You have not written A")

## While loop.
# Do all the questions in for loop using while loop.

#print 1 to 10.

# i = 1
# while i<11:
#     print(i)
#     i = i + 1

# Print 0 to 10.

# i = 0
# while i<11:
#     print(i)
#     i = i + 1

#Print 10 to 14.
# i = 10
# while i<15:
#     print(i)
#     i = i + 1

# Take an integer from user and print from 0 upto that digit. For example: if user gives input 5 then, print 0 to 5 in console.

# x = int(input("Please enter a number - "))
# i = 0
# while i<x+1:
#     print(i)
#     i = i + 1

# Take an integer from user and print from 1 upto that digit. For example: if user gives input 5 then, print 0 to 5 in console.

# x = int(input("Please enter a number - "))
# i = 1
# while i<x+1:
#     print(i)
#     i = i + 1

# Take an integer from user and print from that digit to 1

# x = int(input("Enter a Number - "))
# i = x
# while i>0:
#     print(i)
#     i = i - 1

# Take an integer from user. Calculate sum of 1 to that digit. For example if user gives input 5 then sum of 1, 2, 3, 4, 5.

# x = int(input("Enter a Number - "))
# y = 0
# i = x
# while i>0:
#     y = y + i
#     i = i - 1
# print(y)

# Take an integer from user. Calculate product of 1 to that digit

# x = int(input("Enter a Number - "))
# y = 1
# i = x
# while i>0:
#     y = y * i
#     i = i - 1
# print(y)

# Take an integer from user. Print multiplication table for that number.

# x = int(input("Enter a number - "))
# y = int(input("Till which number table - "))
# i = 1
# while i<y+1:
#     print(x*i)
#     i = i + 1