# Trade Republic Exporter

A simple Python tool to extract a list of securities (stocks, ETFs) and their ISINs from a Trade Republic PDF document and export them to a clean CSV file.

## Features

- Extracts text directly from a PDF file.
- Parses the text to find lines containing ISINs and security names.
- Exports the clean data to a CSV file.
- Easy-to-use command-line interface.
- Modular and easy-to-understand code.

## Project Structure

- `main.py`: The main script and entry point for the application. Handles command-line arguments.
- `processing.py`: Contains the core logic for PDF extraction, text parsing, and CSV writing.
- `requirements.txt`: A list of Python libraries required to run the project.

## How to Use

### 1. Installation

First, clone this repository or download the files. Then, install the necessary dependencies.

```bash
# Navigate to the project directory
cd trade-republic-exporter

# Install required packages
pip install -r requirements.txt

# Run
python main.py report.pdf
```
