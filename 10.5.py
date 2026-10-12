import webbrowser

sites = [
    "https://www.instagram.com",
    "https://www.facebook.com",
    "https://www.linkedin.com"
]

for site in sites:
    print("Opening:", site)
    webbrowser.open(site)