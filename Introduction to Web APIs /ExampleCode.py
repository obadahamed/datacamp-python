import requests

url = "https://api.github.com/users/octocat"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Name:", data["name"])
    print("Public Repos:", data["public_repos"])
    print("Followers:", data["followers"])
else:
    print("Request failed with status:", response.status_code)
