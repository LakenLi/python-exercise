# -*- coding: utf-8 -*-
# @Author: HoRan.li
# @Date:   2019-12-05 23:13:00
# @Last Modified by:   HoRan.li
# @Last Modified time: 2019-12-05 23:23:21
# @E-mail: laken_phil@163.com

"""
Function Information:
判断一个正整数是不是素数
"""

from math import sqrt

num = int(input('请输入一个正整数:'))
end = int(sqrt(num))

is_prime = True

for x in range(2, end + 1):
	if num % x == 0:
		is_prime = False
		break
if is_prime and num != 1:
	print('%d是素数' % num)
else:
	print('%d不是素数' % num)
