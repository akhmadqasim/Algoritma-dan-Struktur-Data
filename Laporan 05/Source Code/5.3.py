import timeit  # import modul timeit
popzero = timeit.Timer("x.pop(0)", "from __main__ import x")  # membuat objek Timer dengan fungsi pop(0)
popend = timeit.Timer("x.pop()", "from __main__ import x")  # membuat objek Timer dengan fungsi pop()

print("pop(0)            pop()")  # menampilkan judul tabel
for i in range(1000000, 100000001, 1000000):  # perulangan sebanyak 100000000 dengan interval 1000000
    x = list(range(i))  # membuat list dengan range i
    pt = popend.timeit(number=1000)  # menampilkan waktu eksekusi fungsi pop()
    x = list(range(i))  # membuat list dengan range i
    pz = popzero.timeit(number=1000)  # menampilkan waktu eksekusi fungsi pop(0)
    print("%15.5f, %15.5f" % (pz, pt))  # menampilkan waktu eksekusi fungsi pop(0) dan pop()
