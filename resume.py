from requests_html import HTMLSession
import re
import json

# Ouverture d'une session 
session = HTMLSession()

# Url à Scraper
r = session.get('http://www.allocine.fr/film/fichefilm_gen_cfilm=39187.html')


def image_descript(sessionget):
    '''
    # Récupère le nom l'image et le résumé d'un film \n
    ## Input : session.get(url) \n
    ### Output : dict
    '''

    # Création d'un tableau contenant toutes les balises de type text/javascript
    scc =r.html.xpath("//script[@type='application/ld+json']/text()")

    # Conversion en Str
    scc = ''.join(scc)

    # Conversion en Json
    data = json.loads(scc,strict=False)

    # Création d'un dictionnaire avec les information voulu contenu dans data
    dico = {"name": data.get("name"),"image_url": data.get('image').get('url'), "description" : data.get("description")}

    return(dico)


if __name__ == "__main__":
    
    dic = str(image_descript(r))
    print(dic)
