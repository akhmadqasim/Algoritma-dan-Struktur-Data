# fungsi moveTower dengan parameter height, fromPole, toPole, withPole
# fungsi ini digunakan untuk memindahkan tower dengan tinggi height dari fromPole ke toPole
def moveTower(height, fromPole, toPole, withPole):

    if height >= 1:  # jika height lebih besar atau sama dengan 1
        # memanggil fungsi moveTower dengan parameter height - 1, fromPole, withPole, toPole
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)  # memanggil fungsi moveDisk dengan parameter fromPole dan toPole
        # memanggil fungsi moveTower dengan parameter height - 1, withPole, toPole, fromPole
        moveTower(height - 1, withPole, toPole, fromPole)


def moveDisk(fp, tp):  # fungsi moveDisk dengan parameter fp dan tp
    print("moving disk from", fp, "to", tp)  # mencetak "moving disk from" dan fp dan "to" dan tp


moveTower(3, "A", "B", "C")  # memanggil fungsi moveTower dengan parameter 3, "A", "B", "C"
moveTower(2, "A", "B", "C")  # memanggil fungsi moveTower dengan parameter 2, "A", "B", "C"
moveTower(4, "A", "B", "C")  # memanggil fungsi moveTower dengan parameter 4, "A", "B", "C"
