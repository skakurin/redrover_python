import pytest
from lesson1.api_tests.utils.api_client import client

@pytest.fixture(scope="module")
def get_case_id():
    response = client.make_request(
        handle="/testcases",
        method="POST",
        json={
            "name": "test name",
            "description": "test description",
            "steps": [
                "step 1"
            ],
            "expected_result": "test expected result",
            "priority": "высокий"

        }
    )
    return response.get_value_with_key("id")