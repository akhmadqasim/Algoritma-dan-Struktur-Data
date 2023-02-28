# Fungsi anagram merupakan fungsi untuk mengecek apakah dua string merupakan anagram atau tidak
# yang artinya kedua string tersebut memiliki karakter yang sama dan jumlahnya sama

def anagramSolution1(s1, s2):  # Fungsi untuk mengecek apakah dua string merupakan anagram
    alist = list(s2)  # Mengubah string kedalam list

    pos1 = 0  # Membuat variabel pos1 dengan nilai 0 untuk mengecek posisi string pertama
    stillOK = True  # Membuat variabel stillOK dengan nilai True untuk mengecek apakah masih sama

    # Membuat perulangan untuk mengecek apakah string pertama sama dengan string kedua
    while pos1 < len(s1) and stillOK:
        pos2 = 0  # Membuat variabel pos2 dengan nilai 0 untuk mengecek posisi string kedua
        found = False  # Membuat variabel found dengan nilai False untuk mengecek apakah ditemukan
        # Membuat perulangan untuk mengecek apakah string pertama sama dengan string kedua
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:  # Mengecek apakah string pertama sama dengan string kedua
                found = True  # Jika sama maka found bernilai True
            else:  # Jika tidak sama
                pos2 = pos2 + 1  # pos2 ditambah 1

        if found:  # Jika found bernilai True
            alist[pos2] = None  # Membuat nilai list kedua menjadi None
        else:  # Jika found bernilai False
            stillOK = False  # Maka stillOK bernilai False

        pos1 = pos1 + 1  # pos1 ditambah 1

    return stillOK  # Mengembalikan nilai stillOK


print(anagramSolution1('abcd', 'dcba'))  # Menampilkan hasil dari fungsi anagramSolution1
print(anagramSolution1('abcd', 'abdc'))  # Menampilkan hasil dari fungsi anagramSolution1
print(anagramSolution1('abcd', 'defg'))  # Menampilkan hasil dari fungsi anagramSolution1
