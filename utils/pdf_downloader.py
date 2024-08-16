import requests
import os

def download_pdf(url, filename):
    try:
        save_path = 'PDF'
        
        # Pastikan folder ada, jika tidak, buat foldernya
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        
        # Mengganti URL view menjadi URL download
        download_url = url.replace('view', 'download')
        
        # Meminta file dari URL
        response = requests.get(download_url)
        
        # Memastikan request berhasil (status code 200)
        # response.raise_for_status()  # Ini akan memunculkan HTTPError jika status bukan 200
        
        # Menyimpan file PDF ke folder yang ditentukan
        with open(os.path.join(save_path, filename), 'wb') as file:
            file.write(response.content)
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Kesalahan yang terkait dengan HTTP, seperti 404, 500, dll.
    except Exception as err:
        print(f"Other error occurred: {err}")  # Kesalahan lain yang tidak terduga
    else:
        print(filename + " has been downloaded successfully.")

# # Contoh penggunaan
# url = 'https://ejournal.undiksha.ac.id/index.php/JPTK/article/view/2842/2348'
# save_path = 'PDF'  # Ganti dengan path folder tempat ingin menyimpan file
# filename = 'downloaded_file.pdf'  # Ganti dengan nama file yang diinginkan

# download_pdf(url, filename)
