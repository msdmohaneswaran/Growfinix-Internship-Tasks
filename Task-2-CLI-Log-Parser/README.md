# Growfinix Internship – Task 2
## CLI Log Parser for Tour Enquiries

### Project Overview

This project is developed as part of the Python Development Internship at Growfinix Technology.

The CLI Log Parser is a Python application that reads tour enquiry text files and extracts important customer information, including customer names, email addresses, and travel destinations.

It uses Regular Expressions (Regex) to identify and extract information from unstructured text.

### Objectives

- Read customer tour enquiries from a text file.
- Extract customer names.
- Identify and extract email addresses.
- Extract travel destinations.
- Display structured information in the terminal.
- Process files through a Command Line Interface.

### Technologies Used

- Python
- Regular Expressions (re)
- Argparse
- Visual Studio Code

### Project Structure

```text
Growfinix-Task2-CLI-Log-Parser/
│
├── main.py
├── tour_enquiries.txt
└── README.md
```

### Key Features

**1. Customer Name Extraction**
- Identifies customer names from enquiry messages.

**2. Email Extraction**
- Uses Regex patterns to identify email addresses.

**3. Destination Extraction**
- Extracts travel destinations from customer enquiries.

**4. File Processing**
- Reads multiple enquiries from a text file.
- Processes each enquiry separately.

**5. Command Line Interface**
- Accepts the input filename through command-line arguments.
- Uses argparse for command-line input.

### Installation

Install Python 3 on your system.

No external Python libraries are required because this project uses Python's built-in modules.

### How to Run

1. Download or clone this repository.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Run the following command:

```bash
python main.py tour_enquiries.txt
```

### Sample Output

```text
GROWFINIX - TOUR ENQUIRY LOG PARSER

Enquiry 1

Name        : Arun Kumar
Email       : arun@gmail.com
Destination : Ooty

TOTAL ENQUIRIES PROCESSED: 10
```

### Learning Outcomes

- Understanding Python Regular Expressions.
- Working with text files.
- Extracting structured information from unstructured text.
- Using Python functions.
- Implementing command-line arguments with argparse.
- Debugging Python applications.

### Internship Information

**Organization:** Growfinix Technology

**Domain:** Python Development

**Task:** Task 2 – CLI Log Parser for Tour Enquiries

### Conclusion

This project demonstrates how Python can automate the extraction of customer information from unstructured tour enquiry messages using Regular Expressions and command-line processing.

---

Developed as part of the Growfinix Python Development Internship.

