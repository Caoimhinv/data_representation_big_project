from zWineDAO import wineDAO


wine1 = {
    'name': 'buckfast',
    'vintage': 0,
    'country': 'england',
    'grape': 'unknown',
    'region': 'devon',
    'colour': 'brownish'
}
wine2 = {
    'id': 4,
    'name': 'buckfast',
    'vintage': 2020,
    'country': 'england',
    'grape': 'notGrapes!',
    'region': 'devon',
    'colour': 'brownish'
}
# wineDAO.create(wine)

returnValue = wineDAO.getAll()
print(returnValue)
returnValue = wineDAO.findByID(wine2['id'])
print("find by ID")
returnValue = wineDAO.update(wine2)
print(returnValue)
returnValue = wineDAO.findByID(wine2['id'])
print(returnValue)
returnValue = wineDAO.delete(wine2['id'])
print(returnValue)
returnValue = wineDAO.getAll()
print(returnValue)

