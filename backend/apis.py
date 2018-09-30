import requests as req
from bs4 import BeautifulSoup
import config
import populartimes as pop
import re
from math import atan, pi, sqrt

ALC_CONTENT_TABLE = {
        "Abita Amber": 0.44,
        "Absolut 100": 0.50,
        "Absolut Vodka": 0.40,
        "After Shock": 0.40,
        "Alize": 0.16,
        "Amaretto": 0.22,
        "Amaretto Sour": 0.22,
        "Amstel": 0.05,
        "Amstel Light": 0.03,
        "Anchor Steam ": 0.04,
        "Ancient Age Bourbon": 0.40,
        "Anisette": 0.30,
        "Apple Pucker": 0.30,
        "Armagnac": 0.40,
        "Arrow Creme de Cocoa": 0.20,
        "Arrow Creme de Menthe": 0.21,
        "Arrow Curacao": 0.27,
        "Avalanche": 0.40,
        "B52 Kahlua Drink": 0.05,
        "Bacardi 121": 0.60,
        "Bacardi 151": 0.75,
        "Bacardi Limon": 0.35,
        "Bacardi Solero Dark Rum": 0.38,
        "Bacardi White Rum": 0.37,
        "Bad Frog": 0.06,
        "Bahama Mama": 0.15,
        "Bailey's Irish Cream": 0.17,
        "Banana Liqueur": 0.24,
        "Bartles &amp; Jaymes": 0.05,
        "Bartles &amp; Jaymes Light": 0.02,
        "Bass ": 0.05,
        "Becks ": 0.04,
        "Becks Dark": 0.04,
        "Becks Light": 0.03,
        "Becks Octoberfest": 0.05,
        "Beefeater": 0.47,
        "Beer (Domestic)": 0.04,
        "Beer": 0.04,
        "Beer (Imported Ales)": 0.06,
        "Beer (Imported Porters)": 0.06,
        "Beer (Imported Stouts)": 0.06,
        "Beer (Imported)": 0.06,
        "Beer (Lights)": 0.04,
        "Beer (Malt Liquor)": 0.06,
        "Beer (non-alcoholic)": 0.005,
        "Benedictine": 0.43,
        "Berghoff Original ": 0.05,
        "Big Bear": 0.07,
        "Black and White": 0.40,
        "Black Hawk": 0.45,
        "Black Label LA": 0.02,
        "Black Velvet": 0.40,
        "Bloody Mary": 0.40,
        "Blue Carousel": 0.27,
        "Bols Anisette": 0.25,
        "Bols Triple Sec": 0.21,
        "Bombay Gin": 0.43,
        "Boston Anisette": 0.21,
        "Boston Creme de Menthe": 0.17,
        "Boston Triple Sec": 0.17,
        "Bourbon": 0.40,
        "Brandy": 0.42,
        "Brandy (Fruit)": 0.43,
        "Bridgeport Blue Heron Pale ": 0.05,
        "Brinkhoff's #1": 0.07,
        "Brooklyn Brand ": 0.05,
        "Bud Ice ": 0.05,
        "Bud Ice Light": 0.04,
        "Bud Light": 0.04,
        "Budweiser": 0.04,
        "Bull Ice": 0.08,
        "Busch ": 0.04,
        "Busch (in Utah)": 0.03,
        "Busch Ice": 0.05,
        "Busch Light": 0.04,
        "Bushmill's": 0.40,
        "Butterscotch Schnapps": 0.15,
        "Buttershots": 0.15,
        "Camo": 0.08,
        "Canadian Club": 0.40,
        "Canadian Mist": 0.40,
        "Canadian Whiskey": 0.40,
        "Cape Codder": 0.40,
        "Capt.Morgan Original Spiced Rum": 0.35,
        "Carlsburg Light": 0.04,
        "Carlton Gold": 0.04,
        "Castillo Rum": 0.40,
        "Catamount Amber ": 0.04,
        "Chamborg": 0.16,
        "Chivas Regal": 0.43,
        "Christian Bros": 0.40,
        "Club Manhattan": 0.17,
        "Club Pina Colada": 0.12,
        "Coffee Liqueur": 0.22,
        "Cognac": 0.40,
        "Cointreau": 0.40,
        "Colorado Bull Dog": 0.33,
        "Colt 45": 0.05,
        "Coors": 0.04,
        "Coors Extra Gold": 0.05,
        "Coors Light": 0.04,
        "Corona ": 0.04,
        "Cosmopolitan": 0.33,
        "Crazy Horse": 0.06,
        "Creme de Cocoa": 0.24,
        "Creme de Menthe": 0.24,
        "Crown Lager": 0.04,
        "Crown Royal": 0.40,
        "Crown Sterling": 0.43,
        "Crown Sterling Gin": 0.40,
        "Cuervo 1800": 0.40,
        "Cuervo Almndrado Tequila- CuervoAlmndrado": 0.27,
        "Cuervo Anejo Tequila ": 0.40,
        "Cuervo Gold Tequila ": 0.40,
        "Curacao": 0.23,
        "Cutty Sark": 0.40,
        "Dewars": 0.43,
        "Dock Street Amber ": 0.05,
        "Dominion ": 0.05,
        "Don Carlos Tequila": 0.40,
        "Dos Equis ": 0.04,
        "Drambuie": 0.40,
        "Dubouchette Amaretto": 0.28,
        "Dubouchette Triple Sec ": 0.30,
        "Early Times Bourbon ": 0.40,
        "EKU 28 Malt Liquor": 0.10,
        "Elephant Malt Liquor": 0.07,
        "Eliot Ness": 0.06,
        "Elk Mountain Amber ": 0.05,
        "Everclear": 0.95,
        "Fat Tire": 0.05,
        "Fleischmann's": 0.45,
        "Fosters ": 0.05,
        "Franzia in a Box": 0.09,
        "Franzia Wine Cooler": 0.05,
        "Fu-Ki Sake": 0.16,
        "Full Sail Amber ": 0.05,
        "Fuzzy Navel": 0.20,
        "Geary's Pale ": 0.04,
        "Genesee Cream Ale ": 0.04,
        "Genj Sake": 0.17,
        "Gilbey's Gin": 0.40,
        "Gilbey's Vodka": 0.40,
        "Gin (Bar Stock)": 0.40,
        "Gin (Diluted)": 0.21,
        "Gin (Flavored)": 0.35,
        "Glenfiddich": 0.43,
        "Goldschlager": 0.53,
        "Gordon's Gin": 0.40,
        "Grande Marnier": 0.40,
        "Grape Pucker (DeKuyper)": 0.15,
        "Graves": 0.95,
        "Grolsch Lager Beer": 0.05,
        "Guinness": 0.04,
        "H. Walker Creme de Cocoa": 0.27,
        "H. Walker Creme de Menthe": 0.30,
        "Haake Beck Non-Alcoholic": .003,
        "Hard Core Cider": 0.06,
        "Heaven Hill Bourbon": 0.40,
        "Heaven Hill Ol Style": 0.50,
        "Heineken": 0.05,
        "Hennessy Cognac": 0.40,
        "Henry Weinhard's Private Reserve ": 0.04,
        "Herradura Tequila": 0.40,
        "Heublein Marguerita": 0.12,
        "Heublein Pina Colada": 0.13,
        "Heublein Whiskey Sour": 0.15,
        "Hiram Walker Triple Sec": 0.30,
        "Honey Brown - JW Dundee": 0.03,
        "Honey Brown Lager": 0.05,
        "Hoster 90 Shilling Ale": 0.06,
        "Hot Damn": 0.50,
        "Hurricane": 0.05,
        "Ice House": 0.05,
        "Irish Whiskey": 0.40,
        "Jack Daniel Black": 0.45,
        "Jack Daniel Green Bourbon ": 0.40,
        "Jagermeister": 0.35,
        "Jamaica Club (White)": 0.65,
        "Jamaican Club (Gold)": 0.40,
        "Jameson Irish Whiskey": 0.40,
        "Jeremiah Weed": 0.50,
        "Jim Beam": 0.40,
        "Jim Beam 8 year": 0.50,
        "Jim Beam Black": 0.45,
        "Johnny Walker ": 0.40,
        "Johnny Walker Black": 0.43,
        "Johnny Walker Red": 0.43,
        "Juarez Triple Sec": 0.15,
        "Jungle Juice": 0.95,
        "Kahlua": 0.27,
        "Kamakazi": 0.38,
        "Kapala": 0.27,
        "Keystone": 0.04,
        "Keystone Ice": 0.05,
        "Keystone Light": 0.04,
        "Kiki Beach Key Lime Liquor": 0.15,
        "Kiku Masamune Sake": 0.16,
        "Killians Red ": 0.04,
        "King Cobra": 0.06,
        "Kirin ": 0.05,
        "Kiss of Death": 0.07,
        "LA Anheuser Busch": 0.02,
        "Labatt Blue ": 0.05,
        "Legacy Lager ": 0.05,
        "Leinenkugel's Red ": 0.05,
        "Leroux Anisette": 0.30,
        "Leroux Creme de Cocoa": 0.27,
        "Lewiston": 0.95,
        "Liberty ": 0.06,
        "Licor de Cafe": 0.27,
        "Listerine": 0.27,
        "Lite Ultra": 0.04,
        "Lone Star ": 0.04,
        "Long Island Ice Tea": 0.36,
        "Lord Calvert Canadian Whiskey": 0.40,
        "Lowenbrau": 0.04,
        "Lowenbrau Dark": 0.04,
        "Lowenbrau Light": 0.04,
        "Lucky Lager": 0.05,
        "Mad Dog 20/20": 0.19,
        "Magnum 40": 0.05,
        "Magnum Malt": 0.05,
        "Mai Tai": 0.32,
        "Makers Mark": 0.45,
        "Malibu Rum": 0.24,
        "Margarita": 0.34,
        "Martini &amp; Rossi": 0.16,
        "McEwan's Scottish Ale": 0.08,
        "Meisterbrau": 0.04,
        "Melon Liqueur": 0.21,
        "Michelob": 0.04,
        "Michelob Dark": 0.04,
        "Michelob Dry": 0.05,
        "michelob light": 0.04,
        "Mickey's": 0.05,
        "Mickeys Ice": 0.05,
        "Midori": 0.21,
        "Mikes Lemonade": 0.05,
        "Miller": 0.04,
        "Miller Genuine Draft": 0.04,
        "Miller Lite": 0.04,
        "Miller Reserve": 0.04,
        "Milwaukee's Best ": 0.04,
        "Molinari Sambuca": 0.42,
        "Molson Diamond": 0.02,
        "Molson Golden ": 0.05,
        "Molson Ice ": 0.05,
        "Molson Signature Cream Ale": 0.05,
        "Murphy's Irish Stout": 0.04,
        "Muscatel": 0.20,
        "Myers Rum": 0.40,
        "Natural Ice": 0.05,
        "Natural Light ": 0.04,
        "Natural Light Ice": 0.05,
        "Negro Modelo": 0.06,
        "New Amsterdam New York ": 0.03,
        "NewCastle": 0.04,
        "Newport": 0.15,
        "Night Train": 0.18,
        "No Face Label Creme de Cocoa": 0.30,
        "No Face Label Creme de Menthe": 0.30,
        "Norwester HefeWeizen": 0.05,
        "NyQuil": 0.25,
        "Oban Single Malt Scotch": 0.43,
        "Old Bushmills": 0.40,
        "Old Commonwealth St.Patrick": 0.40,
        "Old Crow": 0.40,
        "Old Detroit Amber ": 0.05,
        "Old English 800 Malt Liquor": 0.06,
        "Old English Ice": 0.08,
        "Old Grand Dad": 0.43,
        "Old Milwaukee ": 0.04,
        "Old Speckled Hen": 0.05,
        "Olde English Malt Liqor": 0.06,
        "Oregon Pale Ale": 0.05,
        "Outrigger Rum": 0.40,
        "Ouzo": 0.46,
        "Pabst Blue Ribbon ": 0.04,
        "Parrot Bay Coconut Rum": 0.24,
        "Peach Schnapps": 0.20,
        "Peppermint Schnapps": 0.30,
        "Permafrost": 0.40,
        "Petes Honey Wheat": 0.04,
        "Petes Octoberfest": 0.05,
        "Petes Signature Pilsner": 0.04,
        "Petes Strawberry Blonde": 0.05,
        "Pete's Wicked Ale ": 0.05,
        "Pete's Wicked Ale Pub Lager": 0.05,
        "Petes Wicked Ale Summer Brew": 0.04,
        "Petes Winter Brew": 0.05,
        "Pilsner Urquell ": 0.04,
        "Popov": 0.40,
        "Port": 0.20,
        "Raspberry Weizen": 0.05,
        "Rebel Yell": 0.43,
        "Red Dog": 0.05,
        "Red Hook ESB ": 0.05,
        "Red Hook IPA": 0.06,
        "Red Nectar ": 0.05,
        "Red Wolf ": 0.05,
        "Riunite": 0.08,
        "Rolling Rock": 0.04,
        "Ronrico (Gold)": 0.40,
        "Ronrico (Purple)": 0.75,
        "Rum": 0.40,
        "Rum (Bar Stock)": 0.40,
        "Rum (Cuban)": 0.40,
        "Rum (Jamaican)": 0.40,
        "RumpleMinze": 0.50,
        "Sake": 0.18,
        "Sam Adams": 0.04,
        "Sam Adams Boston Ale": 0.04,
        "Sam Adams Cherry Wheat": 0.05,
        "Sam Adams Cream Stout": 0.04,
        "Sam Adams Double Bock": 0.08,
        "Sam Adams Golder Pilsner": 0.04,
        "Sam Adams Honey Porter": 0.05,
        "Sam Adams IPA": 0.05,
        "Sam Adams Millennium": 0.19,
        "Sam Adams Oktoberfest": 0.05,
        "Sam Adams Pale Ale": 0.05,
        "Sam Adams Spring Ale": 0.05,
        "Sam Adams Summer Ale": 0.05,
        "Sam Adams Triple Bock": 0.17,
        "Sam Adams Winter Lager": 0.06,
        "Sambuca": 0.40,
        "Samichlaus Bier": 0.11,
        "Sauza Tequila Extra": 0.40,
        "Schlitz Bull Ice": 0.08,
        "Schlitz Ice": 0.06,
        "Schlitz Malt Liquor": 0.05,
        "Schnapps": 0.20,
        "Schnapps - Fruit": 0.15,
        "Scotch": 0.40,
        "Screwdriver": 0.40,
        "Seagrams Seven": 0.40,
        "Seagrams Seven Fuzzy Navel": 0.06,
        "Sex on the Beach": 0.30,
        "Sharps": .005,
        "Sherry": 0.20,
        "Shiner Blonde": 0.04,
        "Shiner Bock": 0.04,
        "Shiner Honey Wheat": 0.05,
        "Shiraz": 0.13,
        "Shiraza": 0.14,
        "Sierra Nevada": 0.05,
        "Sierra Nevada Pale Ale ": 0.05,
        "Sierra Nevada Porter": 0.05,
        "Sierra Nevada Stout": 0.05,
        "Sloe Gin": 0.30,
        "Smirnoff": 0.40,
        "Smirnoff Ice": 0.05,
        "Southern Comfort": 0.40,
        "Southpaw Light": 0.05,
        "St Ides": 0.07,
        "St Pauli Girl ": 0.04,
        "Steele Reseve": 0.08,
        "Sterling ": 0.04,
        "Stolichnaya 100": 0.50,
        "Stolichnaya Vodka": 0.40,
        "Stroh's": 0.04,
        "Stroh's Light": 0.04,
        "Sun Country": 0.04,
        "Sun Country Light": 0.02,
        "Sutter Home Merlot": 0.13,
        "Tanqueray Sterling": 0.40,
        "Tanquery": 0.47,
        "Tecate": 0.06,
        "Tequila (Bar Stock)": 0.40,
        "Tequila Rose": 0.17,
        "Tequiza": 0.04,
        "Tequiza Extra": 0.05,
        "Texas Tea": 0.40,
        "Triple Sec": 0.21,
        "Tullamore Dew": 0.40,
        "Ushers": 0.41,
        "V O Canadian Whiskey": 0.40,
        "Vera Cruz Triple Sec": 0.15,
        "Vermouth": 0.18,
        "Victoria Bitter": 0.04,
        "Virgin Bourbon": 0.53,
        "Vodka (Bar Stock)": 0.40,
        "Vodka (Diluted)": 0.21,
        "Vodka (Flavored)": 0.35,
        "Watermelon Pucker": 0.15,
        "Whiskey Bar Stock": 0.40,
        "Wild Irish Rose": 0.18,
        "Wild Turkey": 0.40,
        "Wine": 0.12,
        "Wine (Champagne)": 0.12,
        "Wine (Fortified)": 0.20,
        "Wine (Plum)": 0.14,
        "Wine (Table) Red, White or Rose": 0.12,
        "Wine Cooler": 0.04,
        "Yuengling Premium ": 0.04,
        "Yukon Jack": 0.50,
        "Zima": 0.03
}

