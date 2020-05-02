from requests_html import HTMLSession
import re
import json

session = HTMLSession()


r = session.get('http://www.allocine.fr/film/fichefilm_gen_cfilm=39187.html')



def image_descript(sessionget):

    scc =r.html.xpath("//script[@type='application/ld+json']/text()")
    scc = ''.join(scc)
    data = json.loads(scc,strict=False)
    dico = {"name": data.get("name"),"image_url": data.get('image').get('url'), "description" : data.get("description")}

    return(dico)


def test(sessionget):
    scc =r.html.xpath("//script[@type='application/ld+json']/text()")
    scc = ''.join(scc)

    t= open("test.json", "w")
    t.write(scc)

dic = str(image_descript(r))
print(dic)
