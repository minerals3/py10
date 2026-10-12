import sys
import webbrowser
from urllib.parse import quote

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else:
    address = input("Enter address: ")

url = "https://www.openstreetmap.org/search?query=" + quote(address)
print("Opening:", url)
webbrowser.open(url)