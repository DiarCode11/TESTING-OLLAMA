import pdfplumber
from PyPDF2 import PdfReader
import sys
import re

def read_pdf(file_path):
    # Set encoding ke UTF-8
    sys.stdout.reconfigure(encoding='utf-8')
    
    # Membuka file PDF
    with pdfplumber.open(file_path) as pdf:
        # Menggabungkan teks dari semua halaman
        text = ""
        for page in pdf.pages:
            # Mengabaikan area header dan footer dengan menggunakan bounding box (bbox)
            # Misalnya, kita ingin mengambil teks di area 50-750 pixel pada sumbu y
            # Anda dapat menyesuaikan nilai bbox sesuai kebutuhan
            cropped_page = page.within_bbox((0, 50, page.width, page.height - 50))
            page_text = cropped_page.extract_text()
            if page_text:
                text += page_text
        
        return text

    
def get_abstract(text):
    try:
        # Mengubah teks menjadi huruf kecil
        text = text.lower()
        
        # Daftar pola yang akan dicoba
        patterns = [
            re.compile(rf'abstrak(.*?)(kata-kata kunci)', re.DOTALL),
            re.compile(rf'abstrak(.*?)(kata kunci)', re.DOTALL),
            re.compile(rf'abstrak(.*?)(abstract)', re.DOTALL)
        ]
        
        # Mencoba setiap pola
        for pattern in patterns:
            match = pattern.search(text)
            if match:
                return match.group(1).strip()
        
        return None 
    
    except Exception as e:
        print(f"Gagal menemukan abstrak: {str(e)}")

def get_keyword(text): 
    try:
        # Mengubah teks menjadi huruf kecil
        text = text.lower()
        
        # Daftar pola yang akan dicoba
        patterns = [
            re.compile(r'kata kunci(.*?)(\n)', re.DOTALL), 
            re.compile(r'Keywords(.*?)(\n)', re.DOTALL),  
            # re.compile(r'keyword(.*?)(abstract)', re.DOTALL)     # Mencari teks antara "keyword" dan "abstract"
        ]
        
        # Mencoba setiap pola
        for pattern in patterns:
            match = pattern.search(text)
            keyword = match.group(1).strip()
            if match:
                return keyword[2:]
        
        return None

    except Exception as e:
        print(f"Gagal menemukan kata kunci: {str(e)}")

# for i in range(0, 95):
#     # Contoh penggunaan
#     file_path = f"PDF\JPTK-{i}.pdf"
#     pdf_text = read_pdf(file_path)
#     teks = get_keyword(pdf_text)
#     print(f"{i} : {teks}")

text = read_pdf('PDF\JPTK-5.pdf')
ekstrak = get_keyword(text)
print(f'{text}\n\n{ekstrak}')