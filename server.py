# importing necessary libraries
from flask import Flask, url_for, request, redirect, abort, jsonify, render_template, session, make_response

# importing DAO file to interact with database
from WineDao import wineDao

app = Flask(__name__, static_url_path='', static_folder='static_pages')

# checking if the user exsits in the database
@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != '' or request.form['password'] != '':
            email = request.form['email']
            password = request.form['password']
            foundUser = wineDao.checkUser(email, password)
            if not foundUser:
                error = 'Invalid Credentials. Please try again.'
            else:
                return redirect(url_for('welcome'))
        else:
            return error
    return render_template('login.html', error=error)

# home
@app.route('/')
def home():
    return 'Hello you!' +\
        '<br>' +\
        '<button>' +\
            '<a href="'+url_for('login')+'">' +\
                'Continue' +\
            '</a>' +\
        '</button>'

# welcome page
@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    return render_template('welcome.html') 

#get all
@app.route('/wines')
def getAll():
    return jsonify(wineDao.getAll())

# find By id
@app.route('/wines/<int:ID>')
def findById(ID):
    foundWine = wineDao.findById(ID)
    if not foundWine:
        abort(400)
    return jsonify(foundWine)

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

# update
@app.route('/wines/<int:ID>', methods=['PUT'])
def update(ID):
    foundWine = wineDao.findById(ID)
    if not foundWine:
        abort(404)

    if not request.json:
        abort(400)
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