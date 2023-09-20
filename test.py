import requests


def get_embedding(url: str, text: str) -> dict:
    payload = {"content": text}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    return response.json()


def get_completion(url: str, prompt: str, **kwargs) -> dict:
    payload = {"prompt": prompt, **kwargs}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    return response.json()


url = "http://localhost:8080/embedding"
objective = "Buy a house in Edmonton Alberta"
context = ""
task = f"Make a list of tasks that must be fulfilled in order to complete the goal of {objective}"

prompt = f"Perform one task based on the following objective: {objective}.\n"

if context:
    prompt += "Take into account these previously completed tasks:" + "\n".join(context)
prompt += f"\nYour task: {task}\nResponse:"


payload = {
    "prompt": prompt,
    "content": "hello",
    "n_predict": 2048,
    "mirostat": 2,
    "temperature": 0.7,
    "top_p": 0.9,
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

# transform response to json
response = response.json()

print(response)
