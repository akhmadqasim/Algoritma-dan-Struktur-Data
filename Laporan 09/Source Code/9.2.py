# Fungsi pertama untuk mencari nilai tertentu dalam list
def sequentialSearch(alist, item):  # alist adalah list yang akan dicari, item adalah nilai yang dicari
    pos = 0  # posisi awal
    found = False  # nilai awal

    while pos < len(alist) and not found:  # selama posisi masih kurang dari panjang list dan nilai belum ditemukan
        if alist[pos] == item:  # jika nilai yang dicari sama dengan nilai yang ada di list
            found = True  # maka nilai ditemukan
        else:  # jika tidak
            pos = pos + 1  # maka posisi akan bertambah 1

    return found  # mengembalikan nilai


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]  # list yang akan dicari
print(sequentialSearch(testlist, 3))  # mencari nilai 3
print(sequentialSearch(testlist, 13))  # mencari nilai 13


# Fungsi kedua untuk mencari nilai tertentu dalam list
def orderedSequentialSearch(alist, item):  # alist adalah list yang akan dicari, item adalah nilai yang dicari
    pos = 0  # posisi awal
    found = False  # nilai awal
    stop = False  # nilai awal

    # selama posisi masih kurang dari panjang list dan nilai belum ditemukan dan nilai belum ditemukan
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:  # jika nilai yang dicari sama dengan nilai yang ada di list
            found = True  # maka nilai ditemukan
        else:  # jika tidak
            if alist[pos] > item:  # jika nilai yang ada di list lebih besar dari nilai yang dicari
                stop = True  # maka nilai ditemukan
            else:  # jika tidak
                pos = pos + 1  # maka posisi akan bertambah 1

    return found  # mengembalikan nilai


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]  # list yang akan dicari
print(orderedSequentialSearch(testlist, 3))  # mencari nilai 3
print(orderedSequentialSearch(testlist, 13))  # mencari nilai 13
