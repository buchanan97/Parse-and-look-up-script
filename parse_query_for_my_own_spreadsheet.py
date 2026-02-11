#Here i am creating a toolautomation that can parse through a excel file and extract specific data based on user-defined criteria.
#the first code i created has erros but the second shows a difference in correcrting recursion.
# This scriptg has errors, the indentation is off by the else conditonal, it only works if the file path is invalid.
#leading to a recursion error if the file path is valid, and it does not ask for the column name to search for, and it does not print the user data if the column name is found in the spreadsheet.
#1st code with errors
#  def account_parse():
#     import pandas as pd
#     file_path = input("Enter the path in which you want to parse the data for account lookup: ")
#     if file_path.endswith('.xlsx') or file_path.endswith('.csv'):
#         try:
#             if file_path.endswith('.xlsx'):
#                 data = pd.read_excel(file_path)
#             elif file_path.endswith('.csv'):
#                 data = pd.read_csv(file_path)
#             print("File loaded successfully.")
#         except Exception as e:
#             print(f"Error loading file, must be csv, or xlsx: {e}")
#             account_parse()
#     else:
#         print("Please provide a valid .xlsx or .csv file path.")
#         account_parse()
#         column_name = input("Enter the name of the user you want to inspect for account details: ")
#         spreadsheet = file_path.split('/')[-1]  # Get the file name from the path
#         if column_name in spreadsheet.columns:
#             user_data = data[column_name]
#             print(f"Data for {column_name}:")
#             print(user_data)       
#         else:
#             print(f"Column '{column_name}' not found in the spreadsheet.")
# account_parse()


#for example here is a list of full names in my spreadsheet parse_query_for_my_own_spreadsheet.xlsx that I want to be able to search for and get the user data for, and this is the data that I want to be able to parse through and get the user data for based on the full name of the user in the spreadsheet.
#Alice Vance
# Bob Miller
# Charlie Day
# Diana Prince
# Edward Norton
# Fiona Gallagher
# George Costanza
# Hannah Abbott
# Ian Wright
# Julia Louis
# Kevin Hart
# Laura Palmer
# Michael Scott
# Nina Simone
# Oscar Martinez
# Pam Beesly
# Quentin Tarantino
# Rosa Diaz
# Stanley Hudson
# Toby Flenderson
# Ursula K. Le Guin
# Victor Von Doom
# Wanda Maximoff
# Xavier Charles
# Yara Greyjoy
# Zane Grey
# Amy Pond
# Ben Solo
# Clara Oswald
# Donna Noble
# Eleven Hopper
# Finn Mertens
# Gwen Stacy
# Hal Jordan
# Iris West
# Jake Peralta
# Kate Bishop
# Luke Cage
# Matt Murdock
# Natasha Romanoff
# Oliver Queen
# Peter Parker
# Quinn Fabray
# Reed Richards
# Sam Wilson
# Tony Stark
# Ulysses Klaue
# Vision A.I.
# Wade Wilson
# Zelda Hyrule
# corrected code with the errors fixed, and the code is now able to ask for the column name to search for, and it will print the user data if the column name is found in the spreadsheet, and it will also handle the file path input correctly without causing a recursion error.
def account_parse(): #setting up the function for the script to run
    import pandas as pd #importing the pandas library for data manipulation

    while True:
        file_path = input("Enter the path of the .xlsx or .csv file: ")

        # Normalize Windows paths
        file_path = file_path.replace('\\', '/') #windows uses backslashes for file paths, but pandas can handle forward slashes, so we replace them to avoid issues

        if not (file_path.endswith('.xlsx') or file_path.endswith('.csv')): #using the comparison operator to check if the file path ends with .xlsx or .csv, if it does not then it will print an error message and continue the loop to ask for the file path again
            print("Please provide a valid .xlsx or .csv file path.")
            continue

        try: #using the try and except block to handle any errors that may occur when trying to read the file, if there is an error it will print the error message and continue the loop to ask for the file path again
            if file_path.endswith('.xlsx'):
                data = pd.read_excel(file_path)
            else:
                data = pd.read_csv(file_path)

            print("File loaded successfully.") #if the file is loaded successfully it will print this message and break out of the loop to continue with the rest of the code
            break

        except Exception as e:
            print(f"Error loading file: {e}")
            continue #if there is an error loading the file, it will print the error message and continue the loop to ask for the file path again

    # Show available columns
    print(f"Available columns: {list(data.columns)}") #showing the available columns in the spreadsheet to the user so they know what columns they can search for

    # Ask for the user's full name
    full_name = input("Enter the full name you want to inspect: ").lower()

    # Case-insensitive match
    if 'Full Name' not in data.columns:
        print("The spreadsheet does not contain a 'Full Name' column.") 
        return #if the spreadsheet does not contain a 'Full Name' column, it will print this message and return to the main menu

    matches = data[data['Full Name'].str.lower() == full_name]

    if matches.empty:
        print(f"No user found with the name '{full_name}'.")
    else:
        print("\nUser details:")
        print(matches[['User ID', 'Full Name', 'Background', 'Job Title',
                       'Phone Number', 'Roles', 'RBAC / IAM Information']])
account_parse()