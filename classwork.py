
a =7
b =5
print (a)
print(b)
c =a
a =b
b =c
print(a)
print(b)

#Write a program that asks your name and then greets you by your name
name =input("Enter your name: ")
print("hello!",(name))


#Write a program that asks the user for the radius of a circle and the prints out the area of the circle.

import math

Radius =int(input("Enter your radius: "))
area = math.pi *(Radius ** 2)
print(area)

#Write a program that asks the user for three integer numbers.
# The program prints out the sum, product, and average of the numbers.

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))
sum = num1 + num2 + num3
product = num1 * num2 * num3
average = float(num1 + num2 + num3) / 3
print(sum)
print(product)
print(average)

#Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti).
# The program converts the input to full kilograms and grams and outputs the result to the user:

talents = int(input("Enter number of talents: "))
lots = float(input("Enter number of lots: "))
pounds = float(input("Enter number of pounds: "))
total_talents = talents *20*32*13.3
total_pounds = pounds*32*13.3
total_lots = lots*13.3
total_grams = total_talents + total_pounds + total_lots

kilograms = int(total_grams/1000)
grams = total_grams%1000
print(f"Total number of kilograms:{kilograms} and the {grams:.2f} grams")


#Write a program that draws two random combinations of numbers for a combination lock:
# 3-digit code where each number is between 0 and 9.
# 4-digit code where each number is between 1 and 6.

import random
code1 = random.randint(0,9)
code2 = random.randint(0,9)
code3 = random.randint(0,9)
codeA =f"{code1}{code2}{code3}"

code4 = random.randint(1,6)
code5 = random.randint(1,6)
code6 = random.randint(1,6)
code7 = random.randint(1,6)
codeB = f"{code4}{code5}{code6}{code7}"
print(codeA)
print(codeB)

#Write a program that asks the user for the length and width of a rectangle.
# The program then prints out the perimeter and area of the rectangle.
# The perimeter of a rectangle is the sum of the lengths of each four sides.

L = int(input("Enter the length of the rectangle: "))
B = int(input("Enter the breadth of the rectangle: "))
Area = L*B
perimeter = 2*(L+B)
print(Area)
print(perimeter)


