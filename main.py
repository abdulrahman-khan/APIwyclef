
url = "https://api.example.com/data"

# Headers (if needed)
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

# Make a GET request
response = requests.get(url, headers=headers)

# Check the response status
if response.status_code == 200:
    print("Response Data:", response.json())
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}, Error: {response.text}")