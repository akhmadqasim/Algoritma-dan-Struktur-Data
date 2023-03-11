from timeit import Timer  # import modul Timer dari modul timeit

def test1():  # fungsi test1
    l = []  # membuat list kosong
    for i in range(1000):  # perulangan sebanyak 1000 kali
        l = l + [i]  # menambahkan nilai i ke list l


def test2():  # fungsi test2
    l = []  # membuat list kosong
    for i in range(1000):  # perulangan sebanyak 1000 kali
        l.append(i)  # menambahkan nilai i ke list l


def test3():  # fungsi test3
    l = [i for i in range(1000)]  # membuat list dengan comprehension


def test4():  # fungsi test4
    l = list(range(1000))


t1 = Timer("test1()", "from __main__ import test1")  # membuat objek Timer dengan fungsi test1
print("concat ", t1.timeit(number=1000), "milliseconds")  # menampilkan waktu eksekusi fungsi test1
t2 = Timer("test2()", "from __main__ import test2")  # membuat objek Timer dengan fungsi test2
print("append ", t2.timeit(number=1000), "milliseconds")  # menampilkan waktu eksekusi fungsi test2
t3 = Timer("test3()", "from __main__ import test3")  # membuat objek Timer dengan fungsi test3
print("comprehension ", t3.timeit(number=1000), "milliseconds")  # menampilkan waktu eksekusi fungsi test3
t4 = Timer("test4()", "from __main__ import test4")  # membuat objek Timer dengan fungsi test4
print("list range ", t4.timeit(number=1000), "milliseconds")  # menampilkan waktu eksekusi fungsi test4
