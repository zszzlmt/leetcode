from threading import Semaphore


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.r = ""
        self.semas = (Semaphore(1), Semaphore(0), Semaphore(1), Semaphore(0))

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.semas[0].acquire()
            printNumber(0)
            self.semas[1].release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 2 == 1:
                self.semas[2].acquire()
                self.semas[1].acquire()
                printNumber(i)
                self.semas[0].release()
                self.semas[3].release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 2 == 0:
                self.semas[3].acquire()
                self.semas[1].acquire()
                printNumber(i)
                self.semas[0].release()
                self.semas[2].release()