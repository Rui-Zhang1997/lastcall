from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return "hello :)"

@app.route('/start-hop', methods=["POST"])
def start_hop():
    return 'alcoholic'

@app.route('/add-hop', methods=["POST"])
def add_hop():
    return 'another!'

@app.route('/adjust-hop', methods=["POST"])
def adjust_hop():
    return "adjust"

@app.route('/get-hop')
def get_hop():
    return "hop"

if __name__ == '__main__':
    app.run(port=5000)

