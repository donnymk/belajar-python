# Tipe data List

nama = ["Donny", "Denny", "Fandi", "Nanik"]
# menambah data ke List
nama.append("Ayu")

# hanya menampikan List apa adanya
print(nama);
# menampilkan List dengan format string,
# agar dapat dikombinasikan dengan string lain
print(f"Isi dalam List: {nama}")

# menampilkan panjang List
panjang_list = len(nama)
print(f"Panjang List: {panjang_list}")

# mengakses data dalam List
orang_pertama = nama[0]
print(f"orang_pertama: "+orang_pertama)

# perintah menghapus data dalam List
print("Nama Ayu dihapus dari List, hasilnya:")
nama.remove("Ayu")
print(nama)
