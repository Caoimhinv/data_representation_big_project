import mysql.connector
from mysql.connector import cursor
import dbConfig as cfg

class WineDao:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = cfg.mysql['host'],
            user = cfg.mysql['user'],
            password = cfg.mysql['password'],
            database = cfg.mysql['database']
        )

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
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from wines3'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        return returnArray

    def findById(self, ID):
        cursor = self.db.cursor()
        sql = 'select * from wines3 where ID = %s'
        values = [ ID ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        
    def update(self, wine):
        cursor = self.db.cursor()
        sql = "update wines3 set nameProducer = %s, vintage = %s, regionCountry = %s where ID = %s"
        values = [
            wine['nameProducer'],
            wine['vintage'],
            wine['regionCountry'],
            wine['ID'],
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return wine

    def delete(self, ID):
        cursor = self.db.cursor()
        sql = 'delete from wines3 where ID = %s'
        values = [ ID ]
        cursor.execute(sql, values)
        self.db.commit()
        return {}

    def convertToDict(self, result):
        colnames = ['ID', 'nameProducer', 'vintage', 'regionCountry']
        wine = {}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                wine[colName] = value
        return wine

wineDao = WineDao()