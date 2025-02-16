# Module 6: Practice Problems

#1. Given a list of numbers, write code to iterate through the list and calculate the sum of all even numbers.
#   Print the resulting sum.
number_list = [1,2,3,4,5,6,7,8,9,10,11,12]
print("Listed are the numbers 1-12:", number_list)
evens_sum = 0

for num in number_list:
    if num % 2 == 0:        #modulus operator % used when wanting to test even or odd. When iteration "2" is divided and
        evens_sum += num    # there is no remainder, the number is even. evens_sum = 2. The next even number found is "4",
                            # this is true, so 4 is added to 2 which equals 6.  The steps continue.

print("The sum of the even numbers is:", evens_sum, "\n")

#2. With a list of strings provided, write code that counts how many times the word "Olympic" appears in the list,
#   and then print the count.

list_of_strings = ["I attend Olympic College. On the sporting field they are known as the Olympic College Rangers. I root for Olympic College."]
print("I attend Olympic College. On the sporting field they are known as the Olympic College Rangers. I root for Olympic College.")
count = 0

for string in list_of_strings:
    count += string.count("Olympic")

print("The word Olympic is found", count, "times in the sentence.\n")


#3. Given a list of strings, write code to create a new list that includes only the strings longer than three characters.
#   Print the resulting filtered list.

list_of_string = ["ant","ladybug","bee","butterfly","dragonfly","moth","grasshopper","fly"]
print("Create a list that includes only the insects with names longer than three characters. ant, ladybug, bee,\nbutterfly, dragonfly, moth, grasshopper, and the fly.")
unique_names = []

for string in list_of_string:
    if len(string) > 3:                 # Names greater than 3 characters long. length of words with more than three characters.
        unique_names.append(string)

print("These are the insects with names longer than 3 characters:", unique_names, "\n")


#4. For a list of integers, write code that counts how many numbers are positive and how many are negative,
#   then print both counts.

list_of_int = [-100, -50, -40, -30, -20, -10, 0 , 10, 20, 30, 40, 50 ,60]
print("Of the numbers listed, how many are negative numbers: -100,-50,-40,-30,-20,-10, 0 , 10, 20, 30, 40, 50, 60")
positive = 0
negative = 0

for number in list_of_int:
    if number > 0:
        positive += 1
    if number < 0:
        negative += 1

print("Number of negative numbers:", negative)
print("Number of positive numbers:", positive, "\n")



#5. For a list of integers, use a loop to build a new list where each element is the square of the corresponding element
#   in the original list. Print the new list.
list_of_sqr = [2, 3, 4, 5]
sqr_list = []

for number in list_of_sqr:
    if number > 0:
        sqr_list.append(number ** 2)        # ** 2 is equivilent to squaring

print(sqr_list)

# Again with the numbers already squared.
list_of_sqr = [4, 9, 16, 25]
sqr_list = []

for number in list_of_sqr:
    if number > 0:
        sqr_list.append(number ** 2)        # ** is equivilent to squaring

print(sqr_list)
