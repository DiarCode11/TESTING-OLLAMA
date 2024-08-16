import fitz  # PyMuPDF

def extract_text_from_columns_or_full(pdf_path, output_text_file):
    # Buka PDF
    doc = fitz.open(pdf_path)
    
    # Buka file untuk menyimpan teks yang diekstrak
    with open(output_text_file, 'w') as output_file:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)  # Memuat halaman
            
            # Ambil dimensi halaman
            width = page.rect.width
            height = page.rect.height
            
            # Bagi halaman menjadi dua kolom yang sama
            left_column_rect = fitz.Rect(0, 0, width/2, height)
            right_column_rect = fitz.Rect(width/2, 0, width, height)
            
            # Ekstrak teks dari dua kolom
            left_column_text = page.get_text("text", clip=left_column_rect).strip()
            right_column_text = page.get_text("text", clip=right_column_rect).strip()
            
            # Jika kedua kolom kosong, asumsikan halaman tidak berbentuk kolom
            if left_column_text and right_column_text:
                output_file.write(f"Page {page_num+1} - Left Column:\n")
                output_file.write(left_column_text)
                output_file.write("\n\n")
                
                output_file.write(f"Page {page_num+1} - Right Column:\n")
                output_file.write(right_column_text)
                output_file.write("\n\n")
            else:
                # Ekstrak teks dari seluruh halaman
                full_page_text = page.get_text("text").strip()
                output_file.write(f"Page {page_num+1} - Full Page:\n")
                output_file.write(full_page_text)
                output_file.write("\n\n")

    print(f"Extraction complete. Text saved to {output_text_file}")

# Contoh penggunaan
extract_text_from_columns_or_full("PDF\JPTK-5.pdf", "extracted_text.txt")
