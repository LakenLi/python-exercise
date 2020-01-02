# -*- coding: utf-8 -*-
# @Author: HoRan.li
# @Date:   2020-01-02 22:20:13
# @Last Modified by:   HoRan.li
# @Last Modified time: 2020-01-02 22:37:50
# @E-mail: laken_phil@163.com

"""
Function Information:
模拟使用多进程和不使用多进程的差别
以下的例子不使用多进程
"""

from random import randint
from time import time, sleep

def download_task(filename):
	print('开始下载%s....' % filename)
	time_to_download = randint(5, 10)
	sleep(time_to_download)
	print('%s下载完成！耗费了%d秒' % (filename, time_to_download))

def main():
	start = time()
	download_task('hah.pdf')
	download_task('wao.html')
	end = time()
	print('总共耗费了%.2f秒' % (end - start))

if __name__ == '__main__':
	main()
