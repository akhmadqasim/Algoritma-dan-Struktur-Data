import timeit  # import modul timeit
import random  # import modul random

for i in range(10000, 500001, 20000):  # perulangan sebanyak 500000 dengan interval 20000
    # membuat objek Timer dengan fungsi random.randrange()
    t = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random, x")
    x = list(range(i))  # membuat list dengan range i
    lst_time = t.timeit(number=1000)  # menampilkan waktu eksekusi fungsi random.randrange()
    x = {j: None for j in range(i)}  # membuat dictionary dengan range i
    d_time = t.timeit(number=1000)  # menampilkan waktu eksekusi fungsi random.randrange()
    # menampilkan waktu eksekusi fungsi random.randrange() pada list dan dictionary
    print("%d, %10.3f, %10.3f" % (i, lst_time, d_time))
