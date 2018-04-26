import requests

# Set the request parameters
url = 'https://dev57345.service-now.com/api/now/table/incident'

# Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'blah'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers ,data="{'short_description':'Example ticket created by CreateTicket program','assignment_group':'','urgency':'2','impact':'2'}")

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
