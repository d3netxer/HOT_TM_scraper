import csv
from xml.dom import minidom
import ConfigParser
from geojson import Polygon, MultiPolygon, Feature, FeatureCollection, GeometryCollection, Point
import geojson
import sys
import json

properties_to_add="../project_list.csv"

#http://stackoverflow.com/questions/17315635/csv-new-line-character-seen-in-unquoted-field-error
dataReader = csv.reader(open(properties_to_add, 'rU'), delimiter=',', quotechar='"')

unique_list = []

#read in tsv for valid ITTC services
for row in dataReader:
	#skips first row
	if row[0] != 'id':
		print row[0]
		print row[1]
		print row[2]


	try:
		json_data = open('project_'+row[0]+'.geojson')
		features = json.load(json_data)
		features2 = json.dumps(features)

		#print features2

		#print features["properties"]['name']

		features["properties"]['status'] = row[1]

		features["properties"]['pre_or_post_disaster'] = row[2]

		print features["properties"]

		with open('project_' + row[0] +'_2.geojson', 'w') as f:
				json.dump(features, f)

	except SyntaxError:
		print 'SyntaxError'
	except IOError:
		print 'IOError'

