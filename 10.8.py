import webbrowser
from urllib.parse import quote

address = input("Enter address: ")
url = "https://www.google.com/maps/search/?api=1&query=" + quote(address)

print("Opening:", url)
webbrowser.open(url)