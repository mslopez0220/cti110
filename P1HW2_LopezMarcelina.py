#Travel Expense Calculation
#June 8, 2023
#CTI-110 P1HW2 - Travel Expense
#Marcelina Lopez
#

print("This program calculates and displays travel expenses")
budget=int(input("Enter your budget:"))#Enter their budget
destination=input("Enter your destination:")#Enter their destination
gas=int(input("Enter amount you will spend on gas:"))#Enter amount they will spend on gas
hotel=int(input("Enter amount you will spend on hotel accomodations:"))#Enter amount they will spend on hotel accomodations
food=int(input("Enter amount you will spend on food:"))#Enter amount they will spend on food
expenses=gas+hotel+food#Adding expenses
result=budget-expenses#Subtracting expenses from budget
print("Remaining balance after subtracting expenses from budget for your",destination,"trip is:",result)#printing the result





