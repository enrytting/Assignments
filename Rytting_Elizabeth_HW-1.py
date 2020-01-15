# Elizabeth Rytting
# Homework 1

# Display the welcome text message
print ("This program will calcuate your Body Mass Index")

# Prompt the user for their name
name = input ("Hello, what is your name?:")

# Prompt the user to enter their weight in pounds
weight = float (input ("Please enter your weight in pounds:"))

# Prompt the user to enter their height in feet
height_feet = int (input ("Please enter your height in feet, whole numbers only:"))

# Prompt the user to enter their height in inches
height_inches = float (input ("...and how many inches on top of that?:"))

# Convert the users height into only inches
total_height_in_inches = (height_feet*12) + height_inches

# Calculate BMI
BMI = weight*703/(total_height_in_inches)**2

# Display BMI
print ("Hello ", name, ", Your BMI is ", format (BMI, '.1f'), ", Would you like fries with that?", sep = '')

# Prompt the user to close the window
choice = input ("Please press any key to close the window.") 

