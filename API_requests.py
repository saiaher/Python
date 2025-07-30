import json
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
s1 = requests.get(url)
print(s1)
print(s1.json())

import requests

url = "https://api.github.com/users/octocat"
response = requests.get(url)
data = response.json()
print(data["login"])  # Output: octocat
