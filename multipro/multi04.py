import multiprocessing as mp

def job(x):
    return x*x

# 进程池
def multicore():
    # 定义一下进程池
    # 邦定特定的功能
    # 将数据传入就能返回结果 
    # 自动将任务分配给不同的核心
    pool = mp.Pool()
    res = pool.map(job,range(1000000))
    print(res)

if __name__ == "__main__":
    multicore()

