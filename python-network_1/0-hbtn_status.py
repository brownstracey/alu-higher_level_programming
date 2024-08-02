#!/usr/bin/python3
"""
0-hbtn_status.py
This script fetches the URL https://alu-intranet.hbtn.io/status using urllib
and displays the response body in a specified format.

It specifically:
- Fetches the response from the provided URL
- Prints the type of the response content
- Prints the raw content of the response
- Prints the UTF-8 decoded content of the response

import urllib.request

# URL to fetch
url = 'https://alu-intranet.hbtn.io/status'

# Using the with statement to open the URL
with urllib.request.urlopen(url) as response:
    body = response.read()  # Read the response content

    # Print details about the response body
    print("Body response:")
    print(f"\t- type: {type(body)}")  # Print the type of the body content
    print(f"\t- content: {body}")  # Print the raw bytes content
    print(f"\t- utf8 content: {body.decode('utf-8')}")  # Print the UTF-8 decoded content
