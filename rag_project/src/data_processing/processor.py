import fitz # PyMuPDF
import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List, Tuple

def parse_pdf(pdf_path: str) -> str:
    """Parses a PDF, extracting both text and tables."""
    parsed_data = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    parsed_data.append(f"--- Page {page_num + 1} ---\n{text}\n\n")

                tables = page.extract_tables()
                for table in tables:
                    table_string = "\n".join([" | ".join(map(str, row)) for row in table])
                    if table_string:
                        parsed_data.append(f"--- Page {page_num + 1} Table ---\n{table_string}\n\n")
        return "".join(parsed_data)
    except Exception as e:
        print(f"Error parsing {pdf_path}: {e}")
        return ""

def chunk_text(text: str, chunk_size: int, chunk_overlap: int) -> List[str]:
    """Splits a string of text into smaller, overlapping chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    return text_splitter.split_text(text)

def process_single_pdf(pdf_path: str, chunk_size: int, chunk_overlap: int) -> Tuple[List[str], str]:
    """Combines parsing and chunking for a single PDF."""
    print(f"Processing PDF: {pdf_path}")
    content = parse_pdf(pdf_path)
    if not content:
        return [], ""
    
    chunks = chunk_text(content, chunk_size, chunk_overlap)
    return chunks, content