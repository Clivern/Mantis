"""
Mantis - A Minimalist Database Toolkit for Python

@author: Clivern U{hello@clivern.com}
"""

import sqlite3

class SQLite(object):

	_configs = {}
	_conn = False
	_cursor = False

	def __init__(self, configs):
		self._configs = configs
		return self

	def set_connection(self):
		self._conn = sqlite3.connect(_configs.db)
		self._cursor = self._conn.cursor()
		return self

	def get_connection(self):
		return self._conn

	def execute(self, query):
		return  self._cursor.execute(query)

	def build_table(self, query):
		return  self._cursor.execute(query)

	def get(self):
		pass

	def insert(self):
		pass

	def bulk_insert(self):
		pass

	def update(self):
		pass