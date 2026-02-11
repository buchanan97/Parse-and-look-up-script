📊 User Lookup & Identity Automation
Efficiently parse Active Directory and Entra ID flat files without ever opening Excel.

⚡ Why Use This?
Manually searching through massive .csv or .xlsx exports from Active Directory or Entra ID is slow, error‑prone, and often causes the dreaded Excel lag.
These Python utilities provide a lightweight, command‑line interface to instantly locate:

User identities

IAM roles

RBAC information

All in milliseconds, using pure Python.

🛠️ Installation & Setup
Clone the repository or download the scripts.

Install dependencies:

bash
pip install pandas openpyxl
🚀 The Toolkit
🔍 1. Universal AD Parser
Filename: parse_query_for_all_spreadsheets_locally_AD.py

Your Swiss Army Knife for identity lookups.
It doesn’t care how your spreadsheet is structured — it will find the user wherever they’re hiding.

Logic: Scans every text column for a match

Best for: Unknown or inconsistent column headers (Name, FullName, DisplayName, etc.)

Feature: Automatically converts Windows file paths for Python compatibility

📋 2. Directory Inspector (Template)
Filename: parse_query_for_my_own_spreadsheet.py

A specialized script designed for a consistent, predictable export format.

Logic: Targets a specific Full Name column

Best for: Recurring tasks with the same spreadsheet layout

Output: Structured data including

User ID

Job Title

RBAC / IAM Information

📖 Usage Guide
Running the tools is simple — just follow the interactive prompts.

Step	Action	Description
1	python script_name.py	Launch the desired tool
2	Provide Path	Paste the full path to your .xlsx or .csv file
3	Search Name	Enter the full name (case‑insensitive)
4	Review	View the matched row directly in your console
🛡️ Technical Overview
Data Engine: Powered by pandas for fast, efficient filtering

Path Handling: Automatically converts \ → / to avoid Windows path issues

Safety: Built‑in exception handling prevents crashes on invalid or locked files

Note: These scripts run locally only. No data is uploaded or transmitted. All parsing happens on your machine.
