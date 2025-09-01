import requests

try:
        r = requests.get("https://casestack.com")
        print("site is up",r.status_code)
except Exception as e:
        print("site down",e)