SQlist = []  # list kosong
# mengenerate list dengan for loop dan dimasukkan ke SQlist
for x in range(1, 11):  # x = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    SQlist.append(x * x)  # x * x = 1, 4, 9, 16, 25, 36, 49, 64, 81, 100

print(SQlist)  # menampilkan SQlist

STlist = [x * x for x in range(1, 11)]  # mengenerate list dengan list comprehension
print(STlist)  # menampilkan STlist

s = [x * x for x in range(10)]
v = [2 ** i for i in range(13)]
m = [x * 2 for x in range(5)]

print(s)
print(v)
print(m)
