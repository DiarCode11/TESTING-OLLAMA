import requests
import os

def download_pdf(url, save_path, filename):
    # Meminta file dari URL
    response = requests.get(url)
    
    # Memastikan request berhasil (status code 200)
    if response.status_code == 200:
        # Menyimpan file PDF ke folder yang ditentukan
        with open(os.path.join(save_path, filename), 'wb') as file:
            file.write(response.content)
        print(f"PDF berhasil diunduh dan disimpan di {os.path.join(save_path, filename)}")
    else:
        print("Gagal mengunduh PDF. Status code:", response.status_code)

# # Contoh penggunaan
# url = 'https://ejournal.undiksha.ac.id/index.php/JPI/article/download/4457/3430'
# save_path = 'PDF'  # Ganti dengan path folder tempat ingin menyimpan file
# filename = 'downloaded_file.pdf'  # Ganti dengan nama file yang diinginkan

# # Pastikan folder ada, jika tidak, buat foldernya
# if not os.path.exists(save_path):
#     os.makedirs(save_path)

# download_pdf(url, save_path, filename)
