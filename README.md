# Parse-and-look-up-script
Spreadsheet Identity & AD Lookup Tools
This repository contains two Python-based automation scripts for parsing .xlsx and .csv files. These tools are designed to streamline the process of checking local flat-file exports (such as Active Directory or EntraID reports) for specific user details.

Features
Local Execution: Runs entirely on your Windows machine.

Format Support: Handles both Excel (.xlsx) and Comma-Separated Values (.csv) formats.

Efficiency: Eliminates the need to open heavy Excel files to find a single user.

Automation: Uses pandas for high-speed data parsing and filtering.

The Scripts
1. Specific Spreadsheet Inspector (parse_query_for_my_own_spreadsheet.py)
This script is a tailored example of how to interact with a known data structure. It is optimized for a specific employee directory format.

Best Use Case: When you have a standard internal directory and need to pull specific fields (User ID, Job Title, RBAC/IAM info) for a person.

How it works: * It validates the file path.

It specifically looks for a Full Name column.

It returns a formatted view of that user's specific identity and role attributes.

2. Universal AD/EntraID Parser (parse_query_for_all_spreadsheets_locally_AD.py)
A more robust and flexible tool designed for general administrative use. It is "column-agnostic," meaning it can search for a user even if you don't know exactly which column their name is in.

Best Use Case: Verifying if a user exists in an Active Directory export or EntraID flat-file where column names might vary.

How it works:

It scans the entire spreadsheet for all "text" based columns.

It performs a case-insensitive search across every column simultaneously.

If a match is found anywhere in the row, it displays the full record for that user.

Prerequisites
To run these scripts, you must have Python installed along with the pandas and openpyxl libraries.

Bash
pip install pandas openpyxl
Usage
Launch the script:

Bash
python parse_query_for_all_spreadsheets_locally_AD.py
Enter File Path: When prompted, paste the full path to your .csv or .xlsx file. (Note: The scripts are designed to handle Windows backslashes \ automatically).

Search: Enter the full name of the individual you are looking for.

View Results: The script will output the user's details directly in the terminal or notify you if no match was found.

Technical Details
Error Handling: Both scripts include try-except blocks to prevent crashes if a file is locked or the path is typed incorrectly.

Recursion & Loops: The scripts use while loops to ensure the user can retry a file path without the script ending.

Memory Efficiency: By using pandas, the scripts can search through thousands of rows in milliseconds, significantly faster than manual filtering in Excel.
