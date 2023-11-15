'''
Author: LetMeFly
Date: 2023-11-15 18:31:20
LastEditors: LetMeFly
LastEditTime: 2023-11-15 18:32:07
'''
import requests

response = requests.get('http://narc.letmefly.xyz/日常共享/../..')
print(response)
print(response.text)
