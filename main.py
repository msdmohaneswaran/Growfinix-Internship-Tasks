
# ==========================================
# GROWFINIX INTERNSHIP - TASK 2
# CLI LOG PARSER FOR TOUR ENQUIRIES
# ==========================================

import re
import argparse


# STEP 1: Extract email addresses
def extract_email(text):

    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    result = re.search(pattern, text)

    if result:
        return result.group()

    return "Not found"


# STEP 2: Extract customer names

def extract_name(text):

    patterns = [
        r'this is\s+([A-Za-z][A-Za-z .\'-]*?)(?=[,.!?;]|\s+(?:I|i|We|we|My|my|Contact|contact|Email|email|Please|please)\b|$)',

        r'my name is\s+([A-Za-z][A-Za-z .\'-]*?)(?=[,.!?;]|\s+(?:I|i|We|we|My|my|Contact|contact|Email|email|Please|please)\b|$)',

        r"I'm\s+([A-Za-z][A-Za-z .'-]*?)(?=[,.!?;]|\s+(?:I|i|We|we|My|my|Contact|contact|Email|email|Please|please)\b|$)",

        r'I am\s+(?!interested\b|planning\b|looking\b)([A-Za-z][A-Za-z .\'-]*?)(?=[,.!?;]|\s+(?:I|i|We|we|My|my|Contact|contact|Email|email|Please|please)\b|$)'
    ]

    for pattern in patterns:

        result = re.search(pattern, text, re.IGNORECASE)

        if result:
            return result.group(1).strip()

    return "Not found"



# STEP 3: Extract travel destination
def extract_destination(text):

    patterns = [
        r'trip to\s+([A-Za-z][A-Za-z ]*?)(?=[,.!?;]|\s+(?:Contact|contact|My|my|Email|email|Reach|reach|You|you|Please|please)\b|$)',
        r'travel(?:ling|ing)? to\s+([A-Za-z][A-Za-z ]*?)(?=[,.!?;]|\s+(?:Contact|contact|My|my|Email|email|Reach|reach|Please|please)\b|$)',
        r'visiting\s+([A-Za-z][A-Za-z ]*?)(?=[,.!?;]|\s+(?:Contact|contact|My|my|Email|email|Reach|reach)\b|$)',
        r'visit\s+([A-Za-z][A-Za-z ]*?)(?=[,.!?;]|\s+(?:Contact|contact|My|my|Email|email|Reach|reach)\b|$)',
        r'holiday to\s+([A-Za-z][A-Za-z ]*?)(?=[,.!?;]|\s+(?:Contact|contact|My|my|Email|email|Reach|reach)\b|$)',
        r'holiday in\s+([A-Za-z][A-Za-z ]*?)(?=[,.!?;]|\s+(?:Contact|contact|My|my|Email|email|Reach|reach)\b|$)',
        r'vacation to\s+([A-Za-z][A-Za-z ]*?)(?=[,.!?;]|\s+(?:Contact|contact|My|my|Email|email|Reach|reach)\b|$)',
        r'for\s+([A-Za-z][A-Za-z ]*?)(?=[,.!?;]|\s+(?:Contact|contact|My|my|Email|email|Reach|reach)\b|$)'
    ]

    for pattern in patterns:

        result = re.search(pattern, text, re.IGNORECASE)

        if result:
            return result.group(1).strip()

    return "Not found"


# STEP 4: Process enquiry file
def process_file(filename):

    try:

        with open(filename, "r", encoding="utf-8") as file:

            enquiries = file.readlines()

    except FileNotFoundError:

        print("Error: File not found!")
        return

    print("\n========================================")
    print(" GROWFINIX - TOUR ENQUIRY LOG PARSER")
    print("========================================")

    count = 0

    for enquiry in enquiries:

        enquiry = enquiry.strip()

        if not enquiry:
            continue

        count += 1

        name = extract_name(enquiry)
        email = extract_email(enquiry)
        destination = extract_destination(enquiry)

        print(f"\nEnquiry {count}")
        print("----------------------------------------")
        print("Name        :", name)
        print("Email       :", email)
        print("Destination :", destination)

    print("\n========================================")
    print("TOTAL ENQUIRIES PROCESSED:", count)
    print("========================================")


# STEP 5: Command Line Interface
def main():

    parser = argparse.ArgumentParser(
        description="Tour Enquiry Log Parser"
    )

    parser.add_argument(
        "filename",
        help="Path of the tour enquiry text file"
    )

    args = parser.parse_args()

    process_file(args.filename)


if __name__ == "__main__":

    main()
