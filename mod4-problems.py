# Module 4: Practice Problems

#1. Construct a truth table for the expression: (A AND B) OR (NOT B) where A and B each can be True or False.
#Your truth table should be commented out (as it's not valid Python code!)

# Problem of the day: (A AND B) OR (NOT B)

# (A AND B) Tells us that for AND to be True, both A AND B must be True.
#           if A is True AND B is False, then the answer is False (vice versa B/A).
# (NOT B)   Tells us that if B is True, then the opposite is False.
# OR        Tells us that if A OR B is True, the answer is True.

# A     B       (A AND B)   (NOT B)     (A AND B) OR (NOT B)
#-------------------------------------------------------
#True   True    True        False           True
#True   False   False       True            True
#False  True    False       False           False
#False  False   False       True            True


#2. The headlights of a car should only automatically turn on when the daylight outside is below a certain threshold.
#   If a sensor threshold is below the number 8, print "Headlights On"; otherwise, print "Headlights Off".

# if-else
#   If the daylight is below a sensor threshold of 8, turn on the headlights.
#   else, the "Headlight are Off"

sensor = 8
if sensor > 7.9:
    print("Headlights On")
else:
    print("Headlights Off")


#3. Prompt the user for their bank balance. Evaluate whether the balance is less than $100.
#   Print True if the user’s balance is below $100; print False, otherwise.

#   if-else
#   Prompt user for their bank balance
#   if the balance less than < $100, Print True if the balance is less than $100.
#   else if the balance is greater, print False

balance = float(input("Enter your current bank balance: $"))

if balance < 100:
    print(True)
else:
    print(False)


#4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, and tell them whether they can see G
#   (appropriate for under 13), PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.

# Ask the customer for their age.

print ("This theater restricts certain movie ratings, to the appropriate age classification of the customer.\nPG (appropriate for under 13), PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies. ")
age = int(input("How old are you? "))

# If the customer is younger then 13, they can only enter to watch PG rated movies.
if age < 13:
    print("You can only watch PG movies. ")

# elif The customer is between the ages of 13-17, they can enter and watch PG and PG-13 rated movies.
elif 13 <= age <= 17:
    print("You are allowed to watch PG and PG-13 movies. ")

# elif The customer is 18 years old, they can enter and watch G, PG-13, R rated movies.
elif age >= 18:
    print("Your old enough to make your own decision.")


#5. A store charges $5 for shipping on any order under $50. If the order amount is $50 or more, shipping is free.
#   Ask the user for the order total and print the total cost, including shipping.

# What was the total for the order
order_total = float(input("Enter the order total: $"))
# Cost to ship merchandise

# elif will the customer be charged for shipping
if order_total >= 50:
    shipping_cost = 0
    print ("You qualify for free shipping.")
elif order_total < 50:
    shipping_cost = 5.00
    print ("You will incur a $5.00 shipping fee.")

# Calculate the total cost including shipping
total_cost = order_total + shipping_cost

# Print the total cost
print(f"Total cost, including shipping: ${total_cost:.2f}")
