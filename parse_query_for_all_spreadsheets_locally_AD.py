def account_parse():
    import pandas as pd #import pandas library for data manipulation

    # --- Load the file ---
    while True: #making the while loop true to keep asking for file path until valid file is provided
        file_path = input("Enter the path of the .xlsx or .csv file: ")
        file_path = file_path.replace("\\", "/")

        if not (file_path.endswith(".xlsx") or file_path.endswith(".csv")):
            print("Please provide a valid .xlsx or .csv file path.")
            continue #helps with continuing the loop if the file path is invalid

        try: #holding the the conditionals if the file is read correctly, and if not the exception is caught to say hey there is an error
            if file_path.endswith(".xlsx"): #checking to make sure the file ends with .xlsx or .csv
                data = pd.read_excel(file_path)
            else:
                data = pd.read_csv(file_path)

            print("File loaded successfully.")
            break

        except Exception as e:
            print(f"Error loading file: {e}")
            continue

    # --- Ask for the name to search ---
    search_name = input("Enter the full name to search for: ").lower() #here it asks the user for the full name of the user you want to get information about

    # --- Identify all text columns ---
    text_columns = [ #here I use a list to identify all text columns in the spreadsheet
        col for col in data.columns #col means column and using data.columns which is appended to the pandas dataframe to get all the columns in the spreadsheet
        if data[col].dtype == "object" or data[col].dtype == "string" #checking the data type in each column if it is an object or string
    ]

    if not text_columns:
        print("No text columns found in this spreadsheet.")
        return

    print(f"Searching in text columns: {text_columns}")

    # --- Search for the name in ANY text column ---
    matches = pd.DataFrame() #creating an empty dataframe to store matches

    for col in text_columns: #for looping through each text column
        try:
            col_matches = data[data[col].astype(str).str.lower() == search_name]
            matches = pd.concat([matches, col_matches])
        except Exception:
            continue

    # --- Remove duplicates if found in multiple columns ---
    matches = matches.drop_duplicates()

    # --- Output results ---
    if matches.empty:
        print(f"No user found matching '{search_name}'.")
    else:
        print("\nUser details found:\n")
        print(matches.to_string(index=False))
        
account_parse() #calling the function to run the code