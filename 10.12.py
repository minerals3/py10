import webbrowser
from urllib.parse import quote

query = input("Enter programming query: ")
url = "https://stackoverflow.com/search?q=" + quote(query)

print("Opening:", url)
webbrowser.open(url)