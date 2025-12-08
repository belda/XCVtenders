import json

import pytest
import responses

@pytest.fixture
def tenders_guru_client_mock():
    with open('libs/tenders_guru/tests/mock/get_tenders_response.json', 'r') as f:
        responses.add(
            responses.GET,
            "https://tenders.guru/api/pl/tenders",
            json=json.load(f),
            status=200,
        )