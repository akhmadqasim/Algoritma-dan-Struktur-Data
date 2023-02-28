def anagramSolution2(s1, s2):  # Fungsi untuk mengecek apakah dua string merupakan anagram
    alist1 = list(s1)  # Mengubah string kedalam list
    alist2 = list(s2)  # Mengubah string kedalam list
    alist1.sort()  # Mengurutkan list pertama
    alist2.sort()  # Mengurutkan list kedua
    pos = 0  # Membuat variabel pos dengan nilai 0 untuk mengecek posisi string
    matches = True  # Membuat variabel matches dengan nilai True untuk mengecek apakah sama
    while pos < len(s1) and matches:  # Membuat perulangan untuk mengecek apakah string pertama sama dengan string kedua
        if alist1[pos] == alist2[pos]:  # Mengecek apakah string pertama sama dengan string kedua
            pos = pos + 1  # pos ditambah 1
        else:  # Jika tidak sama
            matches = False  # Maka matches bernilai False
    return matches  # Mengembalikan nilai matches


print(anagramSolution2('abcd', 'edcba'))  # Menampilkan hasil dari fungsi anagramSolution2
print(anagramSolution2('abcde', 'edcb'))  # Menampilkan hasil dari fungsi anagramSolution2
print(anagramSolution2('abcde', 'edfba'))  # Menampilkan hasil dari fungsi anagramSolution2
