from bs4 import BeautifulSoup
import requests
import csv
import re
from urllib2 import urlopen
import json
from xml.dom import minidom
import ConfigParser
import sys

project_list="project_list.csv"

dataReader = csv.reader(open(project_list, 'rU'), delimiter=',', quotechar='"')

#read in tsv for valid ITTC services
for row in dataReader:
	#skips first row
	if row[0] != 'id':
		print row[0]

		json_return = requests.get('http://tasks.hotosm.org/project/' + row[0] + '.json')  
		data = json_return.json()
		with open('project_' + row[0] +'.geojson', 'w') as f:
			json.dump(data, f)


