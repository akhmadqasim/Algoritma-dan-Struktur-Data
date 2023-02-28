def anagramSolution2(s1, s2):  # Fungsi untuk mengecek apakah dua string merupakan anagram
    c1 = [0] * 26  # Membuat list c1 dengan panjang 26
    c2 = [0] * 26  # Membuat list c2 dengan panjang 26

    for i in range(len(s1)):  # Membuat perulangan untuk mengecek apakah string pertama sama dengan string kedua
        pos = ord(s1[i]) - ord('a')  # Mengubah string kedalam list
        c1[pos] = c1[pos] + 1  # Mengurutkan list pertama

    for i in range(len(s2)):  # Membuat perulangan untuk mengecek apakah string pertama sama dengan string kedua
        pos = ord(s2[i]) - ord('a')  # Mengubah string kedalam list
        c2[pos] = c2[pos] + 1  # Mengurutkan list kedua

    j = 0  # Membuat variabel j dengan nilai 0
    stillOK = True  # Membuat variabel stillOK dengan nilai True
    while j < 26 and stillOK:  # Membuat perulangan untuk mengecek apakah string pertama sama dengan string kedua
        if c1[j] == c2[j]:  # Mengecek apakah string pertama sama dengan string kedua
            j = j + 1  # j ditambah 1
        else:  # Jika tidak sama
            stillOK = False  # Maka stillOK bernilai False

    return stillOK  # Mengembalikan nilai stillOK


print(anagramSolution2('apple', 'pleap'))  # Menampilkan hasil dari fungsi anagramSolution2 yaiitu True
print(anagramSolution2('orange', 'ngerao'))  # Menampilkan hasil dari fungsi anagramSolution2 yaiitu True
print(anagramSolution2('apple', 'durian'))  # Menampilkan hasil dari fungsi anagramSolution2 yaiitu False
