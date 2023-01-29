import requests
response=requests.get('https://api.ipify.org')
print('your IP Address is: ',response.text)
