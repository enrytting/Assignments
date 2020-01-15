# Import datetime will allow us to determine the current time
# This will be used in the reciept and in the transaction ID number 
import datetime

# Import sqlite3 allows us to create a database and manipulate
# and update the database 
import sqlite3

# Import pickle allows us to unpickle our online orders 
import pickle

# * * * * * Create Menu * * * * *
# Create sale menu option
# If the user enters one, the process will begin to create a new sale
# which inclues asking the user for the item UPCs for the customer's purchases
# and will later calculate the total of the purchase
CREATE_SALE = 1

# Retrieve online orders menu option
# Will unpickle a binary file for the online order
RETRIEVE_ONLINE_ORDER = 2

# Update catalog menu option
# Will update the table in the database with new items if the
# store owner chooses to stock more items than they currently have
UPDATE_CATALOG = 3

# Quit menu option
# Will quit the program when the store clerk is done 
QUIT = 4

# Define the main function
# Will call the subsequent functions created
# Will hold the while loop that will call different functions based on
# what menu item the clerk selects 
def main ():

    # Create accumulator variable for the choiuce the user selects
    # from the main menu 
    choice = 0

    # Create an accumulator variable to be used for the transaction ID number
    # The count will begin at 1 because if not, the first transaction would be
    # considered transaction 0 
    count = 1
    
    # Create a while loop
    # If the user's choice is quit it will exit the program 
    while choice != QUIT:

        # Display the menu for the user to see
        display_menu()

        # Create a try-except-else statment to handle exceptions 
        try: 

            # The user will enter their menu selection
            choice = int(input("\nEnter your choice: "))

            # If the user enters the number 1 they will be prompted to
            # create a sale 
            if choice == CREATE_SALE:

                # Call the create_id fuction       
                # Will create a new transaction ID number each time the user
                # indicates that they want to record a new sale
                # The argument count is passed in to record the proper transaction number
                # The newid variable catches the return of the transaction ID number
                # from the create ID function
                newid = create_id(count)

                # Call the new_transaction function
                # Will prompt the user to enter UPC numbers which will create
                # a list of UPC's to be returned
                # The newid variable must be passed in to know what the transaction ID
                # number is 
                list_of_UPCs = new_transaction(newid)

                # Add 1 to the accumulator variable
                # This will give the new transaction a new transaction ID number 
                count +=1

            # If the user enters the number 2 they will be prompted to
            # retrieve an online order 
            elif choice == RETRIEVE_ONLINE_ORDER:

                # Call the online order function 
                retrieve_online() 

            # If the user enters the numer 3 they will be prompted to update the
            # database table, often referred to here as a catalog 
            elif choice == UPDATE_CATALOG:

                # Call the update catalog function
                update_catalog ()

            # If the user enters the number 4 they will exit the program
            elif choice == QUIT:
                print ("Exiting the program...")

            # If the user enters a number greater than 4 they will be prompted to
            # enter a valid menu option
            else:
                print ("Please enter a valid menu choice.")
                 
        # Create an exception handler that will display if the
        # user does not enter their menu choice as an integer
        except ValueError:
            print ("Please enter your menu choice as an integer." )

# Define the display_menu function
# The function will display the menu items 
def display_menu ():
    print ("* * * * * MENU * * * * *\n"
           "1) Create Sale\n"\
           "2) Retrieve Online Order\n"\
           "3) Update Catalog\n"
           "4) Quit")

# Define the date function
# The function will give us the current date and time of the transaction
# to be listed on the reciept 
def date ():

    # The d variable is the year, month, date, and time
    # Will split these since we do not want all of that information
    # on the reciept 
    d = datetime.datetime.today()

    # The month variable is the current month 
    month = str(d.month)

    # The day variable is the current day 
    day = str(d.day)

    # The year variable is the current year 
    year = str(d.year)

    # Return the month, day, and year which is what we want in our reciept 
    return month + day + year

# Define the create_id function
# Accepts the parameter the_count which gives the transaction number count 
def create_id (the_count):

    # Call the date function to be used in the reciept 
    today = date()

    # The newID variable combines the date and the number transaction it is
    # to create a unique transaction identification number 
    newID = today + "-" +str(the_count)

    # Return the newID variable to be used in other function 
    return newID
    
