import multiprocessing as mp
import time
def job(l,p,v,num):
    # lock
    # 只有一个循环结束，其它进程才能用共享变量 v 进行运算
    l.acquire()
    for _ in range(10):
        time.sleep(0.1)
        v.value += num
        print(p,' : ',v.value)
    # unlock
    l.release()

def multicore():
    v = mp.Value('i',0) # share variable
    l = mp.Lock() # lock
    p1 = mp.Process(target=job,args=(l,'p11',v,1))
    p2 = mp.Process(target=job,args=(l,'p22',v,3))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == "__main__":
    multicore()