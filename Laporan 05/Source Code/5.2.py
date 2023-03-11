import timeit  # import modul timeit

popzero = timeit.Timer("x.pop(0)", "from __main__ import x")  # membuat objek Timer dengan fungsi pop(0)
popend = timeit.Timer("x.pop()", "from __main__ import x")  # membuat objek Timer dengan fungsi pop()

x = list(range(2000000))  # membuat list dengan range 2000000
print(popzero.timeit(number=1000))  # menampilkan waktu eksekusi fungsi pop(0)

x = list(range(2000000))  # membuat list dengan range 2000000
print(popend.timeit(number=1000))  # menampilkan waktu eksekusi fungsi pop()
