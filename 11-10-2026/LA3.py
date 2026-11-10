import requests

s = requests.Session()
s.get('http://httpbin.org/cookies')

r = s.get('http://httpbin.org/cookies')

print(r.text)

try:
    
    req = requests.get('https://www.geeksforgeeks.org/', timeout=0.000001)
    
except requests.exceptions.RequestException as e:
    
    raise SystemExit(e)