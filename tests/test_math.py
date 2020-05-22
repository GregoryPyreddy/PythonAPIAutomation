import pytest
from restmodule.RequestBuilder import RequestBuilder
from restmodule.JSONReader import JSONReader

def get_data():
    testName=""
    with open('config.txt', 'r') as myfile:
        testName = myfile.read()
    print(testName)
    obj1 = JSONReader()
    testdata = obj1.readJSON("All")
    for row in testdata:
        yield row

@pytest.mark.parametrize("testdata", get_data())
def test_request_All(testdata):
    url = testdata["url"]
    mthd = testdata["method"]
    headers=""
    params=""
    body=""
    expStatusCod = testdata["expectedStatusCode"]
    obj1 = RequestBuilder()
    r = obj1.buildRequest(url, mthd, headers, params, body)
    response = obj1.executeRequest(r)
    print(response.content)
    assert response.status_code == expStatusCod