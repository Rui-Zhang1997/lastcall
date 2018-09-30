from flask import Flask, render_template, request, redirect
import pymongo as m

import apis

app = Flask(__name__)

chars = [str(i) for i in range(10)] + [chr(ord('A')) + i for i in range(26)]
hop_ids = (''.join(chars[i//(36 ** j) % 36] for j in range(4)) for i in range(0, 36**4))

def counter():
    i = 0
    while True:
        yield i
        i += 1

memb_id = counter()

def connect_to_db():
    client = m.MongoClient(config.DB_URI)
    db = client[config.DB_NAME]
    db.authenticate(config.DB_USER,config.DB_PASS)

    return db

@app.route('/hop/make', methods=["POST"])
def start_hop():
    hop = request.json
    start_addy = hop['start']
    end_addy = hop['end']
    hop['hopId'] = next(hop_ids)
    hop['hopName'] = hop['name']
    hop['barCount'] = hop['duration']
    hop['sll'] = start_addy
    hop['ell'] = end_addy
    hop['finalized'] = False
    hop['members'] = []

    db = connect_to_db()
    db[config.COLLECTIONS['hop']].insert(hop)
    return hop


@app.route('/hop/join/<hopcode>', methods=["POST"])
def add_to_hop(hopcode):
    db = connect_to_db()
    hops = db[config.COLLECTIONS['hop']]

    hop = hops.find_one({'hopId': hopcode})
    if hop is None or hope == {} or hop == []:
        return 404, 'Hop not found'

    member = request.json
    member['id'] = next(memb_id)

    if not hop['finalized']:
        #make the route
        bars = apis.bars(apis.addy_to_geo(hop['sll']), apis.addy_to_geo(hop['sll']), hop)

        hops.update({'hopId':  hopcode}, {'$set': {'finalized': True}})

    hops.update({'hopId':  hopcode}, {'$push': {'members': member}})


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

