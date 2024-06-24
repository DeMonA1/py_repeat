import requests


resp = requests.get('http://www.example.com')
resp
resp.status_code
resp.text[:50]