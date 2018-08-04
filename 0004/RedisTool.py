#-*- coding:utf-8 -*-

import redis

class RedisTool:

	def __init__(self, host, port, pwd = '', db = 0):
		self.host = host
		self.port = port
		self.pwd = pwd
		self.db = db
		self.redisConnect = redis.Redis(self.host, self.port, self.db, self.pwd, decode_responses=True)

	def set(self, key, val):
		return self.redisConnect.set(key, val)

	def get(self, key):
		return self.redisConnect.get(key)

	def lpush(self, key, val):
		return self.redisConnect.lpush(key, val)

