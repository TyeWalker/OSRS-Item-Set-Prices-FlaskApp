import mysql.connector
import datetime, timeago


item_high_total = []
item_low_total = []
high_set_values = []
high_set_labels = []
low_set_values = []
low_set_labels = []

# Prepared SQL statement:
select_item = ("SELECT A.itemName, B.itemHigh, B.itemHighTime, B.itemLow, B.itemLowTime, "
               "C.ohHighPriceVolume, C.ohLowPriceVolume, D.odHighPriceVolume, D.odLowPriceVolume, A.itemGELimit, "
               "A.itemHighAlch "
               "FROM item A, itemlatest B, onehourvolume C, onedayvolume D "
               "WHERE A.itemID = %s AND A.itemID = B.itemID AND B.itemID = C.itemID AND C.itemID = D.itemID")


def itemTableData(myItem = [], *args):
    all_items_tuple = tuple()
    now = datetime.datetime.now()
    # Connect to DB:
    connectDB = mysql.connector.connect(host="localhost", user="root", passwd="", database="osrsprices", port=3303)
    cursor = connectDB.cursor()
    for x in myItem:
        query_tuple = (str(x), )
        cursor.execute(select_item, query_tuple)
        myresult = cursor.fetchone()
        margin = (((int(myresult[1]) - int(myresult[3])) / myresult[3]) * 100)
        format_margin = "{:.2f}".format(margin)
        item_tuple = (x, str(x)+".png", myresult[0], myresult[1], timeago.format(myresult[2], now), myresult[3], timeago.format(myresult[4], now), int(myresult[1]) - int(myresult[3]), str(format_margin) + "%", int(myresult[5]) + int(myresult[6]), int(myresult[7]) + int(myresult[8]), myresult[9], myresult[10])
        all_items_tuple = all_items_tuple + (item_tuple,)
    connectDB.commit()
    cursor.close()
    connectDB.close()
    return all_items_tuple