def substrings(st):
    for i in range(len(st)):
        for j in range(i + 1, len(st) + 1):
            yield st[i:j]

ALC_CONTENT_TABLE = [(set(substrings(i.lower())), ALC_CONTENT_TABLE[i]) for i in ALC_CONTENT_TABLE]


def angle_from(point, to):
    angle = atan((point[1] - to[1])/(point[0] - to[0]))
    if point[0] > to[0]:
        return pi + angle
    return angle


def get_alc_vol(drink):
    #it me
    VOLUME_TABLE = "https://www.moderatedrinking.com/self_monitoring/default_self_monitoring.aspx?p=alcohol_content_of_drinks"
    RECIPE_SITE = "https://www.liquor.com/recipes/{}/"

    def limpia(cantidad):
        ubi_slash = cantidad.find('/')
        if ubi_slash < 0:
            return float(cantidad.replace('oz', ''))
        else:
            return float(cantidad[:ubi_slash - 2]) + (cantidad[ubi_slash - 1] / cantidad[ubi_slash + 1])

    receta = req.open(RECIPE_SITE.format(drink.replace(' ', '-')))
    pagina = BeautifulSoup(receta.read())
    no_busque = 'This page doesn\'t seem to exist...' in pagina.get_text()
    if no_busque:
        # creamos que es cerveza
        bebidas = [('beer', 12)]
    else:
        bebidas = [(cosa.get_text(), limpia(cosa.find_all_previous('div', **{'class': 'oz-value'}))) for coas in pagina.find_all('div.x-recipe-ingredient')]

    return sum(i[0] * i[1] for i in bebidas)


