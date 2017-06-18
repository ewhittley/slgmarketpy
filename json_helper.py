import json


def write_list(file_name, key_name, data):
	with open(file_name, 'r+') as json_file:
		json_list = json.load(json_file)

		json_list[key_name].append(data)

		json_file.seek(0)
		json.dump(json_list, json_file)
		json_file.truncate()