MyList = [1, 3, True, 6.5]
print(MyList)
A = [MyList] * 3
print(A)
MyList[2] = 45
print(A)

myList_A = [1024, 3, True, 6.5]
myList_A.append(False)
print(myList_A)
myList_A.insert(2, 4.5)
print(myList_A)
print(myList_A.pop())
print(myList_A)
print(myList_A.pop(1))
print(myList_A)
myList_A.pop(2)
print(myList_A)
myList_A.sort()
print(myList_A)
myList_A.reverse()
print(myList_A)
print(myList_A.count(6.5))
print(myList_A.index(4.5))
myList_A.remove(6.5)
print(myList_A)
del myList_A[0]
print(myList_A)
