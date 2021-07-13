import mysql.connector

graph_set_hour_high = (
    "select DATE_ADD(date(itemHighTime), INTERVAL EXTRACT(HOUR FROM itemHighTime) HOUR) as FETCH_DATE_HOUR, ROUND(avg(itemHigh)) as itemHigh "
    "FROM itemhightimes "
    "WHERE itemID = %s AND itemHighTime > DATE_SUB(CURDATE(), INTERVAL 1 DAY) "
    "group by date(itemHighTime), EXTRACT(HOUR FROM itemHighTime)")
graph_set_hour_low = (
    "select DATE_ADD(date(itemLowTime), INTERVAL EXTRACT(HOUR FROM itemLowTime) HOUR) as FETCH_DATE_HOUR, ROUND(avg(itemLow)) as itemLow "
    "FROM itemlowtimes "
    "WHERE itemID = %s AND itemLowTime > DATE_SUB(CURDATE(), INTERVAL 1 DAY) "
    "group by date(itemLowTime), EXTRACT(HOUR FROM itemLowTime)")


def itemGraphHigh(myItem=[], *args):
    high_set_labels = []
    high_set_values = []
    # Connect to DB:
    connectDB = mysql.connector.connect(host="localhost", user="root", passwd="", database="osrsprices", port=3303)
    cursor = connectDB.cursor()
    tuple_set = (str(myItem[-1]),)
    cursor.execute(graph_set_hour_high, tuple_set)
    graph_data_high = cursor.fetchall()
    for x in graph_data_high:
        high_set_labels.append(x[0].strftime("%d/%m-%H-%M"))
        high_set_values.append(x[1])
    connectDB.commit()
    cursor.close()
    connectDB.close()
    return high_set_labels, high_set_values


def itemGraphLow(myItem=[], *args):
    low_set_labels = []
    low_set_values = []
    connectDB = mysql.connector.connect(host="localhost", user="root", passwd="", database="osrsprices", port=3303)
    cursor = connectDB.cursor()
    tuple_set = (str(myItem[-1]),)
    cursor.execute(graph_set_hour_low, tuple_set)
    graph_data_low = cursor.fetchall()
    for z in graph_data_low:
        low_set_labels.append(z[0].strftime("%d/%m-%H-%M"))
        low_set_values.append(z[1])
    connectDB.commit()
    cursor.close()
    connectDB.close()
    return low_set_labels, low_set_values
