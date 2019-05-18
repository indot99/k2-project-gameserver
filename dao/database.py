#-*- coding:utf-8 -*-
import jsonify
import pymysql

def getConnection():
    return pymysql.connect(host='127.0.0.1',port=3306, user='root', password='sin5chel',
                            db='k2server',charset='utf8')

def CheckLogin(_id,_pw):
    conn = getConnection()
    cursor = conn.cursor()
    sql = "SELECT * FROM `TBLuser` WHERE `id` = '%s' AND `pw` = '%s';" %(_id,_pw)
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result)>0:
        return result
    else:
        return 'n'

def CheckRegister(_id,_pw,_name):

    data = {
        "id" : True,
        "pw" : True,
        "name" : True
    }

    conn = getConnection()
    cursor = conn.cursor()
    sql = "SELECT * FROM `TBLuser` WHERE `id` = '%s'" %(_id)
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result)>0:
        data["id"] = False
    sql = "SELECT * FROM `TBLuser` WHERE `nickname` = '%s'" %(_name)
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result)>0:
        data["name"] = False

    if data["id"] == True and data["pw"] == True and data["name"] == True:
        sql = "INSERT INTO `TBLuser` (`id`,`pw`,`nickname`) VALUES('%s','%s','%s')" %(_id,_pw,_name)
        cursor.execute(sql)
        conn.commit()
        conn.close()
    return data

##이부분##
def GetDictionaryInfo(tablename):
    conn = getConnection()
    cursor = conn.cursor()
    sql = "SELECT * FROM `%s`" %(tablename)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

    