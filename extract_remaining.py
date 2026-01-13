from pypdf import PdfReader
import sys

try:
    reader = PdfReader("d:/EFREI/M1/DevSecOps/TP1/TP1_DevOps_Docker_CICD.pdf")
    text = ""
    # Extract text from pages 15 to 19 (indices 15, 16, 17, 18)
    for i, page in enumerate(reader.pages[15:19]):
        text += f"--- Page {i+16} ---\n"
        text += page.extract_text() + "\n"
    
    # Configure stdout to handle utf-8
    sys.stdout.reconfigure(encoding='utf-8')
    print(text)
except Exception as e:
    print(f"Error: {e}")
