import webbrowser
from urllib.parse import quote

word = input("Enter a word: ")
url = "https://www.dictionary.com/browse/" + quote(word)

print("Opening:", url)
webbrowser.open(url)