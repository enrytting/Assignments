# Elizabeth Rytting
# Homework 4

# Define the main
def main ():

    # Open the files
    firstfile, secondfile = open_files ()

    # Read the files
    readlines1, readlines2 = read (firstfile, secondfile)

    # Close the files
    close (firstfile, secondfile) 

    # Make all letters lowercase
    lowercase1, lowercase2 = lowercase (readlines1, readlines2)

    # Split the file
    word_1, word_2 = split_file(lowercase1, lowercase2)

    # Create two empty lists
    list_1, list_2 = empty (word_1, word_2)
    
    # Create sets
    set_one, set_two = create_sets (list_1, list_2) 

    # Determine what unique words are in both files
    unique (set_one, set_two) 

    # Determine what words are in the first file but not the second
    first_only (set_one, set_two)

    # Determine what words are in the second file but not the first
    second_only (set_one, set_two)

    # Determine what words are in the first or second file but not both
    or_not_both (set_one, set_two) 

# Open the files
def open_files (): 
    file1 = open ("first_file.txt", "r")
    file2 = open ("second_file.txt","r")
    return file1, file2

# Read the files
def read (file1, file2): 
    read_lines1 = file1.read ()
    read_lines2 = file2.read ()
    return read_lines1, read_lines2

# Close the files
def close (file1, file2):
    file1.close ()
    file2.close () 

# Make all of the letters lowercase to create truly unique words by
# making them all lowercase 
def lowercase (read_lines1, read_lines2):
    lower_case1 = read_lines1.lower ()
    lower_case2 = read_lines2.lower ()
    return lower_case1, lower_case2
    
# Split the file
def split_file (lower_case1, lower_case2):
    word1 = lower_case1.split ()
    word2 = lower_case2.split ()
    return word1, word2
    
# Create lists and append the words from the files to their lists
def empty (word1, word2):
    # Create two empty lists
    list1 = []
    list2 = []

    # Append to list
    for words in word1:
        list1.append (words.strip(",."))

    for words in word2:
        list2.append (words.strip(",."))
    return list1, list2 
        
# Create a set to create a unique list of words for both files
def create_sets (list1, list2): 
    set1 = set(list1)
    set2 = set(list2)

    # Display the sets
    print ("The unique words in file 1 are:")
    for word in set1:
        print (word)
    print ("\n")

    print ("The unique words in file 2 are:") 
    for word in set2:
        print (word)
    print ("\n")
    return set1, set2

# Determine what unique words are in both files
def unique (set1, set2):
    unique_words_both_files = set1.intersection(set2)

    # Print what unique words are in both files
    print ("The words that appear in both files are:") 
    for word in unique_words_both_files:
        print (word)
    print ("\n") 

# Determine what words are in the first file but not the second
def first_only (set1, set2): 
    first_not_second = set1.difference (set2)

    # Print what words are in the first file but not the second
    print ("The words that appear in the first file but not the second are:") 
    for word in first_not_second:
        print (word)
    print ("\n")

# Determine what words are in the second file but not the first
def second_only (set1, set2): 
    second_not_first = set2.difference (set1)

    # Print what words are in the second file but not the first
    print ("The words that appear in the second file but not the first are:")
    for word in second_not_first:
        print (word)
    print ("\n")

# Determine what words are in the first or second file but not both
def or_not_both (set1, set2): 
    first_or_second = set1.symmetric_difference(set2)

    # Print what words are in the first or second file but not both
    print ("The words that appear in either the first or second " \
           "set but not both are:")
    for word in first_or_second:
        print (word)

# Call the main
main ()
    
        
        
