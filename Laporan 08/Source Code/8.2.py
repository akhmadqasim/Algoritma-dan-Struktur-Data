def toStr(n, base):  # n adalah bilangan bulat, base adalah basis dari sistem bilangan
    convertString = "0123456789ABCDEF"  # string yang berisi karakter 0-9 dan A-F
    if n < base:  # jika n kurang dari base
        return convertString[n]  # mengembalikan nilai convertString ke indeks n
    else:  # jika tidak
        # mengembalikan nilai fungsi toStr dengan parameter n dibagi base dan base
        # ditambah convertString ke indeks n modulo base
        return toStr(n // base, base) + convertString[n % base]


print(toStr(1453, 16))  # memanggil fungsi toStr dengan parameter 1453 dan 16
