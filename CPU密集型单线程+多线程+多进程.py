"""
sigle_thread 单线程消耗--> 9.81250524520874
multi_thread 多线程消耗--> 10.769865989685059
multi_process 多进程消耗--> 1.9699451923370361
"""

import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

NUM = [10] * 10


def cpu_task(num):
    """cpu密集型任务"""
    tmp = 0
    for a in range(1000):
        for b in range(1000):
            for c in range(num):
                tmp += a + b + c


def sigle_thread():
    """单线程"""
    for i in NUM:
        cpu_task(i)


def multi_thread():
    """多线程"""
    with ThreadPoolExecutor() as pool:
        pool.map(cpu_task, NUM)


def multi_process():
    """多进程"""
    with ProcessPoolExecutor() as pool:
        pool.map(cpu_task, NUM)


if __name__ == '__main__':
    start_time = time.time()
    sigle_thread()
    end_time = time.time()
    print("sigle_thread 单线程消耗-->", end_time - start_time)


    start_time = time.time()
    multi_thread()
    end_time = time.time()
    print("multi_thread 多线程消耗-->", end_time - start_time)



    start_time = time.time()
    multi_process()
    end_time = time.time()
    print("multi_process 多进程消耗-->", end_time - start_time)