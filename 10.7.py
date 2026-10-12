import webbrowser
from urllib.parse import quote

topic = input("Enter topic: ")
url = "https://en.wikipedia.org/wiki/Special:Search?search=" + quote(topic)

print("Opening:", url)
webbrowser.open(url)