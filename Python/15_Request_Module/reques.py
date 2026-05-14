# This is a requests module example like sending get and post request 
import requests
# Sending a GET request
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    print("GET Request Successful")
    
else:
    print("GET Request Failed with status code:", response.status_code)