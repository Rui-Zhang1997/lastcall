from flask import Flask, render_template, request, redirect, jsonify
import pymongo as m
import config
import apis
import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

app = Flask(__name__)

chars = [str(i) for i in range(10)] + [chr(ord('A') + i) for i in range(26)]
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

    return db

@app.route('/hop/make', methods=["POST"])
def start_hop():
    hop = request.json
    hop['hopId'] = next(hop_ids)
    hop['finalized'] = True
    hop['members'] = [
        {
            "memberName": hop['creatorName'],
            "memberId": next(memb_id),
            "drunkLevel": hop['drunkLevel'],
            "maxCost": hop['maxBarCost'],
            "currentHop": hop['hopId']
        }
    ]

    db = connect_to_db()
    db[config.COLLECTIONS['hop']].insert(hop)
    return JSONEncoder().encode(hop)


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
        bars = list(apis.bars(apis.addy_to_geo(hop['sll']), apis.addy_to_geo(hop['sll']), hop))

        hops.update({'hopId':  hopcode}, {'$set': {'finalized': True}})
        hops.update({'hopId':  hopcode}, {'$set': {'bars': bars}})
        return {
            'hopId': hopcode,
            'bars': bars
        }

    hops.update({'hopId':  hopcode}, {'$push': {'members': member}})


@app.route('/hop/exists/{hopcode}')
def is_hop(hopcode):
    db = connect_to_db()
    hops = db[config.COLLECTIONS['hop']]
    hop = hops.find_one({'hopId': hopcode})
    return not ( hop is None or hope == {} or hop == [])

@app.route('/hop/member/{id}')
def get_hop_member(id):
    #if the member is in the hop, they have the same stats as the hop creator
    db = connect_to_db()
    hops = db[config.COLLECTIONS['hop']]
    hop = hops.find_one({'members': {'$elemMatch': {'memberId': id}}})
    if hop is None or hope == {} or hop == []:
        return 404, 'Member not found!'
    return {
        "memberName": hop['creatorName'],
        "memberId": id,
        "drunkLevel": hop['drunkLevel'],
        "maxCost": hop['maxBarCost'],
        "currentHop": hop['hopId']
    }


@app.route('/hop/{id}')
def get_hop():
    db = connect_to_db()
    hops = db[config.COLLECTIONS['hop']]

    hop = hops.find_one({'hopId': hopcode})
    if hop is None or hope == {} or hop == []:
        return 404, 'Hop not found'
    if not hop['finalized']:
        return 400, 'Hop not finalized!'

    return {
        'hopId': hop['id'],
        'bars': hop['bars']
    }

@app.route('/hop/update/{member_id}', methods=["POST"])
def update_hop(mem_id):
    hop = request.json
    db = connect_to_db()
    hops = db[config.COLLECTIONS['hop']]

    hop = hops.find_one({'hopId': hop['hopId']})
    if hop is None or hope == {} or hop == []:
        return 404, 'Hop not found'

    hops.update({'hopId': hop['hopId'], '$pull': {'members': {'memberId': mem_id}}})

    new_hop['hopId'] = next(hop_ids)
    new_hop['finalized'] = True
    new_hop['members'] = [
        {
            "memberName": hop['creatorName'],
            "memberId": next(memb_id),
            "drunkLevel": hop['drunkLevel'],
            "maxCost": hop['maxBarCost'],
            "currentHop": hop['hopId']
        }
    ]

    hops.insert(new_hop)
    return new_hop

if __name__ == '__main__':
    app.run(port=5000)

