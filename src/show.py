import sqlite3


def quick_read_record(database, how_many=10):
	conn = sqlite3.connect(database)
	cur = conn.cursor()
	query = '''SELECT * FROM {}'''.format('moz_places')
	cur.execute(query)
	print_more = None
	print(cur.description)
	for count, record in enumerate(cur):
		print(record[-3])
		print(record)
		if count % how_many == 0:
			print_more = input()
		if print_more:
			break


def print_records(record_gen, each_time=10, profile_name=None):
	import time
	if profile_name:
		print('\n' * 2, profile_name, '\n' * 2)
	time.sleep(2)
	print('Press ENTER key for the next set of records, c for number of records so far, any other to exit.\n\n')
	time.sleep(1)
	for srn, record in enumerate(record_gen):
		print(record)
		try:
			cond = srn % each_time == 0 and srn > 0
		except TypeError:
			pass
		else:
			if cond:
				quitter = input()
				if quitter in {'c', 'C'}:
					print(srn)
					time.sleep(1)
				elif quitter:
					break
				pass
