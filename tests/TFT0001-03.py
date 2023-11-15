import requests

response = requests.get('http://narc.letmefly.xyz/日常共享/..')
print(response)
print(response.text)
