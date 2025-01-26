# mod3-problems.py

#1 Prompt the user for a word.

word = input("Input a word: ")
times = int(input("Just for fun, how many times should I repeat your word? "))
times_reapeated = word * times
print (f"This is your word repeated: {times_reapeated}\n")

#2 Prompt the user for their name and their age.

# Concatenation (+) example from lecture video
# word = "fantastic "
# str1 = "Hello, " + word + "World!"
# print (str1)
# Hello, fantastic World!

name = input("What is your name? ")
age = int(input("What is your age: "))
year_older = age + 1

str1 = "Hello, " + name + "! You are " + str(age) + " years old. Next year, you will be " + str(year_older) + " years old.\n"
print (str1)

#3. Prompt the user for a sentence and a word to try to find in that sentence.

# in Keyword, will output a true false statement
#str3 = "apple"
#print ("l" in str3)
#print ("o, W" in str1)
#print ("word" in str1) #T/F: are BOOLEANS

sentence = input("Write a sentence below and then choose any word.  If the word is in the sentence,\nthe program will answer with a True statement, if the word is not in the sentence\nit will respond with False.\nEnter sentence here: ")

word = input("Choosen word: ")
found = word in sentence
print (found)

print ("Thanks for playing along.\n")

#4. Prompt the user for: a word, a first index, and a last index. Slice the word at
# the indexes provided by the user and print to the screen.

# I had to read a bit more about indexing to "kind of" understand what's happening.
# using the word e.g. Hello World! and typing the numbers 2 and 8 into the 1st and 2nd
# indexes, the output returns "llo wo". This is because the index begins at the zeroth
# place "H", and indexing returns all the letters starting at 2 "l" and one letter within
# the 8th character position, "o". Watching the lecture and a bit more searching on-line
# helps, I just can't see the overall reason and where it applies with coding at this point.

word = input("Please enter a word: ")
first_index = int(input("Enter first index here: "))
second_index = int(input("Enter second index here: "))
print (word[first_index:second_index])

#5. Print 3 words with a | character (called a pipe) in between them. Use the appropriate keyword argument in print() to do so.

phrase = "My daughter's are:"
phrase = phrase.split(" ")
phrase = "|".join(phrase)
print (phrase)
