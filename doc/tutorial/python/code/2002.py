import requests

# response = requests.get('http://mirrors.sohu.com/')
# print(response.text)

# print (type(response))


# payload = {'key1': 'value1', 'key2': 'value2'}

# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)

# headers = {
#     'user-agent': 'my-app/0.0.1', 
#     'auth-type': 'jwt-token'
# }

# r = requests.post("http://httpbin.org/post", headers=headers)
# print(r.text)

r = requests.post("http://httpbin.org/post", data={1:1,2:2})
print(r.json())