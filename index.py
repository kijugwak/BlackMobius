from os import sendfile
from flask import Flask, render_template, send_file


app = Flask(__name__)
app.debug = True

@app.route('/')
def blackmobius():
    return render_template('index.html')

@app.route('/shop')
def test():
    return render_template('shop.html')

@app.route('/hood')
def pants():
    return render_template('hood.html')

@app.route('/grayhood')
def hood_1():
    return render_template('hood_1.html')

@app.route('/현상')
def girl():
    return send_file('./static/girl.png')

@app.route('/shop_rev')
def shop_rev():
    return render_template('shop_rev.html')

@app.route('/case')
def case():
    return render_template('case.html')

@app.route('/login')
def login():
    return render_template('black_mobius_login.html')

@app.route('/membership')
def login_error():
    return render_template('join_membership.html')

@app.route('/black_sky_hood')
def black_sky_hood():
    return render_template('hood_2.html')

@app.route('/black_sky_hood_nolabel')
def black_sky_hood_nolabel():
    return render_template('hood_3.html')

@app.route('/goblin')
def goblin():
    return render_template('hood_4.html')

@app.route('/white_sky_nolabel')
def whitesky_nolabel():
    return render_template('hood_5.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9900)