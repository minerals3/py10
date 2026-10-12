import webbrowser
from urllib.parse import quote

city = input("Enter city: ")
url = "https://www.google.com/search?q=" + quote("weather in " + city)

print("Opening:", url)
webbrowser.open(url)