def foursquare(place, num_bars):
    BASE_URL = "https://api.foursquare.com/v2/venues/search"
    BAR_URL = "https://api.foursquare.com/v2/venues/{}/menu"

    params = {
        'query': "",
        'radius': '500',
        'limit': '10',
        'll': '{},{}'.format(*place),
        'categoryId': "4bf58dd8d48988d116941735",
        'query': "bar"
    }
    params.update(config.FOURSQUARE_PARAMS)

    bar_params = {
    }
    bar_params.update(config.FOURSQUARE_PARAMS)

    res = req.get(BASE_URL, params=params)
    yield from res.json()['response']['venues']

def route(*waypts):
    BASE_URL = "https://route.api.here.com/routing/7.2/calculateroute.json"

    params = {
        'mode': 'fastest;pedestrian'
    }
    params.update(config.HERE_API_PARAMS)

    for idx, waypt in enumerate(waypts):
        params['waypoint' + str(idx)] = "{},{}".format(*waypt)

    res = req.get(BASE_URL, params=params)
    print(res.url)
    return res.json()

def addy_to_geo(addy):
    HERE_BASE_URL = "https://geocoder.api.here.com/6.2/geocode.json"
    params = {'searchtext': addy}
    params.update(config.HERE_API_PARAMS)
    here = req.get(HERE_BASE_URL, params=params)
    there = here.json()
    print(there)
    coords = there['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']
    return coords['Latitude'], coords['Longitude']

def bars(src, dest, params):
    origin = (src)
    end = (dest)
    direction = angle_from(origin, end)
    for bar in sorted(foursquare(origin, params['barCount']),
            key = lambda b: abs(direction - angle_from(origin, (b['location']['lat'], b['location']['lng'])))):
        yield {
            'barName': bar['name'],
            'barId': bar['id'],
            'barRating': 'LOL',
            'barCost': 0,
            'll': '{},{}'.format(bar['location']['lat'], bar['location']['lng']),
            'menu': []
        }

print(list(foursquare(addy_to_geo('60606'), 5)))
