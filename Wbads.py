from requests_html import HTMLSession
import re
import json

# Ouverture d'une session 
session = HTMLSession()

# Url à Scraper
r = session.get('http://www.allocine.fr/film/fichefilm_gen_cfilm=39187.html')


def distrib_and_date(sessionget):
    '''
    # Récupère le distributeur et la date de production d'un film \n
    ## Input : session.get(url) \n
    ### Output : dict
    '''
    # Création d'un tableau contenant toutes les balises de type text/javascript
    scc =sessionget.html.xpath("//script[@type='text/javascript']/text()")
    # Conversion en Str pour les Regex
    scc = ''.join(scc)
    # Utilisation des Regex pour selectionner la balise voulue
    regex = re.findall(r'WbAdsConfig.=.\{.*\}\}',scc)
    # Sélection du Json uniquement
    regex = re.findall(r"\{.*\}",regex[0])
    # Conversion en Json
    data = json.loads(regex[0],strict=False)

    # Création d'un dictionnaire avec les information voulu contenu dans data
    dico = {"movie_distributors": data.get("targeting").get("movie_distributors"),"production_year":(data.get("targeting")).get("production_year")}

    return(dico)

if __name__ == "__main__":
    
    dic = distrib_and_date(r)
    print(dic)