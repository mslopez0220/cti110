# CTI-110

# P4HW2 - Salary Calculator

# Marcelina Lopez

# July 5th, 2023

#

# Set variables
number_of_employee = 0     # holds total employees entered
total_overtime_pay = 0     # holds total over time pay for all employees
total_regular_pay = 0      # holds total regular pay for all employees
total_gross_pay = 0        # holds total gross pay for all employees

# Loop until user exits program
while True:
    
    # For each command, enter employee's name, hours worked, and pay rate
    name = input("Enter employee's name or \"Done\" to terminate: ")
    
    # Check if name is "Done", then break the loop
    if name == "Done":
        break
    else:
        
        # Correct name then increase employee count by 1
        number_of_employee+= 1
    
    hours = float(input("How many hours did " + name + " worked? "))
    rate = float(input("What is " + name + "\' pay rate? "))
    
    # Set variables to calculate values
    overtime = 0
    overtime_pay = 0
    regular_pay = 0
    gross_pay = 0
    
    # Check for overtime, if number of worked hours are greater than 40
    if hours > 40:
        
        # Calculate overtime
        overtime = hours - 40
        
        # Calculate over time Pay
        overtime_pay = overtime * rate * 1.5
        
        # Calculate regular pay
        regular_pay = 40*rate
        
        # Calculate gross pay
        gross_pay = regular_pay + overtime_pay
    else:
        
        # Calculate regular pay and gross pay
        regular_pay = hours*rate
        gross_pay = regular_pay
    
    # Add over time pay to total over time pay
    total_overtime_pay += overtime_pay
    
    # Add regular pay to total regular pay
    total_regular_pay += regular_pay
    
    # Add gross pay to total gross pay
    total_gross_pay += gross_pay
    
    # Print employee's name
    print("\nEmployee name: " + name + "\n")
    
    # Print the calculations
    print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format("Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay"))
    print("-------------------------------------------------------------------------------------------------------------")
    print("{:<20.1f}{:<20.1f}{:<20.1f}{:<20.2f}${:<19.2f}${:<20.2f}".format(hours, rate, overtime, overtime_pay, regular_pay, gross_pay))
    print()

# Loop terminates, print number of employees entered, total over time pay, total regular pay, and total gross pay
print()
print("Total number of employees entered:", number_of_employee)
print("Total amount paid for over time: $" + '{:.2f}'.format(total_overtime_pay))
print("Total amount paid for regular hours: $" + '{:.2f}'.format(total_regular_pay))
print("Total amount paid in gross: $" + '{:.2f}'.format(total_gross_pay))
