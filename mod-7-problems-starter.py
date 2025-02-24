# Module 7: Practice Problems

'''
#1. Write a function called count_vowels(input) that takes a string
#    and returns the number of vowels (a, e, i, o, u) in it.

# Defining a function
'''

input = ("Write a function called count vowels.")    # This is the sentence (input) use to find how many vowels.
def count_vowels(input):
    vowels = "aeiouAEIOU"
    num_of_vowels = 0
    for x in input:             # Goes through the characters in (input) and finds the stated variable (vowels)
        if x in vowels:
            num_of_vowels += 1  # This will count the num of vowels in the string, adding to the count for every vowel found in (input).

    return num_of_vowels

# Calling a function, this is count_vowels(input) from defining a function.
print(count_vowels(input))

'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
    Test: racecar (True), pikachu (False), Racecar (True)
    Input: string (s)
    Output: boolean
    Function body: lowercase s, flip s and save to new variable (flipped_s), and then compare s & flipped_s
'''

def is_palindrome(s):
    lower_s = s.lower()
    flipped_s = lower_s[::-1]
    return lower_s == flipped_s

print(is_palindrome("pikachu"))
print(is_palindrome("racecar"))
print(is_palindrome("Racecar"))

'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
    For example, water is very effective to fight fire.
    Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
    strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
    simple type effectiveness rules. Your solution only needs to work for these three sets of input:
    print(type_advantage("Water", "Fire"))  # "Super Effective"
    print(type_advantage("Fire", "Water"))  # "Not Very Effective"
    print(type_advantage("Electric", "Grass"))  # "Neutral"
'''
# Test: attack effectiveness
# Function: attack advantage
# Input: (attacker, defender)
# Output: "return string"

def type_advantage(attacker, defender):
    if attacker == "water" and defender == "fire":
        return "Super Effective"
    elif attacker == "fire" and defender == "water":
        return "Not Very Effective"
    elif attacker == "electric" and defender == "grass":
        return "Neutral"

print(type_advantage("water", "fire"))  # "Super Effective"
print(type_advantage("fire", "water"))  # "Not Very Effective"
print(type_advantage("electric", "grass"))  # "Neutral"

'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
'''
# Test: customer ferry fare w or w/o vehicle
# Function: ferry_fare(age, vehicle)
# Input: customer age, w or w/o vehicle
# Output: customer cost

def ferry_fare(age, vehicle):
    if age >= 19 and age <= 64:
        if vehicle == "yes":
            return 20  # 20 dollars for adult with a vehicle
        else:
            return 10  # Adult fare without a vehicle
    elif age >= 65:
        if vehicle == "yes":
            return 15  # 15 dollars for senior with a vehicle
        else:
            return 5  # Senior fare without a vehicle
    else:
        return 0  # 18 and under are free.

# Examples of age with or w/o vehicle.
print(ferry_fare(40, "yes"))
print(ferry_fare(70, "no"))

'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
'''

def level_up(experience):
    if 0 <= experience <= 99:
        return "level 1"  # 0-99 XP
    elif 100 <= experience <= 199:
        return "level 2"  # 100-199 XP
    elif experience >= 200:
        return "level 3"  # 200+ XP

# Examples
print(level_up(300))
print(level_up(200))

