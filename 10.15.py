import webbrowser
from urllib.parse import quote

text = input("Enter text to translate: ")
url = (
    "https://translate.google.com/"
    "?sl=auto&tl=hi&text=" + quote(text) + "&op=translate"
)

print("Opening:", url)
webbrowser.open(url)