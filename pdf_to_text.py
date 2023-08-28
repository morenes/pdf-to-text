import PyPDF2
import sys
import re

def clean_text(text):
    # Replace hyphenated line breaks with a single word
    text = re.sub(r'(\w)-\n(\w)', r'\1\2', text)
    
    # Replace line breaks followed by a lowercase character with a space
    text = re.sub(r'\n(?=[a-z])', ' ', text)
    
    return text

def pdf_to_text(pdf_path, output_file):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        num_pages = len(reader.pages)
        text = ""

        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()

    text = clean_text(text)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python pdf_to_text.py <path_to_pdf> <output_text_file>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_file = sys.argv[2]

    pdf_to_text(pdf_path, output_file)
    print(f"Text extracted from {pdf_path} and saved as {output_file}.")
