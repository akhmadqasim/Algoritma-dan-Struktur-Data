from pythonds.basic.stack import Stack  # Mengimpor modul Stack


def infixToPostfix(infixexpr):  # Fungsi infixToPostfix untuk mengubah ekspresi infix menjadi postfix
    prec = {}  # Membuat variabel prec dengan nilai dictionary kosong
    prec["*"] = 3  # Menambahkan nilai ke dalam variabel prec
    prec["/"] = 3  # Menambahkan nilai ke dalam variabel prec
    prec["+"] = 2  # Menambahkan nilai ke dalam variabel prec
    prec["-"] = 2  # Menambahkan nilai ke dalam variabel prec
    prec["("] = 1  # Menambahkan nilai ke dalam variabel prec
    opStack = Stack()  # Membuat objek Stack
    postfixList = []  # Membuat variabel postfixList dengan nilai list kosong
    tokenList = infixexpr.split()  # Membuat variabel tokenList dengan nilai list yang di split dari variabel infixexpr

    for token in tokenList:  # Melakukan perulangan for
        # Melakukan pengecekan apakah token berada di dalam variabel prec
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)  # Menambahkan nilai token ke dalam variabel postfixList
        elif token == '(':  # Jika token bernilai (
            opStack.push(token)  # Memasukkan nilai token ke dalam stack
        elif token == ')':  # Jika token bernilai )
            topToken = opStack.pop()  # Membuat variabel topToken dengan nilai yang di pop dari stack
            while topToken != '(':  # Melakukan perulangan while
                postfixList.append(topToken)  # Menambahkan nilai topToken ke dalam variabel postfixList
                topToken = opStack.pop()  # Membuat variabel topToken dengan nilai yang di pop dari stack
        else:  # Jika token tidak ada di dalam variabel prec
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):  # Melakukan perulangan while
                # Menambahkan nilai yang di pop dari stack ke dalam variabel postfixList
                postfixList.append(opStack.pop())
            opStack.push(token)  # Memasukkan nilai token ke dalam stack

    while not opStack.isEmpty():  # Melakukan perulangan while
        postfixList.append(opStack.pop())  # Menambahkan nilai yang di pop dari stack ke dalam variabel postfixList
    return " ".join(postfixList)  # Mengembalikan nilai variabel postfixList yang di join dengan spasi


print(infixToPostfix("A * B + C * D"))  # Menampilkan hasil dari fungsi infixToPostfix
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))  # Menampilkan hasil dari fungsi infixToPostfix
print(infixToPostfix("( A + B ) * ( C + D )"))  # Menampilkan hasil dari fungsi infixToPostfix
print(infixToPostfix("( A + B ) * C"))  # Menampilkan hasil dari fungsi infixToPostfix
print(infixToPostfix("A + B * C"))  # Menampilkan hasil dari fungsi infixToPostfix
