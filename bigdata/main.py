import os
import sys

from src.api import get_data

if __name__ == "__main__":

	app_key = os.getenv('APP_KEY')

	list1 = sys.argv[1:]
	page_size = list1[0]
	num_pages = list1[1]
	output = list1[2]

	data = get_data(app_key, page_size, num_pages)
	print(data)

	
	with open(output, "w") as file:
		for i in data:
			for dic in i:
				file.write(f"{dic}"+'\n')
			