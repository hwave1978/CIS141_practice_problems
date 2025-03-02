# Module 8: Practice Problems
'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.
'''
# Writing the file "gardening_tips.txt"
file = open("gardening_tips.txt", "w")
file.write("Three tips for planting starts:\n")
file.write("\t1. Choose the Right Soil: Start with well-draining soil. Healthy\n\t soil supports strong roots and promotes better growth.\n")
file.write("\t2. Water Wisely: Water your plants early in the morning or late\n\t in the evening to minimize evaporation. Avoid overwatering, as\n\t it can lead to root rot.\n")
file.write("\t3. Give Your Plants Enough Sun: Most plants need at least 6 hours\n\t of direct sunlight a day. \n")
file.close()

file = open("gardening_tips.txt", "r")     # Found @ python101/Chapter-18/read_method_demo.py
print(file.read())
file.close()

'''
#2. Write a Python program that allows users to log their hiking trips. The program should:
    - Use a while loop to repeatedly ask for a hike name and distance in miles
    - Save each entry to hiking_log.txt (each hike on a new line)
    - When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''

file = open("hiking_log.txt", "w")      # This code (25-27) must be here, otherwise the inputs continue to be written on top of code written before.
file.write("")                          # it is amended to previuos test.
file.close()

file = open("hiking_log.txt","a")

while True:
    hiking_trail = input("What hiking trail that you will be traversing today? Press 0 to exit. ")
    if hiking_trail == "0":
        break
    distance = input("How many total miles (distance) was traversed for this hike? Press 0 to exit. ")
    if distance == "0":
        break
    file.write(hiking_trail + "\t" + distance + "\n")
file.close()

with open("hiking_log.txt", "r") as file:          # The code refers back to video lecture 3, 'with' Keyword and Processing Text Files with For Loops.
    print("\nContents of the hiking log:")         # This line prints the contents of the log when "0" is entered.
    print(file.read())

'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console
'''

file = open("song_lyrics.txt", "w")         # Writing the " Itsy Bitsy Spider" lyrics to file
file.write("The itsy bitsy spider\nclimbed up the waterspout.\nDown came the rain\nand washed the spider out.\nOut came the sun\nAnd dried up all the rain,\nAnd the itsy bitsy spider\nclimbed up the spout again.\n")
file.close()

file = open("song_lyrics.txt", "r")     # Reading the lyrics on file.
lyrics = file.read()                    # Reads the entire song's lyrics. The lyrics are stored in the variable "lyrics"
file.close()

five_words = ["bitsy", "spider", "climbed", "rain", "sun"]      # These are the 5 words I want to count from the "lyrics" variable.

frequency_of = {}                                               # This is the dictionary, it has no contents.
for words in five_words:                                        # This is a "for" loop, it counts the iteration of the 5 words, in five_words.
    frequency_of[words] = lyrics.count(words)                   # This loop is how the dictionary is created. The program counts the iteration of
#                                                               # "words" from the five_words and places them into "frequency_of" which is the dictionary.
print(frequency_of)                                             # This is the dictionary that prints the word and number of times it appears.



'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.
'''

# I used the same concept as above to complete this problem.

file = open("poll.txt", "w")
file.write("yea,nay,yea,yea,nay,yea,nay,yea,nay,yea,yea,nay,yea,nay,yea,nay,yea,yea,nay,yea,nay,yea,nay,yea,yea,nay,yea,nay,yea,nay,yea,yea,nay,yea,nay")
file.close()

file = open("poll.txt", "r")
votes = file.read()
file.close()

yea_nay = ["yea", "nay"]

frequency_of = {}
for word in yea_nay:
    frequency_of[word] = votes.count(word)

print(frequency_of)



