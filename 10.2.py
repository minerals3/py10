import webbrowser
from urllib.parse import quote

try:
    import pyperclip
    address = pyperclip.paste().strip()
except Exception:
    address = ""

if not address:
    address = input("Enter address: ")

url = "https://www.openstreetmap.org/search?query=" + quote(address)
print("Opening:", url)
webbrowser.open(url)