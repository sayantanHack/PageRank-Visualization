import requests, sys, webbrowser, bs4
n= int(input('Enter the numbers of tabs you want to opn in Browser: '))

res = requests.get("https://google.com/search?q="+"".join(sys.argv[1:]))

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

linkElem = soup.select('.r a')

linkOpen = min(n, len(linkElem))

for i in range(linkOpen):
    webbrowser.open('https://facebook.com'+linkElem[i].get('href'))
