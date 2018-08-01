import pymysql
import string
import random
import time

"""
将生成的优惠券写入数据库
"""

KEY_LEN = 20
KEY_ALL = 200

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PWD = 'Horan@mysql#0312'

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

def mysql_connect():
	db = pymysql.connect(MYSQL_HOST, MYSQL_HOST, MYSQL_PWD)
	return db

def add_gen(num = None):
	if num is None:
		num = 10

	currentDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	db = mysql_connect()
	cursor = db.cursor()

	try:
		for i in range(num):
			gen = key_gen()
			sql = "INSERT INTO discount_info(discount_key, created_at) \
       		VALUES ('%s', '%s')" % (gen, currentDate)
       		cursor.execute(sql)

       	db.commit()
    except:
    	db.rollback()

    db.close()


if __name__ == '__main__':
	add_gen(KEY_ALL)





