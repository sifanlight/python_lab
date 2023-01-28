import json

#   Part 1
print("Part 1:")
data = {
    'name': 'Sadra',
    'id': 97101972,
}
data_to_json = json.dumps(data, indent=4)
print("Data to json:")
print(data_to_json)
data_from_json = json.loads(data_to_json)
print("Data from json:")
print(data_from_json)
print(f"name: {data_from_json['name']}")
print(f"id: {data_from_json['id']}")

print("=" * 40)
#   Part 2
message = """
Bin '1673690991664-4441226008348'

No requests received yet.

Try one of these and refresh to see the results:

    curl -H 'X-Status: Awesome' https://www.toptal.com/developers/postbin/1673690991664-4441226008348
    wget https://www.toptal.com/developers/postbin/1673690991664-4441226008348?hello=world
    echo "hello=world" | POST https://www.toptal.com/developers/postbin/1673690991664-4441226008348
"""
print("Done")
print(message)
BIN_ID = "1673690991664-4441226008348"

print("=" * 40)
#   Part 3
import requests

url = f'https://www.toptal.com/developers/postbin/{BIN_ID}'
headers = {
    'Content-Type': 'application/xml',
    'X-Status': 'Awesome',
}

r = requests.post(url, data=data_to_json, headers=headers)
print(f"Data sent to {url} with code {r.status_code}")
#   status_code = 200 --> OK
r = requests.get(url, headers=headers)
print(f"Data got from {url} with code {r.status_code}:")
print(r.headers)
print(r.text)

# {
#     'Date': 'Sat, 14 Jan 2023 10:18:13 GMT',
#     'Content-Type': 'text/plain; charset=utf-8',
#     'Content-Length': '27',
#     'Connection': 'keep-alive',
#     'Etag': 'W/"1b-VP0fhMCoZbo3mTD+4+YzMqC5daA"',
#     'X-Response-Time': '1.13749ms',
#     'Via': '1.1 google',
#     'CF-Cache-Status': 'HIT',
#     'Age': '164',
#     'Expires': 'Sat, 14 Jan 2023 10:28:13 GMT',
#     'Cache-Control': 'public, max-age=600',
#     'Accept-Ranges': 'bytes',
#     'Vary': 'Accept-Encoding',
#     'Server': 'cloudflare',
#     'CF-RAY': '7895a058dbe15a43-MXP'
# }
