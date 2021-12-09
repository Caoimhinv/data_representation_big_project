from flask import Flask, session, url_for, request, redirect, abort, jsonify
from WineDao import wineDao

app = Flask(__name__, static_url_path='', static_folder='static_pages')

app.secret_key = 'WINEesjrhcb755bdhb13463'

@app.route('/')
def home():
    if not 'username' in session:
        return redirect(url_for('login'))
    
    return 'Welcome ' + session['username'] +\
        '<br><br><a href="'+url_for('getData')+'">Continue to app</a>' +\
        '<br><a href="'+url_for('logout')+'">Logout</a>'
 
@app.route('/login')
def login():
    return '<h1> login</h1> '+\
        '<button>'+\
            '<a href="'+url_for('proccess_login')+'">' +\
                'login' +\
            '</a>' +\
        '</button>'

@app.route('/processlogin')
def proccess_login():
    #check credentials
    #if bad redirect to login page again

    #else
    session['username']="Wine fan!"
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/daddyswine.html')
def getData():
    if not 'username' in session:
        abort(401)
    return '{"data":"all here"}'

@app.route('/')
def index():
    return "hello"

#get all
@app.route('/wines')
def getAll():
    return jsonify(wineDao.getAll())

# find By id
@app.route('/wines/<int:ID>')
def findById(ID):
    return jsonify(wineDao.findById(ID))

# create
@app.route('/wines', methods=['POST'])
def create():
    if not request.json:
        abort(400)

    wine = {
        "nameProducer": request.json["nameProducer"],
        "vintage": request.json["vintage"],
        "regionCountry": request.json["regionCountry"],
    }
    return jsonify(wineDao.create(wine))
    return "served by Create "

# update
@app.route('/wines/<int:ID>', methods=['PUT'])
def update(ID):
    foundWine = wineDao.findById(ID)
    print (foundWine)
    if foundWine == {}:
        return jsonify({}), 404
    currentWine = foundWine
    if 'nameProducer' in request.json:
        currentWine['nameProducer'] = request.json['nameProducer']
    if 'vintage' in request.json:
        currentWine['vintage'] = request.json['vintage']
    if 'regionCountry' in request.json:
        currentWine['regionCountry'] = request.json['regionCountry']
    wineDao.update(currentWine)
    return jsonify(currentWine)

#delete
@app.route('/wines/<int:ID>', methods=['DELETE'])
def delete(ID):
    wineDao.delete(ID)
    return jsonify({"done": True})

if __name__ == "__main__":
    app.run(debug=True)