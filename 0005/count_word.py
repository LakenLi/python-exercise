#-*- coding:utf-8 -*-

import os
import sys
import re
import collections

"""
统计纯英文文本内单词出现的个数
"""

def doCount(path = None):
	if path is None:
		path = '/Users/apple/python-exercise/0005/test.txt'

	"""
	##统计总单词数
	count = 0
	with open(path, 'r', errors='ignore') as f:
		line = f.read().split()
		print(line)
		count += len(line)

	
	return count
	"""
	##统计各个单词出现的次数
	
	reObj = re.compile('\b?(\w+)\b?')
	
	words = dict()

	with open(path, 'r', errors='ignore') as f:
		word = reObj.findall(f.read())

		for wd in word:
			if wd.isdigit():
				continue
			if wd.lower() in words:
				words[wd.lower()] += 1
			else:
				words[wd] = 1

	for key, value in words.items():
		print('%s: %s' % (key, value))

	
	

if __name__ == '__main__':
	path = '/Users/apple/python-exercise/0005/test.txt'
	doCount(path)
	#print(count)