import requests

url = "https://www.gutenberg.org/files/1112/1112-0.txt"

try:
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    print(type(response))
    print(response.ok)
    print(len(response.content))
    print(response.text[:500])

except requests.RequestException as e:
    print("Error:", e)