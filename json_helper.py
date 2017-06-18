import json
import errno


def write_list(file_name, key, data):
	with open(file_name, 'r+') as json_file:
		# read json string from file and load it as a python dict
		json_list = json.load(json_file)

		# add new item to sub list
		json_list[key].append(data)

		# go to beginning of file and write new dict
		json_file.seek(0)
		json.dump(json_list, json_file)

		# truncate old dict
		json_file.truncate()

def get_list(file_name, key=None, key_compare=None):
	try:
		with open(file_name, 'r') as json_file:
			# read json string from file and load it as a python dict
			json_list = json.load(json_file)

			# check if key exists and if we have a match
			if key is not None:
				for list_item in json_list.values()[0]:
					if list_item[key] == key_compare:
						# if we do return it
						return list_item
			else:
				# if we don't have a match, return all items
				return json_list
	except ValueError, e:
		print("No Items")