# imports necessary libraries
import mysql.connector
from mysql.connector import cursor
import dbConfig as cfg

class WineDao:

    # mySQL connection using config file
    db=""
    def connectToDB(self):
        self.db = mysql.connector.connect(
            host = cfg.mysql['host'],
            user = cfg.mysql['user'],
            password = cfg.mysql['password'],
            database = cfg.mysql['database'],
        )

    def __init__(self):
        self.connectToDB()
    
    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()

    # creates and inserts a wine into database
    def create(self, wine):
        cursor = self.getCursor()
        sql = "insert into wines3 (nameProducer, vintage, regionCountry) values (%s, %s, %s)"
        values = [
            wine['nameProducer'],
            wine['vintage'],
            wine['regionCountry'],
        ]
        cursor.execute(sql, values)
        self.db.commit()
        lastRowId = cursor.lastrowid
        cursor.close()
        return lastRowId

    # returns all wines from database
    def getAll(self):
        cursor = self.getCursor()
        sql = 'select * from wines3'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        cursor.close()
        return returnArray

    # returns a specific wine from database
    def findById(self, ID):
        cursor = self.getCursor()
        sql = 'select * from wines3 where ID = %s'
        values = [ID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        wine = self.convertToDict(result)
        cursor.close()
        return wine
    
    # updates a wine in database
    def update(self, wine):
        cursor = self.getCursor()
        sql = "update wines3 set nameProducer = %s, vintage = %s, regionCountry = %s where ID = %s"
        values = [
            wine['nameProducer'],
            wine['vintage'],
            wine['regionCountry'],
            wine['ID'],
        ]
        cursor.execute(sql,values)
        self.db.commit()
        cursor.close()
        return wine

    # deletes a wine from database
    def delete(self, ID):
        cursor = self.getCursor()
        sql = 'delete from wines3 where ID = %s'
        values = [ID]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return {}

    # converts the values to dictionary items
    def convertToDict(self, result):
        colnames = ['ID', 'nameProducer', 'vintage', 'regionCountry']
        wine = {}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                wine[colName] = value
        return wine

    # checks user is in database
    def checkUser(self, email, password):
        cursor = self.getCursor()
        sql="SELECT * FROM users where email=%s and password=%s"
        values = (email, password)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToDictionary2(result)

    # converts the values to dictionary items
    def convertToDictionary2(self, result):
        colNames=["ID", "name", "email", "password"]
        print(colNames)
        item = {}
        if result:
            for i, colName in enumerate(colNames):
                print(colNames)
                value = result[i]
                item[colName] = value
        return item

wineDao = WineDao()