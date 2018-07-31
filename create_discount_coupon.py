##生成优惠券
##-*- coding:utf-8 -*-
# import string #导入string这个模块
# print string.digits  #输出包含数字0~9的字符串
# print string.lowercase #包含所有小写字母的字符串
# print string.uppercase  #包含所有大写字母的字符串
# print string.punctuation #包含所有标点的字符串
# print string.ascii_letters #与string.letters一样
#

import string
import random

"""
生成优惠券的第一种方式
def rand_gen(lenght = 8):
	string = 'abcdefghijkmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZ1234567890';
	gen = []

	while(len(gen) < lenght):
		index = random.randint(0, len(string) - 1)
		
		rand = string[index]

		gen.append(rand)
	

	return ''.join(gen)


def create_discount(num):
	discount = [];
	for i in range(1, num):
		discount.append(rand_gen())

	return discount;


if __name__ == '__main__':
	discount = create_discount(200)
	print(discount)
"""

###网上作者的写法，与上面自己的比较，模块用的不熟

KEY_LEN = 20
KEY_ALL = 200

def base_str():
	return (string.ascii_letters + string.digits)

def key_gen():
	keylist = [random.choice(base_str()) for i in range(KEY_LEN)]
	return ("".join(keylist))

def key_num(num, result = None):
	if result is None:
		result = []
	for i in range(num):
		result.append(key_gen())
	return result

def print_key(num):
	for i in key_num(num):
		print(i)

if __name__ == '__main__':
	print_key(KEY_ALL)








