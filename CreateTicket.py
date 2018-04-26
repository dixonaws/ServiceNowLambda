import requests
import boto3

clientSsm=boto3.client('ssm')

# get the servicenow dev instance's url, username and pwd from the secure stirng store
snow_dev_instance=clientSsm.get_parameter(
    Name='snow_dev_instance',
    WithDecryption=True
)

snow_dev_username=clientSsm.get_parameter(
    Name='snow_dev_username',
    WithDecryption=True
)

snow_dev_pwd=clientSsm.get_parameter(
    Name='snow_dev_pwd',
    WithDecryption=True
)

snow_dev_instance=snow_dev_instance['Parameter']['Value']
snow_dev_username=snow_dev_username['Parameter']['Value']
snow_dev_pwd=snow_dev_pwd['Parameter']['Value']

print "Using parameters: instance=" + snow_dev_instance + ", username=" + snow_dev_username + ", password=" + snow_dev_pwd

url = 'https://' + str(snow_dev_instance) + '.service-now.com/api/now/table/incident'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.post(url, auth=(snow_dev_username, snow_dev_pwd), headers=headers, data="{'short_description':'Example ticket created by CreateTicket program','assignment_group':'','urgency':'2','impact':'2'}")

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
