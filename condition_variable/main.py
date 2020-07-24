import time
import threading
from threading import Condition

class Job(object):

    def __init__(self):
        self._stop = False

    def __call__(self, num, cv):
        print("start: ", num)
        cv.acquire()
        while not self._stop:
            print("num: ", num)
            cv.wait()
        print("end: ", num)
        cv.release()

    def stop(self):
        self._stop = True


def notify_all(cv):
    cv.acquire()
    cv.notify_all()
    cv.release()


def main():
    threads = []
    cv = Condition()
    job = Job()
    for num in range(5):
        thread = threading.Thread(target=job, args=(num, cv))
        threads.append(thread)
        thread.start()
    for notify in range(3):
        notify_all(cv)
        time.sleep(0.3)
    job.stop()
    notify_all(cv)
    for th in threads:
        th.join()


if __name__ == '__main__':
    main()
