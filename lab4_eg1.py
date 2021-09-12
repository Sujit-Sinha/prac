from threading import Thread
import time
import random
# Thread-1 task:
def thread_1(count):
 for i in range(1,count+1):
  val=random.randint(0, 5)
 time.sleep(val)
 print('Thread No - [1] : Count : {}, T1'.format(i))
# Thread-2 task:
def thread_2(count):
 for i in range(1,count+1):
  val=random.randint(0, 5)
  time.sleep(val)
  print('Thread No - [2] : Count : {}, T2'.format(i))
# Main Process:
if __name__=='__main__':
 T1=Thread(target=thread_1, args=(10,))
 T2=Thread(target=thread_2, args=(10,))
 T1.start()
 T2.start()
 # while T1.is_alive():
 # print('T1 is alive')
 T1.join()
 T2.join()
print('Exit from main process')
