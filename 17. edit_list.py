# Edit List

nama = ["Donny", "Denny", "Fandi", "Nanik"]
# menambah data ke List
nama.append("Ayu")

# hanya menampikan List apa adanya
# print(nama)

# menampilkan List dengan format string,
# agar dapat dikombinasikan dengan string lain
print(f"Isi dalam List: {nama}")


# perintah mengedit data dalam List
print("Nama Fandi diganti dengan Leonardo, hasilnya:")
nama[2] = "Leonardo"
print(nama)
