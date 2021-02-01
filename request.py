import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'YearsExperience':2.1})

print(r.json())
