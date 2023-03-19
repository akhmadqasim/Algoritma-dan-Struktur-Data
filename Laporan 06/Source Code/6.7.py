from pythonds.basic.stack import Stack  # Mengimpor modul Stack


def postfixEval(postfixExpr):  # Fungsi postfixEval untuk mengubah ekspresi postfix menjadi nilai
    operandStack = Stack()  # Membuat objek Stack
    # Membuat variabel tokenList dengan nilai list yang di split dari variabel postfixExpr
    tokenList = postfixExpr.split()

    for token in tokenList:  # Melakukan perulangan for untuk setiap token di dalam variabel tokenList
        if token in "0123456789":  # Melakukan pengecekan apakah token berada di dalam variabel prec
            operandStack.push(int(token))  # Memasukkan nilai token ke dalam stack
        else:  # Jika token tidak ada di dalam variabel prec
            operand2 = operandStack.pop()  # Membuat variabel operand2 dengan nilai yang di pop dari stack
            operand1 = operandStack.pop()  # Membuat variabel operand1 dengan nilai yang di pop dari stack
            result = doMath(token, operand1, operand2)  # Membuat variabel result dengan nilai dari fungsi doMath
            operandStack.push(result)  # Memasukkan nilai result ke dalam stack
    return operandStack.pop()  # Mengembalikan nilai yang di pop dari stack


def doMath(op, op1, op2):  # Fungsi doMath untuk melakukan operasi matematika
    if op == "*":  # Melakukan pengecekan apakah op bernilai *
        return op1 * op2  # Mengembalikan nilai op1 * op2
    elif op == "/":  # Melakukan pengecekan apakah op bernilai /
        return op1 / op2  # Mengembalikan nilai op1 / op2
    elif op == "+":  # Melakukan pengecekan apakah op bernilai +
        return op1 + op2  # Mengembalikan nilai op1 + op2
    else:  # Jika op bernilai -
        return op1 - op2  # Mengembalikan nilai op1 - op2


print(postfixEval('7 8 + 3 2 + /'))  # Menampilkan hasil dari fungsi postfixEval
