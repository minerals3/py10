import webbrowser

sites = [
    "https://www.bbc.com/news",
    "https://www.reuters.com",
    "https://www.thehindu.com"
]

for site in sites:
    print("Opening:", site)
    webbrowser.open(site)