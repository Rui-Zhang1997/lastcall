import requests as req
from bs4 import BeautifulSoup

def get_directions():
    #ANDREA, plz
    pass

def get_bars():
    #aNDREA, plz
    pass

def get_alc_vol(drink):
    #it me
    VOLUME_TABLE = "https://www.moderatedrinking.com/self_monitoring/default_self_monitoring.aspx?p=alcohol_content_of_drinks"
    RECIPE_SITE = "https://www.liquor.com/recipes/{}/"

    receta = req.open(RECIPE_SITE.format(drink))
    pagina = BeautifulSoup(receta.read())
    no_busque = 'This page doesn\'t seem to exist...' in pagina.text()
    if no_busque:
        # creamos que es cerveza
        bebidas = ['beer']
    else:
        pass
