from flask import Flask, url_for, request, redirect, abort, jsonify, render_template
from WineDao import wineDao

app = Flask(__name__, static_url_path='', static_folder='static_pages')

# from - https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/
# Route for handling the login page logic
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

@app.route('/')
def home():
    return "hello"

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    return render_template('welcome.html')  # render a template

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