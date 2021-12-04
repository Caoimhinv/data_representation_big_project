from flask import Flask, url_for, request, redirect, abort, jsonify

from zWineDAO import wineDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello"

# get all
@app.route('/wine')
def getAll():
    return jsonify(wineDAO.getAll())


# find by ID
@app.route('/wine/<int:id>')
def findById(id):
  
    return jsonify(wineDAO.findByID(id))

# create
@app.route('/wine', methods=['POST'])
def create():
    if not request.json:
        abort(400)

    wine = {
        "id": request.json["id"],
        "name": request.json["name"],
        "vintage": request.json["vintage"],
        "country": request.json["country"],
        "grape": request.json["grape"],
        "region": request.json["region"],
        "colour": request.json["colour"]
    }
    return jsonify(wineDAO.create(wine))

# update
@app.route('/wine/<int:id>', methods=['PUT'])
def update(id):
    foundWine = wineDAO.findByID(id)
    print(foundWine)
    if foundWine == {}:
        return jsonify([]), 404
    currentWine = foundWine
    if 'id' in request.json:
        currentWine['id'] = request.json["id"]
    if 'name' in request.json:
        currentWine['name'] = request.json["name"]
    if 'vintage' in request.json:
        currentWine['vintage'] = request.json["vintage"]
    if 'country' in request.json:
        currentWine['country'] = request.json["country"]
    if 'grape' in request.json:
        currentWine['grape'] = request.json["grape"]
    if 'region' in request.json:
        currentWine['region'] = request.json["region"]
    if 'colour' in request.json:
        currentWine['colour'] = request.json["colour"]
    wineDAO.update(currentWine)

    return jsonify(currentWine)

# delete
@app.route('/wine/<int:id>', methods=['DELETE'])
def delete(id):
    wineDAO.delete(id)

    return jsonify({"done": True})

if __name__ == "__main__":
    app.run(debug=True)

# curl -X POST -d "{\"id\":1, \"name\":\"opus_one\", \"vintage\":1979, \"country\":\"USA\", \"grape\":\"cabernet_sauvignon\", \"region\":\"california\", \"colour\":\"red\"}" -H Content-Type:application/json http://127.0.0.1:5000/wine 