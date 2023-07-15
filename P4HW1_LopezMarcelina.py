# CTI-110

# P4HW1 - Score List

# Marcelina Lopez

# July 3rd, 2023

#


# Create an empty list
list_of_scores = []

# User input for number_of_scores
number_of_scores = int(input("How many scores do you want to enter? "))

# Current_number_of_scores to 0
current_number_of_scores = 0

# Looping until required number of scores are entered
while(True):
    
    # Looping for user input
    while(current_number_of_scores<number_of_scores):
        scores = float(input('Enter score #{}: '.format(current_number_of_scores+1)))
        
        # If score was invalid
        while(True):
            if(scores<0 or scores>100):
                print("\nINVALID Score entered!!!!\nScore should be between 0 and 100")
                scores = float(input('Enter score #{} again: '.format(current_number_of_scores+1)))
            
            # If valid score was entered    
            else:
                
                # Adding this to the list
                list_of_scores.append(scores)
                
                # Breaking out of the loop as a valid score was 
                # entered, no need for additional scores
                break
           
        # When a valid score was entered
        current_number_of_scores+=1 
        
        
    # If user entered all required number of valid scores
    if(current_number_of_scores==number_of_scores):
        # Breaking the loop no futher scores needed 
        break

# Computing lowest score
minimum = min(list_of_scores)

# Removing minimum score from the list
list_of_scores.remove(min(list_of_scores))

# Computing average score
average = sum(list_of_scores)/len(list_of_scores)

# Computing grade average
if(average>=90 and average<=100):
    grade = 'A'
    
elif(average>=80 and average<=89.9):
    grade = 'B'
        
elif(average>=70 and average<=79.9):
    grade = 'C'
    
elif(average>=60 and average<=69.9):
    grade = 'D'
        
elif(average<59.9):
    grade = 'F'

# Displaying Final Results
print("--------------------Results----------------------")
print("Lowest Score  :",minimum)
print("Modified List :",list_of_scores)
print("Scores Average:",average)
print("Grade         :",grade)
print("-------------------------------------------------")
