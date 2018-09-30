import requests as req
from bs4 import BeautifulSoup
import config

def get_alc_vol(drink):
    #it me
    VOLUME_TABLE = "https://www.moderatedrinking.com/self_monitoring/default_self_monitoring.aspx?p=alcohol_content_of_drinks"
    RECIPE_SITE = "https://www.liquor.com/recipes/{}/"

    receta = req.open(RECIPE_SITE.format(drink))
    pagina = BeautifulSoup(receta.read())
    no_busque = 'This page doesn\'t seem to exist...' in pagina.get_text()
    if no_busque:
        # creamos que es cerveza
        bebidas = [('beer', 12)]
    else:
        bebidas = [(cosa.get_text(), cosa.find_all_previous('div', **{'class': 'oz-value'})) for coas in pagina.find_all('div.x-recipe-ingredient')]

    sitio_tabula = req.open(VOLUME_TABLE)
    tabula = BeautifulSoup(sitio_tabula).find('table', dir="LTR")
    total = 0
    for (bebida, cantidad) in bebidas:
        lo_que_es = tabula.find('div', text=bebida)
        porcentaje = float(tabula.find('div', align='left').get_text())
        total += cantidad * porcentaje
    return total

def foursquare():
    BASE_URL = "https://api.foursquare.com/v2/venues/search"

    params = {
        'v':"20180323",
        'query': "",
        'radius': '500',
        'limit': '10',
        'll': '40.712776,-74.005974',
        'categoryId': "4bf58dd8d48988d116941735",
        'intent': "checkin"
    }

    res = req.get(BASE_URL, params=params);
    print(res.json())

def route():
    BASE_URL = "https://route.api.here.com/routing/7.2/calculateroute.json"
    waypoint0 = "&waypoint0=51.5141%2C-0.0999"
    waypoint1 = "&waypoint1=51.5081%2C-0.0985"
    mode = "&mode=pedestrian"
    params = {
        'waypoint0': '51.5141%2C-0.0999',
        'waypoint1': '51.5081%2C-0.0985',
        'mode': 'fastest;pedestrian'
    }
    #app_code is breaking everything

    res = req.get(BASE_URL, params=params)
    print(res.json())
    return render_template("location.html", obj=res); 

