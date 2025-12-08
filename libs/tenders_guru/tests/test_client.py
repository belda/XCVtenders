import responses

from libs.tenders_guru.client import tenders_guru_client


@responses.activate
def test_client(tenders_guru_client_mock):

    result = tenders_guru_client.get_tenders()
    assert len(result) == 100
