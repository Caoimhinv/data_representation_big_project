from flask import Flask, url_for, request, redirect, abort, jsonify, render_template, session, make_response
from WineDao import wineDao

app = Flask(__name__, static_url_path='', static_folder='static_pages')

# from - https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/
# NOT WORKING THOUGH?????
# https://github.com/RitRa/data-representation-project/blob/master/application.py
# https://stackoverflow.com/questions/20137688/login-with-flask-framework

# ----
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

# ------

# app.secret_key = 'betyacantguessthis1'

# @app.route('/')
# def home():
#     if not 'username' in session:
#         return redirect(url_for('login'))
#     # return render_template('welcome.html')
#     return 'Welcome ' + session['username'] +\
#         '<br>' +\
#         '<button>' +\
#             '<a href="'+url_for('welcome')+'">' +\
#                 'Continue' +\
#             '</a>' +\
#         '</button>' +\
#         '<button>' +\
#             '<a href="'+url_for('logout')+'">' +\
#                 'Logout' +\
#             '</a>' +\
#         '</button>'

@app.route('/')
def home():
    return 'Hello you!' +\
        '<br>' +\
        '<button>' +\
            '<a href="'+url_for('login')+'">' +\
                'Continue' +\
            '</a>' +\
        '</button>'

# @app.route('/login')
# def login():
#     return '<h1>Login</h1> '+\
#         '<body style="background-color:ivory;">'+\
#         '<button>'+\
#             '<a href="'+url_for('process_login')+'">' +\
#                 'Login' +\
#             '</a>' +\
#         '</button>' +\
#         '</body>' +\
#         '<img src="https://media.istockphoto.com/vectors/red-wine-glass-icon-illustration-vector-id1132889797?k=20&m=1132889797&s=612x612&w=0&h=789LAtKiSQynEGPCS_j3nivLwWPkaCgDAYeLeCM6rYI=" +\
#         alt="Wine_image" align="top" height=300 width=400>'

# @app.route('/processlogin')
# def process_login():
#     session['username'] = "Wine Person!"
#     return redirect(url_for('home'))

# @app.route('/logout')
# def logout():
#     session.pop('username',None)
#     return redirect(url_for('home'))

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
    # return "served by Create "

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