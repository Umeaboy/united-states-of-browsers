import sqlite3
import os


def connect_db(db_file):
	"""
	Establishes connection to the database file, returns connection, cursor objects and filename.
	:param db_file: Path of the database file.
	:type db_file: str/path-like object
	:return: conn, cur filename
	:rtype: connection object, cursor object, str
	"""
	# if not os.path.exists(db_file):
	#     print("ERROR: Invalid path. ({})".format(db_file))
	#     print("Quitting...")
	#     quit()
	conn = sqlite3.connect(database=db_file)
	cur = conn.cursor()
	return conn, cur, os.path.split(db_file)[1]


def _db_tables(cursor):
	"""
	Returns names of tables from the cursor object of the database file.
	:param cursor: Cursor object attached to the database file, from connect_db function.
	:type cursor: Connection.Cursor Object
	:return: list of table names in database file.
	:rtype: list['str']
	"""
	query = "SELECT name FROM sqlite_master WHERE type = 'table'"
	return [table_[0] for table_ in cursor.execute(query)]



