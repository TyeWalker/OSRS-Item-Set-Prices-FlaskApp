import mysql.connector
import datetime, timeago
import re

# SQL Prepared Statement:
select_set = ("SELECT A.itemID, A.itemName, B.itemHigh, B.itemHighTime, B.itemLow, B.itemLowTime "
                "FROM item A, itemlatest B "
                "WHERE A.itemID = B.itemID AND A.itemID = %s")


def internalLink(name):
    new_name = re.sub('\'', "-", name)
    final_name = re.sub(' ', '-', new_name)
    return final_name.lower()


def homePage(myItem = [], *args):
    all_items_tuple = tuple()
    now = datetime.datetime.now()
    connectDB = mysql.connector.connect(host="localhost", user="root", passwd="", database="osrsprices", port=3303)
    cursor = connectDB.cursor()
    for x in myItem:
        select_tuple = (str(x[-1]), )
        cursor.execute(select_set, select_tuple)
        myresult = cursor.fetchone()
        diff = int(myresult[2]) - int(myresult[4])
        item_set_tuple = (myresult[0], str(myresult[0]) + ".png", myresult[1], myresult[2], timeago.format(myresult[3], now), myresult[4], timeago.format(myresult[5], now), internalLink(myresult[1]), diff)
        all_items_tuple = all_items_tuple + (item_set_tuple,)
    return all_items_tuple