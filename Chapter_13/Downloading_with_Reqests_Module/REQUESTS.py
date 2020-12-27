import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(res.status_code) # print status code (200 means ok)
# print(res.text[:300]) # print the first 300 letters
res.raise_for_status() # do nothing when error detected
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)


