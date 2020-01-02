# -*- coding: utf-8 -*-
# @Author: HoRan.li
# @Date:   2020-01-02 22:34:21
# @Last Modified by:   HoRan.li
# @Last Modified time: 2020-01-02 22:49:17
# @E-mail: laken_phil@163.com

"""
Function Information:
模拟使用多进程和不使用多进程的差别
以下的例子使用多进程
"""

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
	print('启动下载进程，进程号[%d].' % getpid())
	print('开始下载%s...' % filename)
	time_to_download = randint(5, 10)
	sleep(time_to_download)
	print('%s下载完成!耗费了%d秒' % (filename, time_to_download))


def main():
	start = time()
	p1 = Process(target = download_task, args = ('haha.pdf',))
	p1.start()
	p2 = Process(target = download_task, args = ('asdf.html',))
	p2.start()
	p1.join()
	p2.join()
	end = time()
	print('总共耗费了%.2f秒' % (end - start))


if __name__ == '__main__':
	main()