# Define the new_transaction function
# The new_transaction function has to accept the idnum (transaction
# identification number) as a parameter to conintue to make sure that the
# transaction identification number is unique 
def new_transaction (idnum):


    # Create a connection that represents the database
    conn = sqlite3.connect('ourproject2.db')

    # Create a cursor object s othat methods can be performed on it 
    c= conn.cursor()

    # Print New Sale as a header 
    print ("\n* * * * * New Sale * * * * *")

    # Create an empty UPC list 
    upc_list = []

    # Create an infinite loop that will break only when the data input is valid 
    while True: 
        
        # Create a try-except-else statement that will catch exceptions if the user
        # does not enter a valid UPC number
        try:

            # Prompt the user to enter an item UPC number 
            upc_number = int(input("Enter the UPC number for the item or enter 0" \
                            " when finished: "))
            
            # Create a sentinel that will prompt the user for another UPC number
            # if they do not enter 0 indicating they want to end the loop 
            while upc_number !=0:

                # Create if statement for if the user enters an invalid UPC number
                # If they enter a valud UPC (11 or 12 digits in number) they will
                # be prompted to contintue entering UPC's
                if len(str(upc_number)) == 11 or len(str(upc_number)) == 12:

                    upc_list.append(upc_number) 

                    # Prompt the user to enter a UPC number 
                    upc_number = int(input("Enter the UPC number for the item or enter 0" \
                                        " when finished: "))
                
                # If the user does not enter a valid UPC the UPC they entered will not be
                # appended to the UPC list and they will be given instrustions on where
                # to find a valid UPC
                else:
                    print ("Please enter a valid UPC number, the UPC number" \
                            " can be found directly below the barcode on the item" \
                            " and should be 11 or 12 integers in length.\n")
                
                    upc_number = int(input("Enter the UPC number for the item or enter 0" \
                                        " when finished: "))

        # Create an except statement that will display a message for the user if
        # they enter commas or spaces between the numbers 
        except ValueError:
            print ("Please enter a UPC in integers without any spaces or other" \
                       " seperators between the numbers.\n")

            
        # Once the data is validated and there are no other errors move on to
        # the next required user input
        else:
            break

    # Call the retrieve price funcion
    price_list = retrieve_price(upc_list)
        
    # Call the retrieve description function
    description_list = retrieve_description(upc_list)

    # Call the calculate_reciept function
    prices = calculate_receipt(price_list)
        
    # Ask clerk if they'd like a receipt for the customer
    receipt_prompt = input("Enter yes to write receipt or no to skip this step: " )

    # If the clerk enters yes, then call write_receipt function 
    if receipt_prompt == 'yes':
        write_receipt(idnum, upc_list, prices)
    elif receipt_prompt == 'no':
        print("End of transaction", idnum, "\n")

    # Commit the changes
    conn.commit()

    # Close the connection to the database
    conn.close()

    # Return the list of UPC numbers 
    return upc_list
    
        
# Define the retrieve_price function
# The function will retrieve the price for each item in the database that the
# customer purchases
def retrieve_price(list_UPC):

    # Create a connection object that represents the database
    conn = sqlite3.connect('ourproject2.db')
    # Create a cursor object to perform methods using SQL commands
    c = conn.cursor()

    # Create an empty list in order to add the prices to it later 
    price_list = []
    
    # Create a for loop to get data on a single UPC
    for item in range(len(list_UPC)):

        # Get one item of the UPC list by indexing beginning with the first item
        one_UPC = list_UPC[item]

        # Take each UPC and put it into a tuple 
        upc_tuple = (one_UPC,)

        # Select the row from the table where the UPC is found 
        c.execute('SELECT * FROM goods WHERE UPC=?', upc_tuple)

        # Fetch the row in order to get the databse 
        row = c.fetchone()
        

        # In the row, get the third index which is the price
        price = row[2]

        # Append the price from each item into the list so they can be
        # used to calculate the total later 
        price_list.append(price)
    
    
    # Commit the changes 
    conn.commit()

    # Close the connection after the changes have been committed
    # With a higher tech company continuing to open, commit, and close
    # would use too much overhead 
    conn.close()
    
    # Return the price list
    # Will be used later to calculate the subtotal, tax, and grand total 
    return price_list

