import requests as req

r = req.get('https://www.geeksforgeeks.org/',)

print(r)

print(r.text[0:1000])