x = 12
y = 37

Ha = x + y
print("Ha =", Ha)

Hb = Ha + 10.5
print("Hb =", Hb)

Hc = int(Hb)
print("Hc =", Hc)

Hd = Ha / Hb
print("Hd =", Hd)

print(isinstance(Hd, int))

print(isinstance(Hd, float))

if isinstance(Hd, int):
    print("Hd adalah bilangan integer")
else:
    print("Hd adalah bilangan float")
