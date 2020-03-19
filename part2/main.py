import os
import argparse
from src.api import get_data

if __name__ == "__main__":

	app_key = os.getenv('APP_KEY')

	parser = argparse.ArgumentParser()
	parser.add_argument("--page_size", type=int)
	parser.add_argument("--num_pages", default=None, type=int)
	parser.add_argument("--output", default=None)
	parser.add_argument("--elastic", default=False, type=bool)
	args = parser.parse_args()

	data = get_data(app_key, args.page_size, args.num_pages, args.elastic)
	

	
	with open(args.output, "w") as file:
		for i in data:
			for dic in i:
				file.write(f"{dic}"+'\n')
			