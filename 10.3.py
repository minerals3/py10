import webbrowser
from urllib.parse import quote

query = input("Enter search query: ")
url = "https://www.google.com/search?q=" + quote(query)

print("Opening:", url)
webbrowser.open(url)