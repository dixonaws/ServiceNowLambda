# ServceNowPythonIntegration
Lambda function to create an Incident Record in ServiceNow

Note that you will need to package the Python program with dependencies for Lambda, e.g.: <code>zip -r CreateTicket.zip CreateTicket.py requests/ urllib3/ chardet/ certifi/ idna/</code>

You will also need to provide IAM permissions for your Lambda execution role to read from the Parameter Store.