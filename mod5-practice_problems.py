# mod5-practice problems

#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.

num = int(input("Enter a positive number: "))
i = 1
sum = 0
while i <= num:
    sum += i
    i += 1
print("The sum of your number is:", sum)

# e.g. 5 -> this will add the range of numbers begining at 1,2,3,4, to 5.
# 1+2= 3+3= 6+4= 10+5=15 The sum is 15

#2. Define a string variable (e.g., my_string = "Olympic College"). Use a for loop to print each character on its own line.
#   Convert each character to uppercase before printing.

string = "Seattle Mariners"

for char in string:
    print(char.upper())         #.upper() -> UPPERCASE
print("Playoff bound 2025?")

#3. Use a for loop and the range() function to print all even numbers from 2 to 20.

for i in range(0, 21, 2): # Step value of 2
    print(i)

#4. Use nested for loops to create a simple multiplication table for numbers 1 through 5.
#   Format your output so that each row corresponds to multiplying by a specific number. Example output:
# 1   2   3   4   5
# 2   4   6   8   10
# 3   6   9   12  15
# 4   8   12  16  20
# 5   10  15  20  25

for i in range(1, 6):                   # Row
    for j in range(1, 6):               # Column
        print(f"{i * j:2}", end=" ")    # end=" " layout numbers horizontal, space between the numbers on chart.
#
    print()                             #f"{i*j} rows * columns
#                                       :2} the numbers in columns will have 2 spaces in front. (alignment)
#                                       Keeps the layout in row and columns

#5. Write a program that continuously asks the user to input a number. If the user enters 0,
#immediately stop asking for more numbers. Otherwise, print the number they entered.

#Sample interaction:

#Enter a number (0 to stop): 4
#You entered 4
#Enter a number (0 to stop): 7
#You entered 7
#Enter a number (0 to stop): 0
#Exiting...


for i in range (11):
    n = int(input("Enter a number between 0 and 10: "))

    if n == 0:
        print("\nExiting program\n")
        break

    print(f"You entered: {n}")

