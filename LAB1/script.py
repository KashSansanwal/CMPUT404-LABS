import requests

print(requests.__version__)

print(requests.get('http://google.com/').content)

print("____________________________________________________________________________________________________________________________")
print(requests.get('https://raw.githubusercontent.com/KashSansanwal/CMPUT404-LABS/main/LAB1/script.py').text)