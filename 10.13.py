import webbrowser
from urllib.parse import quote

query = input("Enter repository topic: ")
url = "https://github.com/search?q=" + quote(query) + "&type=repositories"

print("Opening:", url)
webbrowser.open(url)