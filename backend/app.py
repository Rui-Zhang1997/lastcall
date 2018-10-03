from flask import Flask

app = Flask(__name__)

class Member:
    def __init__(self, member_id, member_name, drunk_level, max_cost, current_hop):
        self.member_id = member_id
        self.member_name = member_name
        self.drunk_level = drunk_level
        self.max_cost = max_cost
        self.current_hop = current_hop

def Hop:
    def __init__(self, hop_id, hop_name, creator_name, saddr, eaddr, stime, drunk_level, bar_count, max_bar_cost):
        self.hop_id = hop_id
        self.hop_name = hop_name
        self.creator_name = creator_name
        self.saddr = saddr
        self.eaddr = eaddr
        self.stime = stime
        self.drunk_level = drunk_level
        self.bar_count = bar_count
        self.max_bar_cost = max_bar_cost

@app.route('/hop/make')
def make_hop():
    pass

@app.route('hop/join/<hopcode>')
def join_hop():
    pass

@app.route('/hop/exists/<hopcode>')
def check_hop():
    pass

@app.route('/hop/member/<id>')
def get_member():
    pass

@app.route('/hop/<hopid>')
def get_hop():
    pass

@app.route('/hop/update/<memberid>')
def update_member():
    pass
