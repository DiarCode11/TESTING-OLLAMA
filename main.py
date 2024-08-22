from langchain_community.document_loaders import OnlinePDFLoader
import sys


# Set encoding ke UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# URL file PDF
url = "https://ejournal.undiksha.ac.id/index.php/JPI/article/download/1409/1270"

# Menginisialisasi OnlinePDFLoader dengan URL PDF
loader = OnlinePDFLoader(url)

# Mengambil konten dari PDF
documents = loader.load()

print(documents[0].page_content)
