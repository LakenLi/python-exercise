# -*- coding: utf-8 -*-
# @Author: HoRan.li
# @Date:   2019-12-09 22:30:42
# @Last Modified by:   HoRan.li
# @Last Modified time: 2019-12-09 22:33:46
# @E-mail: laken_phil@163.com

"""
Function Information:
在屏幕上显示跑马灯文字
"""

import os
import time

def main():
	content = '哇哈哈哈哈哈哈哈------'

	while True:
		#清理屏幕上的输出
		os.system('clear')
		print(content)

		#休眠200毫秒
		time.sleep(0.2)
		content = content[1:] + content[0]


if __name__ == '__main__':
	main()
