import urllib
import urllib2
import csv

# Defining the required watersheds as an example
i=['03333600','04180000','03298250']

# Loop for creating the reuird URLs

for n in i :
    # Building URL
    getVars = {'site_no': n}
    url1 = 'https://nwis.waterdata.usgs.gov/nwis/peak?search_'
    url2 = '&search_site_no_match_type=exact&group_key=NONE&sitefile_output_format=html_table&column_name=agency_cd&column_name=site_no&column_name=station_nm&set_logscale_y=1&format=rdb&date_format=YYYY-MM-DD&rdb_compression=value&hn2_compression=file&list_of_search_criteria=search_site_no'
    link = (url1 + urllib.urlencode(getVars) + url2)
    print (link)
    #Data Storing
    DataStore="W:\A4_Python\Homeworks\HW03\Result\Data_" + n + ".csv"
    response = urllib2.urlopen(link)
    html = response.read()
    with open(DataStore, 'wb') as f:
        f.write(html)





