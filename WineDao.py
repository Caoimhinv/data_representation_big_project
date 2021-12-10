import mysql.connector
from mysql.connector import cursor
import dbConfig as cfg

class WineDao:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = cfg.mysql['host'],
            user = cfg.mysql['user'],
            password = cfg.mysql['password'],
            database = cfg.mysql['database'],
        )
        # return db
    
    # def getConnection(self):
    #     db = mysql.connector.connect(
    #         pool_name = 'my_connection_pool',
    #     )
    #     return db

    # def __init__(self):
    #     db = self.initConnectToDB()
    #     db.close()

    def create(self, wine):
        cursor = self.db.cursor()
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

    def getAll(self):
        cursor = self.db.cursor()
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

    def findById(self, ID):
        cursor = self.db.cursor()
        sql = 'select * from wines3 where ID = %s'
        values = [ID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        wine = self.convertToDict(result)
        cursor.close()
        return wine
        
    def update(self, wine):
        cursor = self.db.cursor()
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

    def delete(self, ID):
        cursor = self.db.cursor()
        sql = 'delete from wines3 where ID = %s'
        values = [ID]
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()
        return {}

    def convertToDict(self, result):
        colnames = ['ID', 'nameProducer', 'vintage', 'regionCountry']
        wine = {}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                wine[colName] = value
        return wine

    def checkUser(self, email, password):
        cursor = self.db.cursor()
        sql="SELECT * FROM users where email=%s and password=%s"
        values = (email, password)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        return self.convertToDictionary2(result)

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