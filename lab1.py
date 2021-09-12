from multiprocessing import Queue, Process
import time

def write_to(container, arr):
    for data in arr:
        container.put(data)
        


def read_from(container):
    time.sleep(0.5)
    while not container.empty():
        print('Printing from P2 {}'.format(container.get()**2))


if __name__ == '_main_':

    # Create Queue object
    Q=Queue()
    # Create Process class objects
    val_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    P1 = Process(target=write_to, args=(Q, val_list,))
    P2 = Process(target=read_from, args=(Q,))
    
    P1.start()
    P2.start()
    # Hold until both are terminated
    P1.join()
    P2.join()
    print('========== Exchange of Data tested =============')