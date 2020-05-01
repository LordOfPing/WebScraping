from requests_html import HTMLSession



session = HTMLSession()

r = session.get('http://www.allocine.fr/film/fichefilm_gen_cfilm=9393.html')

html = r.content

fi = open('output.html','w')

fi.write(str(html))


