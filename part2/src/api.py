from sodapy import Socrata
from src.elasticsearch import create_and_update_index, push_data

 
def get_data(app_key, page_size,num_pages,elastic):

	client = Socrata("data.cityofnewyork.us", app_key)
	results = []

	rows = client.get("nc67-uf89", select="COUNT(*)")

	if not num_pages:
		num_pages = (rows // page_size) + 1

	if elastic:
		es = create_and_update_index('bigdata')

	for x in range(0, num_pages):
			records = client.get("nc67-uf89", limit=page_size, offset=x*(page_size))
			results.append(records)
			for r in records:
				if elastic:
					push_data(r, es, 'bigdata')
	return results