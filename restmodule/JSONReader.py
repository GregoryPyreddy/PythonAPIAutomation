import json
class JSONReader:
    def __init__(self): 
        print("Object Created")
    def readJSON(self, testName):
        print(testName)
        testdata = []
        with open('testdata/testdata.json') as f:
            data = json.load(f)
            if(testName == "All"):
                keylist = data.keys()
                for key in keylist:
                    testdata.append(data[key])
            else:   
                testdata.append(data[testName]) 
        return testdata