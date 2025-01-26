import math

# 1. Create a program that prints the following output to the screen: "Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked."

print ("Water. Earth. Fire.Air. Long ago, the four nations lived together in harmony.  Then, everyting changed when the fire Nation attacked.")

# 2. Create a program that prompts for 2 numbers and then outputs the addition, subtraction, multiplication, and division of the first number by the second number.

num1 = float(input("Hello, I'm HAL. Please input any two numbers after the number 1. I will compute their addition, subtraction, multiplication, and division (with the first number divided by the second. Input the first number here: "))
num2 = float(input("Input second number here: "))
print ("Here are the answers:")

result = addition = num1 + num2
print (result)

result = subtraction = num1 - num2
print (result)

result = multiplication = num1 * num2
print (result)

result = division = num1 / num2 , num1 % num2 #--> This is the modulus of the divided number.
print (result)

# 3. Create a program that prompts for the side lengths of a triangle and computes the area using Heron's formula. (https://en.wikipedia.org/wiki/Heron%27s_formula)

print ("Let's find the area of a triangle. Enter the length of sides a, b and c below, to find the area of a triangle. ")

#Sides of the triangle
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

#Find the semi-perimeter of a triangle to find the area --> s = (a+b+c) /2 --> Let the sides be a=4, b=13, c=15 --> s = (4+13+15) /2 --> s = 32/2
#--> s = 16
s = (a+b+c) / 2

#To find the area, use the formula: A = sqrt. s (s-a)(s-b)(s-c) --> 16-4 = 12, 16-13 = 3, 16-15 = 1 --> sqrt. 16*12*3*1 = 576 --> sqrt. 576 = 24
area = math.sqrt (s * (s-a)*(s-b)*(s-c))

print(f"The area of the triangle is: {area:.2f}.")

# 4. Create a program that computes different statistics given five numbers including the total, average, minimum, maximum, range, and standard deviation (https://en.wikipedia.org/wiki/Standard_deviation).

#This will ask the participant their name and then ask for five numbers.

user_name = input ("What is your name? ")
print ("Hello,", user_name)
print ("Enter five numbers and I will compute their total, average, minimum, maximum, range, and standard deviation.")
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))
num4 = int(input("Fourth number: "))
num5 = int(input("Fifth number: "))

#These are the commands to calculate total, average, minimum, maximum, range, and standard deviation.

total = sum([num1, num2, num3, num4, num5])
average = total / 5
minimum = min([num1, num2, num3, num4, num5])
maximum = max([num1, num2, num3, num4, num5])
range_value = maximum - minimum
variance = sum((x - average) ** 2 for x in [num1, num2, num3, num4, num5]) / len([num1, num2, num3, num4, num5])
standard_deviation = math.sqrt(variance)

print ("Ta-da! The answers are below:")

print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Range: {range_value}")
print(f"Standard Deviation: {standard_deviation:.2f}")

print ("This is the end.")
