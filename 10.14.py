import webbrowser
from urllib.parse import quote

product = input("Enter product name: ")
url = "https://www.amazon.in/s?k=" + quote(product)

print("Opening:", url)
webbrowser.open(url)