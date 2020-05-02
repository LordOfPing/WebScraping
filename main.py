from requests_html import HTMLSession
import re
import json
import Wbads
import google
import resume
session = HTMLSession()


film = google.google("la ligne verte", session)

r = session.get(film[0])



dic1 = Wbads.distrib_and_date(r)

dic2 = resume.image_descript(r)

fiche = {**dic2,**dic1}

print(fiche)
