import requests

def fetch(url: str) -> str:
    response = requests.get(
        url,
        timeout=15,
    )

    response.raise_for_status()

    return response.text