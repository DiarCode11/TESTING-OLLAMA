import requests
from bs4 import BeautifulSoup as bs4
import sys
from pdf_downloader import download_pdf

# Mengatur encoding konsol ke UTF-8 untuk menghindari UnicodeEncodeError saat mencetak
sys.stdout.reconfigure(encoding='utf-8')

# Mengirim permintaan HTTP dan mendapatkan respons sebagai teks
data = requests.get('https://ejournal.undiksha.ac.id/index.php/JPI/oai?verb=ListRecords&metadataPrefix=oai_dc').text

# Parsing data XML menggunakan BeautifulSoup
soup = bs4(data, 'xml')

# Menyimpan hasil parsing ke file dengan encoding UTF-8
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

# Contoh: Menampilkan semua elemen 'record' dalam XML
records = soup.find_all('record')

n = 0
# Mengambil dan menampilkan informasi spesifik dari setiap 'record'
for record in records:
    title = record.find('title').text if record.find('title') else "No title"
    url = record.find('relation').text if record.find('relation') else None
    
    # Mengabaikan record jika URL kosong
    if not url:
        continue
    
    pdf_title = f'JPTK-{n}.pdf'
    
    # Mengunduh PDF hanya jika URL ada
    download_pdf(url, pdf_title)
    
    n += 1

    # Menyimpan setiap record yang valid ke file dengan encoding UTF-8
    with open('records_output.txt', 'a', encoding='utf-8') as f:
        f.write(f"Title: {title}\nURL: {url}\n\n")
