from flask import Flask, url_for, request, redirect, abort, jsonify
from WineDao import wineDao

app = Flask(__name__, static_url_path='', static_folder='static_pages')


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
# curl -X POST -d "{\"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}" http://127.0.0.1:5000/wines


@app.route('/wines', methods=['POST'])
def create():
   
    if not request.json:
        abort(400)

    wine = {
        # "ID": request.json["ID"],
        "name": request.json["name"],
        "producer": request.json["producer"],
        "vintage": request.json["vintage"],
        "country_region": request.json["country_region"],
        "grape_style": request.json["grape_style"]
    }
    return jsonify(wineDao.create(wine))

    return "served by Create "

#update
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/wines/1


@app.route('/wines/<int:ID>', methods=['PUT'])
def update(ID):
    foundWine=wineDao.findById(ID)
    print (foundWine)
    if foundWine == {}:
        return jsonify({}), 404
    currentWine = foundWine
    if 'name' in request.json:
        currentWine['name'] = request.json['name']
    if 'producer' in request.json:
        currentWine['producer'] = request.json['producer']
    if 'vintage' in request.json:
        currentWine['vintage'] = request.json['vintage']
    if 'country/region' in request.json:
        currentWine['country_region'] = request.json['country_region']
    if 'grape/style' in request.json:
        currentWine['grape_style'] = request.json['grape_style']
    wineDao.update(currentWine)

    return jsonify(currentWine)

#delete
# curl -X DELETE http://127.0.0.1:5000/wines/1


@app.route('/wines/<int:ID>', methods=['DELETE'])
def delete(ID):
    wineDao.delete(ID)

    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug=True)