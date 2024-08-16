import fitz  # PyMuPDF

# Buka file PDF
doc = fitz.open("PDF/JPTK-10.pdf")

# Iterasi melalui halaman-halaman
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text = page.get_text("text")  # Mendapatkan teks dengan struktur paragraf
    print(text)
