# -*- coding: utf-8 -*-
# @Author: HoRan.li
# @Date:   2019-12-09 22:34:36
# @Last Modified by:   HoRan.li
# @Last Modified time: 2019-12-09 22:40:30
# @E-mail: laken_phil@163.com

"""
Function Information:
生成指定长度的验证码
"""

import random

def generate_code(code_len = 4):
	"""
	生成指定长度的验证码

    :param code_len: 验证码的长度(默认4个字符)

    :return: 由大小写英文字母和数字构成的随机验证码
	"""

	all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	last_pos = len(all_chars) - 1
	code = ''
	for _ in range(code_len):
		index = random.randint(0, last_pos)
		code += all_chars[index]
	return code

def main():
	code_len = int(input('请输入验证码的长度:'))
	code = generate_code(code_len)

	print(code)

if __name__ == '__main__':
	main()