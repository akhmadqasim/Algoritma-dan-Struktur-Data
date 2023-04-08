import turtle  # Mengimport modul turtle

myTurtle = turtle.Turtle()  # Membuat objek turtle
myWin = turtle.Screen()  # Membuat objek screen


def drawSpiral(myTurtle, lineLen):  # Membuat fungsi drawSpiral
    if lineLen > 0:  # Jika lineLen lebih besar dari 0
        myTurtle.forward(lineLen)  # Menggerakkan turtle ke depan sejauh lineLen
        myTurtle.right(90)  # Mengubah arah turtle ke kanan sejauh 90 derajat
        drawSpiral(myTurtle, lineLen - 5)  # Memanggil fungsi drawSpiral dengan parameter myTurtle dan lineLen - 5


drawSpiral(myTurtle, 100)  # Memanggil fungsi drawSpiral dengan parameter myTurtle dan 100
myWin.exitonclick()  # Menutup window ketika diklik

# --------------- Program 8.4b ----------------- #

# import turtle


# def tree(branchLen, t):
#     if branchLen > 5:
#         t.forward(branchLen)
#         t.right(20)
#         tree(branchLen - 15, t)
#         t.left(40)
#         tree(branchLen - 15, t)
#         t.right(20)
#         t.backward(branchLen)
#
#
# def main():
#     t = turtle.Turtle()
#     myWin = turtle.Screen()
#     t.left(90)
#     t.up()
#     t.backward(100)
#     t.down()
#     t.color("green")
#     tree(75, t)
#     myWin.exitonclick()
#
# main()