# Define the retrive_price function
# The function will retrieve the description for each item in the database that the
# customer purchases 
def retrieve_description(list_UPC1):

    # Create a connection object that represents the database
    conn = sqlite3.connect('ourproject2.db')

    # Create a cursor object to perform methods using SQL commands
    c= conn.cursor()

    # Create an empty list in order to add the item descriptions to it later 
    description_list = []

    # Create a for loop to get data on a single UPC
    for item in range(len(list_UPC1)):

        # Get one item of the UPC list by indexing beginning with the first item
        one_UPC = list_UPC1[item]

        # Take each UPC and put it into a tuple
        upc_tuple = (one_UPC,)

        # Select the row from the table where the UPC is found
        c.execute('SELECT * FROM goods WHERE UPC=?', upc_tuple)

        # Fetch the row in order to get the databse 
        row = (c.fetchone())

        # In the row, get the third index which is the price
        price = row[1]
        
        # Append the description from each item into the list so they can be
        # used in the reciept if the customer requests one 
        description_list.append(price)
    
    # Commit the changes 
    conn.commit()

    # Close the connection after the changes have been committed
    # With a higher tech company continuing to open, commit, and close would
    # use too much overhead 
    conn.close()
    
    # Return the price list
    # Will be used later to calculate the subtotal, tax, and grand total 
    return description_list

# Define the calculate receipt function
# The function will calculate the subtotal, tax, and grand total to display on the receipt
def calculate_receipt (price_list1):

    # Create an accumulator variable to determine the subtotal of the
    # items purchased by the customer
    subtotal = 0.00

    # Use a loop to add the accumulator variable to the price of the
    # previous item
    for price in price_list1:
        subtotal+= price

    # Format the subtotal so it is clear that it is monetary
    subtotal_format = format(subtotal, ',.2f')

    # Create a global constant for the total tax, 8%
    TAX_AMT = 0.08

    # Multiply the subtotal by the tax amount
    tax = subtotal*TAX_AMT

    # Format the tax so it is clear that it is monetary
    tax_format = format(tax, ',.2f')

    # Calculate the grand total but adding the subtotal to the tax
    grand_total = subtotal + tax

    # Format the grand total so it is clear that it is monetary
    grand_total_format = format(grand_total, ',.2f')

    # Return the subtotal, tax, and grand total
    return ("Subtotal: $ "+ subtotal_format, "Tax: $" + tax_format,"Grand total: $"+ grand_total_format)


# Define the write receipt function
# The function will create a receipt with the transaction time, date, ID number,
# subtotal, tax, and total
def write_receipt(name,list_UPC, price_list):
    
    # Create a SQLITE3 connection object
    conn = sqlite3.connect('ourproject2.db')
    
    # Create a cursor to preform methods
    c= conn.cursor()
    
    # Open a file to write a receipt the name of the file will be
    # passed to this function as the orderID
    receipt = open(name, "w")

    # For each item in the list of items purchased, iterate through each item
    for item in range(len(list_UPC)):
        
        # Get the item from the list
        each_UPC = list_UPC[item]

        #For each upc create a tuple with the individual UPC value  
        upc= (each_UPC,)
        
        # Once you have one UPC from the list, use SQLITE3    
        c.execute('SELECT * FROM goods WHERE UPC=?', upc)
        
        # Get the row from our goods table from the database
        row = c.fetchone()
        
        # Write each row to the receipt file
        # each row will have the UPC, description and price
        receipt.write(str(row))
        
        # Go to next line before writing another upc, description and price
        receipt.write("\n")
        
    # Add a dotted line to seperate rows from pricing information 
    receipt.write("---------------------------")
    
    # Skip line before writing price information
    receipt.write("\n")
    
    
    for total in range(len(price_list)):
        # Each individual price becomes a value
        value = price_list[total]
        
        # Write subtotal, tax and total to the receipt
        receipt.write(str(value))
        
        # Skip line to do the same to other items
        receipt.write("\n")
        
    # Close the file
    receipt.close()

    # Close the connection
    conn.close()

# Define the retrieve online function
# The function will retrieve online orders from a binary file
def retrieve_online ():

    # Create an infinite loop that will break only when the data input is valid 
    while True: 

        # Create an exception handler
        try:

            # Prompt the user to enter the name of the online order file
            a_file = input("Enter name of online order file: ")
    
            # Open a binary file that contains the online orders
            # Be able to read the binary
            pickled_file= open(a_file, 'rb')

            # To unpickle the file use the pickle load method
            unpickled = pickle.load(pickled_file)

            # Ask if they want to see the contents of the file
            file_contents = input ("Enter 'yes' if you would like to see" \
                               " the contents of the file: ")

            # If the user wants to print print the contents of the file
            if file_contents == "yes":
                print (unpickled)

        # If the user enters an invalid file name create an except statement to
        # catch the error
        except IOError:

            print ("The file was not found.\n")

        # If no exceptions are caught break from the infinite loop 
        else:
            break
    
    # Return unpickled content of online order
    return unpickled
    

