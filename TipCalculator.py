# Tip Calculator for Restaurants
#
#

print("Welcome to my tip calculator! Thank you for using it, Juan - ")

total = input("What was the total of your bill?  ")
totalTip = input ("How much percentage would you like to tip? ")
amountOfPeople = input("How many people are splitting the bill?  ")

calculation = ((float(total) / float(amountOfPeople)) *(1+ (float(totalTip) / 100)))
#print(round(calculation, 2))

finalCost = float(total) / float(amountOfPeople)
finalTip = calculation - finalCost
type(finalTip)
print(f"Thus everyone sharing the bill will pay ${round(finalCost,2)} plus a ${round(finalTip,2)} tip.")
