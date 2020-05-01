from requests_html import HTMLSession
import re
import json

session = HTMLSession()


r = session.get('http://www.allocine.fr/film/fichefilm_gen_cfilm=9393.html')

def distrib_and_date(sessionget):

    scc =sessionget.html.xpath("//script[@type='text/javascript']/text()")
    scc = ''.join(scc)

    regex = re.findall(r'WbAdsConfig.=.\{.*\}\}',scc)
    regex = re.findall(r"\{.*\}",regex[0])

    data = json.loads(regex[0])


    dico = {"movie_distributors": data.get("targeting").get("movie_distributors"),"production_year":(data.get("targeting")).get("production_year")}

    return(dico)

dic = distrib_and_date(r)
print(dic)