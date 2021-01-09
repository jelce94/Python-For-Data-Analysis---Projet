import requests
import json

url = 'http://0.0.0.0:5000/api/'

data = {
		'values': [[8.00000e+00,0.00000e+00, 3.80000e+01, 0.00000e+00, 4.37000e+03, 7.10000e+01,
    	5.00000e+00, 1.70000e+01, 3.00000e+00, 1.00000e+00, 1.00000e+00,
       	3.00000e+01, 6.97640e+01]],
       	'model': 'RF'
       }
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)
