from flask import Flask, render_template, request, redirect
import pymongo as m

app = Flask(__name__)

chars = [str(i) for i in range(10)] + [chr(ord('A')) + i for i in range(26)]
hop_ids = (''.join(chars[i//(36 ** j) % 36] for j in range(4)) for i in range(0, 36**4))

@app.route('/hop/make', methods=["POST"])
def start_hop():
    hop = request.json
    start_addy = hop['start']
    end_addy = hop['end']
    

@app.route('/hop/join/{hopcode}', methods=["POST"])
def add_to_hop():
    return 'another!'

@app.route('/hop/exists/{hopcode}')
def is_hop():
    return "adjust"

@app.route('/hop/member/{id}')
def get_hop_member():
    return "hop"

@app.route('/hop/{id}')
def get_hop():
    return "hop"

@app.route('/hop/update/{member_id}', methods=["POST"])
def update_hop():
    return "hop"

if __name__ == '__main__':
    app.run(port=5000)

