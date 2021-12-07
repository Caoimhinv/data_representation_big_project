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
        sql = "insert into wines (ID, name, producer, vintage, country_region, grape_style) values (%s,%s,%s,%s,%s,%s)"
        values = [
            wine['ID'],
            wine['name'],
            wine['producer'],
            wine['vintage'],
            wine['country_region'],
            wine['grape_style']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from wines'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, ID):
        cursor = self.db.cursor()
        sql = 'select * from wines where ID = %s'
        values = [ ID ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, wine):
       cursor = self.db.cursor()
       sql = "update wines set name = %s, producer = %s, vintage = %s,  country_region = %s, grape_style = %s where ID = %s"
       values = [
            wine['name'],
            wine['producer'],
            wine['vintage'],
            wine['country_region'],
            wine['grape_style'],
            wine['ID'],
        ]
       cursor.execute(sql, values)
       self.db.commit()
       return wine

    def delete(self, ID):
       cursor = self.db.cursor()
       sql = 'delete from wines where ID = %s'
       values = [ID]
       cursor.execute(sql, values)
       
       return {}

    def convertToDict(self, result):
        colnames = ['ID','name', 'producer', 'vintage', 'country_region', 'grape_style']
        wine = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                wine[colName] = value
        return wine

wineDao = WineDao()