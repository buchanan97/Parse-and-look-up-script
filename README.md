# **📊 User Lookup & Identity Automation**

This repository contains Python utilities designed to efficiently parse Active Directory (AD) and Entra ID flat files. These scripts allow you to instantly locate user identities, IAM roles, and RBAC information without the manual effort of opening massive `.csv` or `.xlsx` exports in Excel.

---

## **⚡ Why Use This?**

* **Speed:** Locate users in milliseconds using pure Python.
* **Efficiency:** Avoid the "Excel lag" associated with massive identity exports.
* **Flexibility:** Search across all columns or target specific data structures.
* **Local & Secure:** All parsing happens on your machine; no data is uploaded or transmitted.

---

## **📁 Repository Structure**

| File | Description |
| :--- | :--- |
| `parse_query_for_all_spreadsheets_locally_AD.py` | **Universal AD Parser:** Scans every text column for a match. Ideal for inconsistent headers like Name or DisplayName. |
| `parse_query_for_my_own_spreadsheet.py` | **Directory Inspector:** Targeted lookup for consistent layouts. Extracts specific fields like User ID, Job Title, and RBAC info. |

---

## **🧩 Requirements**

* **Python 3.8+**
* **Pandas:** `pip install pandas`
* **Openpyxl:** `pip install openpyxl`

---

## **🚀 Usage**

### **1. Run a Lookup Script**
```bash
python parse_query_for_all_spreadsheets_locally_AD.py
