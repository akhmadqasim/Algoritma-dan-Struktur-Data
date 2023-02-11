mySet = {3, 6, "kucing", 4.5, False}
print(mySet)
print(len(mySet))
print(False in mySet)
print("cat" in mySet)

yourSet = {99, 3, 100, "kuda"}
print(mySet.union(yourSet))
print(mySet | yourSet)
print(mySet.intersection(yourSet))
print(mySet & yourSet)
print(mySet.difference(yourSet))
print(mySet - yourSet)
print({3100}.issubset(yourSet))
print({3100} <= yourSet)

mySet.add("rumah")
print(mySet)
mySet.remove(4.5)
print(mySet)
print(mySet.pop())
print(mySet)

mySet.clear()
print(mySet)
