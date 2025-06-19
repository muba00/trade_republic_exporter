# processing.py
import csv
import re
from typing import List, Tuple

import pdfplumber
from pdfplumber.pdf import PDF

# Define a type hint for our structured data for clarity
StockData = List[Tuple[str, str]]

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Opens a PDF file and extracts all text content into a single string.

    Args:
        pdf_path (str): The file path to the PDF.

    Returns:
        str: A single string containing all text from the PDF pages.
    
    Raises:
        FileNotFoundError: If the pdf_path does not exist.
    """
    full_text = []
    print(f"Reading PDF: '{pdf_path}'...")
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                full_text.append(text)
    print(f"Successfully extracted text from {len(pdf.pages)} pages.")
    return "\n".join(full_text)


def parse_isin_from_text(text: str) -> StockData:
    """
    Parses a block of text to find lines containing ISINs and company names.

    Args:
        text (str): The input text to parse.

    Returns:
        StockData: A list of (ISIN, Name) tuples.
    """
    # Regex to find lines that start with a 12-character ISIN.
    # ^([A-Z]{2}[A-Z0-9]{10})\s+(.*)
    isin_pattern = re.compile(r'^[A-Z]{2}[A-Z0-9]{10}\s+.*', re.MULTILINE)
    
    extracted_data: StockData = []
    
    # Use findall to get all non-overlapping matches in the string
    matches = isin_pattern.findall(text)
    
    for line in matches:
        # The line is guaranteed to have the ISIN. Split it once on the first space.
        parts = line.strip().split(' ', 1)
        if len(parts) == 2:
            isin, name = parts
            extracted_data.append((isin, name.strip()))

    if not extracted_data:
        print("Warning: No data matching the ISIN pattern was found in the text.")
    else:
        print(f"Found {len(extracted_data)} potential stock records.")
        
    return extracted_data


def write_to_csv(data: StockData, output_csv_path: str) -> None:
    """
    Writes a list of (ISIN, Name) tuples to a CSV file.

    Args:
        data (StockData): The list of data to write.
        output_csv_path (str): The file path for the output CSV.
    """
    if not data:
        print("No data to write. CSV file will not be created.")
        return

    print(f"Writing data to '{output_csv_path}'...")
    try:
        with open(output_csv_path, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(['ISIN', 'Name'])  # Write header
            writer.writerows(data)             # Write all data rows
        print("Successfully created the CSV file.")
    except IOError as e:
        print(f"Error: Could not write to file '{output_csv_path}'. Reason: {e}")