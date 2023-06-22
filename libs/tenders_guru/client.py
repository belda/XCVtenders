import requests


class TendersGuruClient:
    """
    Client to retrieve tenders from Tenders Guru API.
    doc: https://tenders.guru/pl/api
    """

    base_url = 'https://tenders.guru/api/'
    country = 'pl'  # TODO: expand for more sites

    def get(self, endpoint, params: dict | None = None):
        response = requests.get(f"{self.base_url}{self.country}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

    def get_tenders(self, page: int = 1):
        return self.get('tenders', {'page': page})['data']


tenders_guru_client = TendersGuruClient()
