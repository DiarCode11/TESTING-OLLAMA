def name_swapping(authors_list):
    hasil = []
    for name in authors_list:
        # Memisahkan nama berdasarkan spasi
        parts = name.split(',')
        
        # Memeriksa apakah nama memiliki setidaknya dua bagian
        if len(parts) >= 2:
            # Menukar posisi nama
            hasil.append(f"{parts[1]} {parts[0]}")
        else:
            # Jika hanya ada satu bagian atau kosong, tambahkan nama seperti aslinya
            hasil.append(name)
    
    return hasil
