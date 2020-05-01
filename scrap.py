from requests_html import HTMLSession
import re
import json

session = HTMLSession()


r = session.get('http://www.allocine.fr/film/fichefilm_gen_cfilm=9393.html')



scc =r.html.xpath("//script[@type='text/javascript']/text()")
scc = ''.join(scc)

regex = re.findall(r'WbAdsConfig.=.\{.*\}\}',scc)
regex = re.findall(r"\{.*\}",regex[0])

print (regex[0])


fi = open('textjs.html','w')

fi.write(regex[0])
