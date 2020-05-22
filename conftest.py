# import tesults
import pytest
from restmodule.JSONReader import JSONReader
def pytest_addoption(parser):
    parser.addoption("--testName", action="store")

@pytest.fixture(scope='session')
def testName(request):
    testname_value = request.config.option.testName
    if testname_value is None:
        pytest.skip()
    return testname_value