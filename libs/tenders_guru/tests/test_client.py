from apiimporter.client import tenders_guru_client


def test_client():
    result = tenders_guru_client.get_tenders()
    assert len(result) == 100
