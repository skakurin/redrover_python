from http.client import responses

import pytest
from allure_commons import fixture

from lesson1.api_tests.case.pom.case import create_case
from lesson1.api_tests.case.models.case import Case
from lesson1.api_tests.case.data.case import create_case_dict
from lesson1.api_tests.utils.api_client import client
from lesson1.api_tests.tests.conftest import get_case_id

# def test_create_case():
#     response = create_case(Case(**create_case_dict).model_dump())
#     response.status_code_should_be_eq(200)
#     response.json_should_be_eq(Case(**create_case_dict).model_dump())
#     response.schema_should_be_eq(Case(**create_case_dict).model_json_schema())

def test_create_case_without_id():
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
    response.status_code_should_be_eq(200)

def test_create_case_without_name():
    response = client.make_request(
        handle="/testcases",
        method="POST",
        json={
            "id": "123",
            "description": "test description",
            "steps": [
                "step 1"
            ],
            "expected_result": "test expected result",
            "priority": "высокий"

        }
    )
    response.status_code_should_be_eq(422)

def test_get_case_by_id(get_case_id):
    response = client.make_request(
        handle=f"/testcases/{get_case_id}",
        method="GET"
    )
    response.status_code_should_be_eq(200)

def test_get_all_cases():
    response = client.make_request(
        handle=f"/testcases",
        method="GET"
    )
    response.status_code_should_be_eq(200)

def test_update_case(get_case_id):
    response = client.make_request(
        handle=f"/testcases/{get_case_id}",
        method="PUT",
        json={
            "id": f"{get_case_id}",
            "name": "test new name",
            "description": "test description",
            "steps": [
                "step 1"

            ],
            "expected_result": "test expected result",
            "priority": "низкий"

        }
    )
    response.status_code_should_be_eq(200)

def test_delete_case(get_case_id):
    response = client.make_request(
        handle=f"/testcases/{get_case_id}",
        method="DELETE"
    )
    response.status_code_should_be_eq(200)


