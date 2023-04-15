def binarySearch(alist, item):  # alist adalah list yang akan dicari, item adalah nilai yang dicari
    first = 0  # posisi awal
    last = len(alist) - 1  # posisi akhir
    found = False  # nilai awal

    # selama posisi awal lebih kecil dari sama dengan posisi akhir dan nilai belum ditemukan
    while first <= last and not found:
        midpoint = (first + last) // 2  # nilai tengah
        if alist[midpoint] == item:  # jika nilai yang dicari sama dengan nilai yang ada di list
            found = True  # maka nilai ditemukan
        else:  # jika tidak
            if item < alist[midpoint]:  # jika nilai yang dicari lebih kecil dari nilai yang ada di list
                last = midpoint - 1  # maka posisi akhir akan berkurang 1
            else:  # jika tidak
                first = midpoint + 1  # maka posisi awal akan bertambah 1

    return found  # mengembalikan nilai


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]  # list yang akan dicari
print(binarySearch(testlist, 3))  # mencari nilai 3
print(binarySearch(testlist, 13))  # mencari nilai 13


# ---------- 9.3b ---------- #

def binarySearch2(alist, item):  # alist adalah list yang akan dicari, item adalah nilai yang dicari
    if len(alist) == 0:  # jika panjang list adalah 0
        return False  # maka nilai tidak ditemukan
    else:  # jika tidak
        midpoint = len(alist) // 2  # nilai tengah
        if alist[midpoint] == item:  # jika nilai yang dicari sama dengan nilai yang ada di list
            return True  # maka nilai ditemukan
        else:  # jika tidak
            if item < alist[midpoint]:  # jika nilai yang dicari lebih kecil dari nilai yang ada di list
                return binarySearch2(alist[:midpoint], item)  # maka akan dicari lagi di list sebelum nilai tengah
            else:  # jika tidak
                return binarySearch2(alist[midpoint + 1:], item)  # maka akan dicari lagi di list setelah nilai tengah


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]  # list yang akan dicari
print(binarySearch2(testlist, 3))  # mencari nilai 3
print(binarySearch2(testlist, 13))  # mencari nilai 13
