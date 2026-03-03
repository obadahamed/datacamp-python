# 🌐 Introduction to Web APIs in Python

![Platform](https://img.shields.io/badge/Platform-DataCamp-03EF62?style=flat-square&logo=datacamp&logoColor=black)
![Language](https://img.shields.io/badge/Language-Python-3776AB?style=flat-square&logo=python)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

> Notes and practical code from the DataCamp course: **Introduction to Web APIs in Python**.  
> Covers how to interact with web services using HTTP requests and process JSON data programmatically.

---

## 🎯 What I Learned

### 1. HTTP Requests with `requests`

```python
import requests

# GET — fetch data
response = requests.get("https://api.github.com/users/obadahamed")

# POST — send data
response = requests.post(url, json={"key": "value"})

# Check status
print(response.status_code)   # 200 = OK
print(response.json())        # Parse JSON response
```

### 2. Working with API Endpoints

```python
# Query parameters
params = {"search": "python", "per_page": 10}
response = requests.get("https://api.github.com/search/repositories", params=params)

# Headers (e.g. API key auth)
headers = {"Authorization": "Bearer YOUR_API_KEY"}
response = requests.get(url, headers=headers)
```

### 3. JSON Handling

```python
data = response.json()

# Access nested values
repos = data["items"]
for repo in repos:
    print(repo["name"], repo["stargazers_count"])
```

### 4. HTTP Status Codes

| Code | Meaning |
|------|---------|
| `200` | OK — request successful |
| `201` | Created — resource created |
| `400` | Bad Request — invalid input |
| `401` | Unauthorized — auth required |
| `403` | Forbidden — no permission |
| `404` | Not Found |
| `500` | Server Error |

### 5. Error Handling

```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()   # Raises exception for 4xx/5xx
    data = response.json()
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.ConnectionError:
    print("Connection failed")
except requests.exceptions.Timeout:
    print("Request timed out")
```

---

## 🔐 Security Applications

These skills are directly useful in cybersecurity for interacting with threat intel APIs, automating recon, and parsing data from security tools — see [Tools-and-Scripts](https://github.com/obadahamed/Tools-and-Scripts) for examples.

---

## 📁 Files

| File | Description |
|------|-------------|
| [ExampleCode.py](./ExampleCode.py) | Practical examples from the course |
| [README.md](./README.md) | This file |
