import requests
class RequestBuilder:
    def buildRequest(self, url, mthd, headers, params, body):
        req = requests.Request(mthd, url, headers=headers, params=params, data=body )
        r = req.prepare()
        # response = requests.get(url)
        return r
    def buildRequestMultipart(self, url, mthd, headers, params, body):
        req = requests.Request(mthd, url, headers=headers, params=params, data=body )
        reqObj = req.prepare()
        # response = requests.get(url)
        return reqObj
    def __init__(self): 
        print("Object Created")
    def executeRequest(self, r):
        s = requests.session()
        response = s.send(r)
        return response
