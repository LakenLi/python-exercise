# encoding: utf-8

year = int(input('please innput year:'))
is_leap = (year % 4 == 0 and year % 100 != 0) or \
	year % 400 == 0

print(is_leap)	