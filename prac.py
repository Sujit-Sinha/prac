from multiprocessing import Process,Queue
def squares(q,num):
    for n in num:
        q.put(n*n)

def prints(q):
    while not q.empty():
        print(' {}'.format(q.get()))

if __name__=='__main__':
    q=Queue()
    num=[2,4,5]

    p1=Process(target=squares,args=(q,num))
    p2=Process(target=prints,args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("done")
