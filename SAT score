# Elizabeth Rytting
# Homework 2

# Prompt the user to enter their Critical Reading Test Score
critical_reading = int (input ("Critical Reading SAT score, or enter '-1' to end:"))

# Continue processing as long as user does not enter done
while critical_reading != -1: 

    # Prompt the user to enter their Mathmatics score
    math = int (input ("Math SAT score:")) 

    # Prompt the user to enter their Writing SAT score
    writing = int (input ("Writing SAT score:"))

    # Prompt the user to enter their rank in their graduating class
    rank = int (input ("Rank in graduating class:")) 

    # Prompt the user to enter the number of students in their graduating class
    total_students = int (input ("Total number of students in graduating class:"))
   
 # (1) Create if/elif statements for if an impossible number is submitted
    if critical_reading < 200 or math < 200 or writing < 200:
        print ("Reject")
    elif critical_reading > 800 or math > 800 or writing > 800:
        print ("Reject")
    elif rank < 1:
        print ("Reject") 
    
    # (2) Create elif statement for if any test score is 800, applicant is accepted
    elif critical_reading == 800 or math == 800 or writing == 800:
        print ("Accept") 

    # (3) Create an elif statement for if any test score is below 300, applicant
    # is rejected
    elif critical_reading < 300 or math <300  or writing < 300:
        print ("Reject")

    # (4) Create an elif statement for if any test score is above 650 and top quarter
    # of graduating class
    elif (critical_reading + math +  writing)/3 > 650 and (rank/total_students) <= (1/4):
         print ("Accept")

    # (5) Create an elif statement for if any two scores are below 400 or applicant
    # is in the bottom quarter of graduating calss
    elif critical_reading < 400 and math < 400 or critical_reading < 400 and writing < 400 or\
        writing < 400 and math < 400 or (rank/total_students) >= (3/4):
        print ("Reject")

    # (6) Create an else statement for if the applicant is put on the waiting list
    else:
        print ("Waitlist")

    # Prompt the user for the next Critical Reading SAT score:
    critical_reading = int (input ("Critical Reading SAT score, or enter '-1' to end:"))    


    
