#!/usr/bin/python3
import requests

response = requests.get("https://api.open-notify.org/this-api-doesnt-exist")

print(response.status_code)