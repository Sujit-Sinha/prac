from threading import Thread
import time
import random


class ChildThreadClass(Thread):
    # Overridding Parent class constructor:
    def __init__(self, count, num):

        # Call Parent class constructor (anyone):
        super().__init__()
        # Thread.__init__(self)
        self.limit = count
        self.id = num

    # This methods invokes automatically while thread.start() is called:
    def run(self):
       for i in range(1,self.limit+1):
          val = random.randint(0, 5)
          time.sleep(val)
          print('Thread No - [{}] : Count : {}'.format(self.id, i))


if __name__ == '__main__':
        thread_list = []
        # Create & Run Thread-1
        count_val = 10
        thread_num = 1
        th = ChildThreadClass(count_val, thread_num)
        th.start()
        thread_list.append(th)
        # Create & Run Thread-2
        count_val = 5
        thread_num = 2
        th = ChildThreadClass(count_val, thread_num)
        th.start()
        thread_list.append(th)
        # Join all threads:
        for thds in thread_list:
           thds.join()


print('Exit from main process')
