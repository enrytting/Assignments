# Elizabeth Rytting
# Homework 3

# Define the main
def main ():
    # Open the files, return the file objects 
    correct, students1 = open_files ()

    # Create 3 empty lists to later append, return the name of the lists
    right, answer, wrong = create_lists ()

    # Append the right answers and the student answers to the list created above
    right_ans, student_ans = append_answers (correct, students1, right, answer)

    # Close the files, passing in the file object names 
    close_files (correct,students1)

    # Create a loop that compares the answer the student gave to
    # the correct answer in the key
    correct1, incorrect, incorrect_answer = loop (right,answer,wrong)

    # Print the score for the test, the number of incorrect answers, number of
    # correct answers, and what question numbers were incorrect 
    score (correct1, incorrect, incorrect_answer) 

def open_files ():
    
    # Open the correct answer file
    correct_answers = open ("answers.txt", "r")

    # Open the students file
    students = open ("student_answers.txt", "r")

    return correct_answers, students
    
def create_lists (): 

    # Create a list for the correct answers 
    right_answers = []

    # Create a list for the students answers
    answer_student = [] 

    # Create a list for the wrong answers
    wrong_answer = []

    return right_answers, answer_student, wrong_answer


def append_answers (correct_answers, students, right_answers, answer_student): 
    
    # Append the correct answers into the list
    for line in correct_answers:
        right_answers.append (line)

    # Append the student's answers into the list
    for line in students:
        answer_student.append (line)

    return right_answers, answer_student


def close_files (correct_answers,students):

    # Close the files
    correct_answers.close()
    students.close()
    

def loop (right_answers, answer_student, wrong_answer): 

    # Initialize accumulator variables 
    right = 0
    wrong = 0

    for count in range (len(right_answers)):
        if right_answers [count] == answer_student [count]:
            right+=1
        else:
            wrong+=1
            wrong_answer.append (count+1)
            
    return right, wrong, wrong_answer


def score (right, wrong, wrong_answer): 
    # Determine if the student passed or failed the test
 
    if right > 18:
        print ("The student passed the test.")
    else:
        print ("The student failed the test.")

    # Display the total number of correct answers
    print ("The student got", right, "answers correct.")

    # Display the number incorrect questions
    print ("The student got", wrong, "answers wrong.")

    # Display which questions were incorrect
    print ("The following numbers were incorrect:") 
    for line in wrong_answer:
        print ("Number", line)


# Call the main
main () 
