from threading import Thread
import time
import random


class ChildThreadClass_1(Thread):
    # Overridding Parent class constructor:
    def __init__(self, count, num):

    # Call Parent class constructor (anyone):
       super().__init__()
       # Thread.__init__(self)
       self.limit = count
       self.id = num

    # This methods invokes automatically while thread.start() is called:
    def run(self):
       for i in range(1, self.limit + 1):
          val = random.randint(0, 5)
          time.sleep(val)
          print('Thread No - [{}] : Count : {}, T1'.format(self.id, i))


class ChildThreadClass_2(Thread):
    # Overridding Parent class constructor:
    def __init__(self, count, num):

        # Call Parent class constructor (anyone):
        super().__init__()
        # Thread.__init__(self)
        self.limit = count
        self.id = num

    # This methods invockes automatically while thread.start() is called:
    def run(self):
        for i in range(1, self.limit + 1):
           val = random.randint(0, 5)
           time.sleep(val)
           print('Thread No - [{}] : Count : {}, T2'.format(self.id, i))
if __name__ == '__main__':
        thread_list = []
        # Create & Run Thread-1
        count_val = 10
        thread_num = 1
        th1 = ChildThreadClass_1(count_val, thread_num)
        th1.start()
        thread_list.append(th1)
        # Create & Run Thread-2
        count_val = 10
        thread_num = 2
        th2 = ChildThreadClass_2(count_val, thread_num)
        th2.start()
        thread_list.append(th2)
        # Join all threads:
        for thds in thread_list:
            thds.join()


print('Exit from main process')
