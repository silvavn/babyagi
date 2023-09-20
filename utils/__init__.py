import requests


def get_embeddings(url: str, text: str) -> dict:
    payload = {"content": text}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def get_completion(url: str, prompt: str, **kwargs) -> dict:
    payload = {"prompt": prompt, **kwargs}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    return response.json()
