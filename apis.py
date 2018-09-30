from flask import Flask, render_template
import requests as req

app = Flask(__name__);

@app.route("/")
def index():
    return "hello!"

@app.route("/location")
def location():
    BASE_URL = "https://route.api.here.com/routing/7.2/calculateroute.json"
    app_code = "?app_code=EI0P0IuuqcN1X6TpV_-UvA"
    app_id = "&app_id=BoWarWKWG31XGrhCbuYl"
    waypoint0 = "&waypoint0=51.5141%2C-0.0999"
    waypoint1 = "&waypoint1=51.5081%2C-0.0985"
    mode = "&mode=pedestrian"
    params = {
        'app_code': "EI0P0IuuqcN1X6TpV_-UvA",
        'app_id': 'BoWarWKWG31XGrhCbuYl',
        'waypoint0': '51.5141%2C-0.0999',
        'waypoint1': '51.5081%2C-0.0985',
        'mode': 'fastest;pedestrian'
    }
    #app_code is breaking everything

    res = req.get(BASE_URL, params=params)
    print(res.json())
    return render_template("location.html", obj=res); 

@app.route("/foursquare")
def foursquare():
    BASE_URL = "https://api.foursquare.com/v2/venues/search"

    params = {
        'client_id': 'XUWE2FK1HJSBITL0ATXPUU3SI5XOYTFTWCDYARDR5MO1T5IL',
        'client_secret': '312KG020HXLNLD0Z1RSZ5WFVBYTJU5I5KBZOQFE50ZHWZQWE',
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
    return render_template("location.html", obj=res);

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5002")
