# Email Extractor

 This project extracts all email addresses from a text file using **Regular Expressions (Regex)** and saves them into a separate file.

# Project Description

The Email Extractor automates the process of finding email addresses from a text file. It reads the content of an input file, identifies valid email addresses using Python's `re` module, displays them on the console, and stores them in an output text file.


# Features

- Extracts all valid email addresses from a text file
- Uses Regular Expressions (Regex)
- Displays extracted emails on the console
- Saves extracted emails to a new text file
- Simple and easy-to-use automation script

# Technologies Used

- Python 3
- Regular Expressions (`re` module)
- File Handling

# Project Structure

```
CodeAlpha_EmailExtractor/
│
├── email_extractor.py
├── input.txt
├── extracted_emails.txt
└── README.md
```

# How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Place your email data inside `input.txt`.
4. Open a terminal in the project folder.
5. Run the script:

```bash
python email_extractor.py
```

# Sample Input (`input.txt`)

```
Hello,

Please contact us at support@gmail.com

For business queries:
info@company.com

HR Department:
hr@company.org
```

# Sample Output

```
========================================
Extracted Email Addresses
========================================

support@gmail.com
info@company.com
hr@company.org

Emails have been saved to extracted_emails.txt
```

# Output File (`extracted_emails.txt`)

```
support@gmail.com
info@company.com
hr@company.org
```

# Python Concepts Used

- Regular Expressions (`re`)
- File Handling
- Input/Output
- String Process

# Author

**Your Name**

GitHub: https://github.com/Somkant07

LinkedIn: https://www.linkedin.com/in/somkant-sharma
