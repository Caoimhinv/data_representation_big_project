import mysql.connector

class WineDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Francie3",
            database = "wineCellar"
        )
        # print("connection made")

    def create(self, wine):
        cursor = self.db.cursor()
        sql = "insert into wine (name, vintage, country, grape, region, colour) values (%s, %s, %s, %s, %s, %s)"
        values = [
            wine['name'],
            wine['vintage'],
            wine['country'],
            wine['grape'],
            wine['region'],
            wine['colour']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from wine"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        
        return returnArray

    def convertToDict(self, result):
        colNames = ['name', 'vintage', 'country', 'grape', 'region', 'colour']
        wine = {}
        if result:
            for i, colName in enumerate(colNames):
                value = result[i]
                wine[colName] = value
        return wine

    def findByID(self, id):
        cursor = self.db.cursor()
        sql = "select * from wine where id = %s"
        values = [ id ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)

    def update(self, wine):
        cursor = self.db.cursor()
        sql = "update wine set name = %s, vintage = %s, country = %s, grape = %s, region = %s, colour = %s"
        values = [
            wine['name'],
            wine['vintage'],
            wine['country'],
            wine['grape'],
            wine['region'],
            wine['colour']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return wine

    def delete(self, id):
        cursor = self.db.cursor()
        sql = "delete from wine where id = %s"
        values = [ id ]
        cursor.execute(sql, values)
       
        return {}
    
wineDAO = WineDAO()