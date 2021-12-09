import mysql.connector
from mysql.connector import cursor
import dbConfig as cfg

class WineDao:
    def initConnectToDB(self):
        db = mysql.connector.connect(
            host = cfg.mysql['host'],
            user = cfg.mysql['user'],
            password = cfg.mysql['password'],
            database = cfg.mysql['database'],
            pool_name = 'my_connection_pool',
            pool_size = 10
        )
        return db
    
    def getConnection(self):
        db = mysql.connector.connect(
            pool_name = 'my_connection_pool',
        )
        return db

    def __init__(self):
        db = self.initConnectToDB()
        db.close()

    def create(self, wine):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "insert into wines3 (nameProducer, vintage, regionCountry) values (%s, %s, %s)"
        values = [
            wine['nameProducer'],
            wine['vintage'],
            wine['regionCountry'],
        ]
        cursor.execute(sql, values)
        db.commit()
        lastRowId = cursor.lastrowid
        db.close()
        return lastRowId

    def getAll(self):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'select * from wines3'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        db.close()
        return returnArray

    def findById(self, ID):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'select * from wines3 where ID = %s'
        values = [ID]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        wine = self.convertToDict(result)
        db.close()
        return wine
        
    def update(self, wine):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "update wines3 set nameProducer = %s, vintage = %s, regionCountry = %s where ID = %s"
        values = [
            wine['nameProducer'],
            wine['vintage'],
            wine['regionCountry'],
            wine['ID'],
        ]
        cursor.execute(sql,values)
        db.commit()
        db.close()
        return wine

    def delete(self, ID):
        db = self.getConnection()
        cursor = db.cursor()
        sql = 'delete from wines3 where ID = %s'
        values = [ID]
        cursor.execute(sql, values)
        db.commit()
        db.close()
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
        cursor = self.getCursor()
        sql="SELECT * FROM users where email = %s and password=%s"
        values = (email, password)
        cursor.execute(sql, values)
            # Fetch one record and return result
        account = cursor.fetchone()
        cursor.close()
        return self.convertToDictionary2(account)

            #result = cursor.fetchone()
            #ßprint(result)
        print("Hello Caoimhin")

    def convertToDictionary2(self, account):
        colnames=["ID", "name", "email", "password"]
        print(colnames)
        item = {}

        if account:
            for i, colname in enumerate(colnames):
                print(colnames)
                value = account[i]
                item[colname] = value
        return item

wineDao = WineDao()