# Define the update catalog function
# The function will update the item catalog when the owner of the store adds new
# items to the store
def update_catalog ():

    # Print the update catalog header
    print ("\n* * * * * UPDATE CATLOG * * * * *")

    # Create the connection object that represents the database 
    conn = sqlite3.connect ("ourproject2.db")

    # Create a cursor so that actions can be performed on the database
    c = conn.cursor()

    # Create a list to hold the new items price, description, and UPC number
    # A list must be created since the execute statement only takes 2 arguments
    update_catalog_list = []

    # Prime the while loop
    keep_going = "yes"

    # Enter the while loop that will ask the user for the item UPC,
    # price, and description
    while keep_going == "yes":

        # Create an infinite loop that will break only when the data input is valid 
        while True:

            # Create a try statement that will be used to check for value errors
            try: 

                # Prompt the user for the UPC number they want to add to the catalog
                upc_number = int(input("Enter the UPC for the item you want to" \
                                       " insert into the catalog: "))

                # Ensure that the length of the UPC entered is either 11 or 12 digits 
                while len(str(upc_number)) != 12 and len(str(upc_number)) != 11:

                    # If the length is not 11 or 12 digits, inform the user that
                    # the UPC number is not valid
                    print ("Please enter a valid UPC number, the UPC number" \
                           " can be found directly below the barcode on the item" \
                           " and should be 11 or 12 integers in length.\n")

                    # Prompt the user again to enter a valid UPC number
                    upc_number = int(input("Enter the UPC for the item you want to" \
                                        " insert into the catalog: "))
                    
                # If the data is valid, append the number to list
                update_catalog_list.append(upc_number)

            # Create an except statement to catch all value errors
            except ValueError:
                print ("Please enter the UPC number as an integer.\n")

            # Once the data is validated and there are no other errors move on to
            # the next required user input
            else:
                break

        # Prompt the user for the description of the product
        description = input("\nEnter the description for the item you want to" \
                            " insert into the catalog: ")

        # Create a loop that will check to see if the description of the item is less
        # than two characters
        while len(description) < 2:

            # Inform the user that the description of the item is too short and
            # they need to enter a longer description
            print ("Please enter a longer description for the item.\n")

            # Prompt the user to re-enter the description
            description = input("Enter the description for the item you want to" \
                                " insert into the catalog: ")

        # Create a loop that will check to see if the description of the item
        # is more than 50 characters
        while len(description) > 50:

            # Inform the user that the description of the item is too long
            # and they need to enter a shorter description
            print ("Please enter a shorter description for the item.\n")

            # Prompt the user to re-enter the description 
            description = input("Enter the description for the item you want to" \
                                " insert into the catalog: ")

        # If there are no errors in the input data append the description
        # to the list
        update_catalog_list.append (description)

        # Create an infinite loop that will only break if all the data entered
        # by the user is valid
        while True:

            # Create a try statement that will be used to check for
            # value errors
            try: 

                # Prompt the user for the price of the item
                price = float(input ("\nEnter the price for the item you want to" \
                           " insert into the catalog: $"))


                # When the price is less and a cent or greater than 30 dollars enter
                # a loop that will inform the user that it is an invalid price
                # The store will not sell any items that are free or any items
                # over  dollars therefore if either of these prices were entered
                # it was a mistake
                while price < .01 or price > 30:

                    # Inform the user that their price not valid 
                    print ("The number you have entered is not a valid price. Please enter" \
                            " a valid item price.\n") 

                    # Prompt the user to re-enter the price
                    price = float(input ("Enter the price for the item you want to add" \
                                       " insert into the catalog: $"))

                # If there are no flaws in the input append the price to the lsit 
                update_catalog_list.append (price)

            # Create an except statement to catch the value errors
            except ValueError:
                print ("Please enter the price in the format: XX.XX\n")

            # Once the data is validated and there are no other errors move on to
            # the next required user input
            else:
                break

        # Insert the values into the catalog 
        c.execute("INSERT INTO goods VALUES (?,?,?)", update_catalog_list)

        # Create a variable that will allow the user to enter the database
        keep_going = input ("If you would like to add another item into the catalog" \
                            " enter 'yes': ")
        # Commit the changes 
        conn.commit ()

    # Close the connection to the database
    conn.close ()
    
# Call the main function 
main ()
