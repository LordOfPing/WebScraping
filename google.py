from requests_html import HTMLSession


# Ouverture d'une session 
session = HTMLSession()

# Le film à rechercher
chaine = "la ligne verte"

# Remplacement des espace par des +
chaine = (chaine.strip()).replace(" ","+")

# Url de base pour une recherche Google
url = "https://www.google.com/search?q="

# Création de la requette
url += chaine +"+allocine"

# Génération de la page
r = session.get(url)

# Création d'un tableau contenant l'url du film sur allociné
fiche = r.html.xpath("//div[@class = 'g'][1]//div[@class = 'r'][1]/a/@href")
print(fiche)