#-*- coding:utf-8 -*-


from RedisTool import RedisTool

import string
import random

KEY_LEN = 20
KEY_ALL = 200

def base_str():
	return (string.ascii_letters + string.digits)

def key_gen():
	keylist = [random.choice(base_str()) for i in range(KEY_LEN)]
	return ("".join(keylist))

def add_gen(num = None):
    if num is None:
        num = 10

    redisTool = RedisTool('127.0.0.1', '6379')

    for i in range(num):
        redisTool.lpush('discount_list', key_gen())

if __name__ == '__main__':
	add_gen(KEY_ALL)