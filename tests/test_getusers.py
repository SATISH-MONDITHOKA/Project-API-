import pytest
from utils.apis import APIS

@pytest.fixture(scope='module')
def apis():
    return APIS()  # Create and return an instance of APIS

def test_getusers_validation(apis):
    response = apis.get(endpoint='')  # Use the instance returned by the fixture
    print(response.json())  # Print the JSON response for debugging
    assert response.status_code == 200  # Validate the status code is 200
    assert len(response.json()) > 0  # Validate the JSON response is not empty












