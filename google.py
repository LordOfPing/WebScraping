from requests_html import HTMLSession

session = HTMLSession()

chaine = "la ligne verte"
url = "https://www.google.com/search?q="
chaine = (chaine.strip()).replace(" ","+")
url += chaine +"+allocine"


r = session.get(url)

fiche = r.html.xpath("//div[@class = 'g'][1]//div[@class = 'r'][1]/a/@href")
print(fiche)