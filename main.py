# main.py
import argparse
import sys
from processing import extract_text_from_pdf, parse_isin_from_text, write_to_csv

def main():
    """
    Main function to run the PDF to CSV extraction process.
    """
    # --- 1. Set up Command-Line Argument Parser ---
    parser = argparse.ArgumentParser(
        description="Extracts stock ISINs and names from a Trade Republic PDF report and saves them to a CSV file."
    )
    parser.add_argument(
        "pdf_input_path",
        type=str,
        help="The path to the input PDF file (e.g., 'report.pdf')."
    )
    parser.add_argument(
        "-o", "--output",
        dest="csv_output_path",
        type=str,
        default="trading_universe.csv",
        help="The path for the output CSV file (default: 'trading_universe.csv')."
    )
    args = parser.parse_args()

    # --- 2. Execute the Processing Pipeline ---
    try:
        # Step 1: Extract text from the PDF
        raw_text = extract_text_from_pdf(args.pdf_input_path)
        
        # Step 2: Parse the extracted text to find stock data
        stock_data = parse_isin_from_text(raw_text)
        
        # Step 3: Write the structured data to a CSV file
        write_to_csv(stock_data, args.csv_output_path)

    except FileNotFoundError:
        print(f"Error: The input file '{args.pdf_input_path}' was not found.", file=sys.stderr)
        sys.exit(1) # Exit with an error code
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()