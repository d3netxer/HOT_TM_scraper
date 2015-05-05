from bs4 import BeautifulSoup
import requests
import csv
import re
from urllib2 import urlopen
import json

search_term = "Nepal+Earthquake"

search_results = ["id","description"]

with open('search_results_csv.csv', 'w') as f:

	writer = csv.writer(f)

	writer.writerow(search_results)

	#num of page results
	r = requests.get("http://" + "tasks.hotosm.org/?sort_by=created&direction=desc&search=" + search_term)
	data0 = r.text
	soup = BeautifulSoup(data0)
	#http://stackoverflow.com/questions/5041008/handling-class-attribute-in-beautifulsoup
	pages = soup.findAll("div", { "class" : "btn-group btn-group-xs" })
	#print(pages)
	num_list = []
	for child in pages[0].children:
		#print(child.string)
		try:
			#print(int(child.string))
			num_list.append(int(child.string))
		except ValueError:
			print("not a literal, continue")
	print(max(num_list))
	max_page=max(num_list)+1
		

	for num in range(1,max_page):
		print(num)
		#not able to retrieve archived projects
		r = requests.get("http://" + "tasks.hotosm.org/?direction=desc&page=" + str(num) + "&search=" + search_term + "&sort_by=created")

		data = r.text

		#print(data)

		soup = BeautifulSoup(data)

		alltr = soup.find_all('h3')

		#print(alltr)

		new_list = {}

		for element in alltr:

			print(element)

			if 'Projects' in element:

				print('got it!')

				#print("printing element parent: ")
				#print(element.parent)

				project_numbers = element.parent.find_all('h4')
		
				#print("printing project numbers: ")
				#print(project_numbers)

				for child in project_numbers:

					project_num_and_string = child.a.contents[0].strip()
			
					print(project_num_and_string)

					split = re.split('(\D+)(\d+)', project_num_and_string)

					print(split[2])

					print(split[3:])

					new_list = (split[2],split[3:])

					writer.writerow(new_list)
					
					#http://stackoverflow.com/questions/17518937/saving-a-json-file-to-computer-python
					#json_return = requests.get('http://tasks.hotosm.org/project/' + split[2] + '/tasks.json')
					json_return = requests.get('http://tasks.hotosm.org/project/' + split[2] + '.json')  
					data = json_return.json()
					with open('project_' + split[2] +'.json', 'w') as f:
						json.dump(data, f)
						
					#consider doing a merge of geoJSONs with Shapely (python geos library)
					#http://pydoc.net/Python/Shapely/1.2.10/shapely.examples.dissolve/
					#http://bl.ocks.org/mbostock/5416405
					#http://gis.ibbeck.de/ginfo/apps/OLExamples/OL27/examples/intersection%20of%20features.asp

		






                    
 
                    


        
