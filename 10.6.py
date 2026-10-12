import webbrowser
from urllib.parse import quote

query = input("Enter YouTube search: ")
url = "https://www.youtube.com/results?search_query=" + quote(query)

print("Opening:", url)
webbrowser.open(url)