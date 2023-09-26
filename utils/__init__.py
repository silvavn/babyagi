import requests
from chromadb.api.types import Documents, EmbeddingFunction, Embeddings

def get_embedding(text: str, url: str = "http://localhost:8080", **kwargs) -> dict:
    payload = {"content": text}
    payload.update(kwargs)
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(f"{url}/embedding", json=payload, headers=headers)
        return response.json()["embedding"]
    except Exception as e:
        print(e)
        print("PAYLOAD:", payload)
        print("RESPONSE:", response)
        return None

def get_completion(prompt: str, url: str = "http://localhost:8080", **kwargs) -> dict:
    payload = {"prompt": prompt}
    payload.update(kwargs)
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(f"{url}/completion", json=payload, headers=headers)
        return response.json()["content"]
    except Exception as e:
        print(e)
        print("PAYLOAD:", payload)
        print("RESPONSE:", response)
        return None

# Llama embedding function
class LlamaEmbeddingFunction(EmbeddingFunction):
    def __init__(self, LLAMA_API_PATH: str = "http://localhost:8080"):
        self.LLAMA_API_PATH = LLAMA_API_PATH

    def __call__(self, texts: Documents) -> Embeddings:
        embeddings = []
        for t in texts:
            e = get_embedding(t, self.LLAMA_API_PATH)
            embeddings.append(e)
        return embeddings
    
    def embed_documents(self, texts: Documents) -> Embeddings:
        return self(texts)
    
    def embed_query(self, text: str) -> Embeddings:
        return self([text])[0]