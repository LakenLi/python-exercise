# -*- coding: utf-8 -*-
# @Author: HoRan.li
# @Date:   2019-12-10 22:44:32
# @Last Modified by:   HoRan.li
# @Last Modified time: 2019-12-10 22:49:05
# @E-mail: laken_phil@163.com

"""
Function Information:
python对象属性访问可见性问题
"""

class Test:
	"""docstring for Test"""

	def __init__(self, foo):
		self.__foo = foo

	def __bar(self):
		print(self.__foo)
		print('__bar')


def main():
	test = Test('hello')

	test.__bar()

	print(test.__foo)

if __name__ == "__main__":
	main()
