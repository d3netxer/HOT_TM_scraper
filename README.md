# HOT_TM_scraper
downloads extents of projects from HOT Tasking Manager

In this example I have downloaded the extents from projects set-up for the Nepal Earthquake in 2015

Run HOT_TM_scraper_search.py with a search term. It will create geojsons of the project extent that match your search term and record the project names in the search_results.csv

The script cannot find archived projects

You can then refine your project list in the project_list.csv

The HOT_TM_scraper_project_list.py will read the projects in the project_list.csv to generate the geojsons of the project extents
