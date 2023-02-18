capitals = {"KalTim": "Samarinda", "Bali": "Denpasar"}  # variabel capitals berisi dictionary
print(capitals["KalTim"])  # Menampilkan isi variabel capitals pada key "KalTim"
capitals["JaTim"] = "Surabaya"  # Menambahkan key "JaTim" dengan value "Surabaya" ke dictionary capitals
print(capitals)  # Menampilkan isi variabel capitals
capitals["KalSel"] = "Banjarmasin"  # Menambahkan key "KalSel" dengan value "Banjarmasin" ke dictionary capitals
print(len(capitals))  # Menampilkan panjang dictionary capitals
for k in capitals:  # Menampilkan isi dictionary capitals
    print(capitals[k], "adalah ibukota dari ", k)  # Menampilkan isi dictionary capitals

# contoh dictionary yang berisi tipe data integer dan float
contoh = {"a": 1, "b": 2, "c": 3, "d": 4.5}
