# -*- coding: utf-8 -*-
# @Author: HoRan.li
# @Date:   2019-12-05 23:19:02
# @Last Modified by:   HoRan.li
# @Last Modified time: 2019-12-05 23:34:43
# @E-mail: laken_phil@163.com

"""
Function Information:
输出100以内的所有的素数
"""

import math

for num in range(2, 100):
    is_prime = True
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end="," )