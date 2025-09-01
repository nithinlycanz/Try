import json

# with open("data.json","r") as f :
#     data = json.loads(f)
#     print(data)
data = '''
{
  "user": {
    "id": 101,
    "name": "Nithin",
    "role": "SRE Intern"
}
}
'''
extracted = json.loads(data)
print("name =",extracted["user"]["name"])
print(extracted["user"]["id"])
