#-*- coding:utf-8 -*-

import os
import sys
import re

"""
统计纯英文文本内单词出现的个数
"""

def doCount(path = None):
	if path is None:
		path = '/Users/apple/python-exercise/0005/test.txt'

	count = 0
	with open(path, 'r', errors='ignore') as f:
		line = f.read().split()
		print(line)
		count += len(line)

	
	return count
	
	

if __name__ == '__main__':
	path = '/Users/apple/python-exercise/0005/test.txt'
	count = doCount(path)
	print(count)