import multiprocessing as mp

def job(x):
    return x*x

# 进程池
def multicore():
    # 定义一下进程池
    # 邦定特定的功能
    # 将数据传入就能返回结果 
    # 自动将任务分配给不同的核心
    pool = mp.Pool(processes=2) # prcesses 定义将任务分配给几个核心
    res = pool.map(job,range(10))
    print(res)
    # apply_async只能将任务分配给一个核心,只能有一个值
    res = pool.apply_async(job,(2,))
    print(res)
    # apply_asnyc如果想要多个值，等价于连续启动多个apply__sync
    # 每个apply_sync都由pool分配核心。
    multi_res = [pool.apply_async(job,(i,)) for i in range(10)]
    print([res.get() for res in multi_res]) # 迭代获取不同的res结果

    # map可以迭代很多个参数自动分配给不同的核心
    # apply_async只能一个，不过可以通过[]列表迭代同时启动多个
    # 实现 apply_async和map等价
if __name__ == "__main__":
    multicore()

    # 多进程中的共享内存
    # 多线程可以用globe 定义全局变量
    # 多进程不可以，因为数据是在不同的核心中，每下cpu
    # 都有自己的各自的共享内存，却不互通
    # 定义
    # value = map.Value('i',4) # i表示整数 值为4
    # value2 = map.Value('i',[1,2,3,4]) # 只能一维

