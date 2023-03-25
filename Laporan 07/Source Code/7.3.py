from pythonds.basic.queue import Queue  # Mengimpor modul Queue
import random  # Mengimpor modul random


class Printer:  # Membuat kelas Printer
    def __init__(self, ppm):  # Membuat konstruktor
        self.pagerate = ppm  # Membuat variabel pagerate dengan nilai ppm
        self.currentTask = None  # Membuat variabel currentTask dengan nilai None
        self.timeRemaining = 0  # Membuat variabel timeRemaining dengan nilai 0

    def tick(self):  # Membuat fungsi tick
        if self.currentTask != None:  # Jika currentTask tidak sama dengan None
            self.timeRemaining = self.timeRemaining - 1  # Maka nilai timeRemaining akan dikurangi 1
            if self.timeRemaining <= 0:  # Jika nilai timeRemaining kurang dari sama dengan 0
                self.currentTask = None  # Maka nilai currentTask akan bernilai None

    def busy(self):  # Membuat fungsi busy
        if self.currentTask != None:  # Jika currentTask tidak sama dengan None
            return True  # Maka kembalikan nilai True
        else:  # Maka jika tidak
            return False  # Maka kembalikan nilai False

    def startNext(self, newtask):  # Membuat fungsi startNext
        self.currentTask = newtask  # Membuat variabel currentTask dengan nilai newtask
        # Membuat variabel timeRemaining dengan nilai newtask.getPages() * 60 / self.pagerate
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task:  # Membuat kelas Task untuk membuat task baru
    def __init__(self, time):  # Membuat konstruktor
        self.timestamp = time  # Membuat variabel timestamp dengan nilai time
        self.pages = random.randrange(1, 21)  # Membuat variabel pages dengan nilai random dari 1 sampai 21

    def getStamp(self):  # Membuat fungsi getStamp
        return self.timestamp  # Mengembalikan nilai timestamp

    def getPages(self):  # Membuat fungsi getPages
        return self.pages  # Mengembalikan nilai pages

    def waitTime(self, currenttime):  # Membuat fungsi waitTime
        return currenttime - self.timestamp  # Mengembalikan nilai currenttime - timestamp


def simulation(numSeconds, pagesPerMinute):  # Membuat fungsi simulation
    labprinter = Printer(pagesPerMinute)  # Membuat objek labprinter dengan nilai Printer(pagesPerMinute)
    printQueue = Queue()  # Membuat objek printQueue dengan nilai Queue()
    waitingtimes = []  # Membuat variabel waitingtimes dengan nilai list kosong

    for currentSecond in range(numSeconds):  # Melakukan perulangan for
        if newPrintTask():  # Jika fungsi newPrintTask bernilai True
            task = Task(currentSecond)  # Membuat objek task dengan nilai Task(currentSecond)
            printQueue.enqueue(task)  # Memasukkan nilai task ke dalam printQueue

        # Jika labprinter tidak sibuk dan printQueue tidak kosong
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()  # Membuat objek nexttask dengan nilai printQueue.dequeue()
            # Menambahkan nilai nexttask.waitTime(currentSecond) ke dalam waitingtimes
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)  # Memulai task selanjutnya

        labprinter.tick()  # Memanggil fungsi tick

    # Membuat variabel averageWait dengan nilai rata-rata dari waitingtimes
    averageWait = sum(waitingtimes) / len(waitingtimes)
    # Menampilkan nilai averageWait dan panjang dari printQueue
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))


def newPrintTask():  # Membuat fungsi newPrintTask
    num = random.randrange(1, 181)  # Membuat variabel num dengan nilai random dari 1 sampai 181
    if num == 180:  # Jika nilai num sama dengan 180
        return True  # Maka kembalikan nilai True
    else:  # Maka jika tidak
        return False  # Maka kembalikan nilai False


for i in range(10):  # Melakukan perulangan for
    simulation(3600, 5)  # Memanggil fungsi simulation dengan nilai 3600 dan 5
