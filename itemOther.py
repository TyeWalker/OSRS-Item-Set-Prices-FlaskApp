import mysql.connector
import re

link_pricesrswiki = "https://oldschool.runescape.wiki/w/"               # takes name, eg: https://oldschool.runescape.wiki/w/Ahrim%27s_armour_set
link_platinumtokens = "https://platinumtokens.com/item/"                # takes name, eg: https://platinumtokens.com/item/rune-dart-tip
link_getracker = "https://www.ge-tracker.com/item/"                     # takes name, eg: https://www.ge-tracker.com/item/extended-antifire-4

# SQL:
select_high = ("SELECT itemHigh, itemLow "
               "FROM itemlatest "
               "WHERE itemID = %s")
select_name = ("SELECT itemName "
               "FROM item WHERE "
               "itemID = %s")


# Individual High & Low Calculation:
def indCalc(myItem = [], *args):
    high_total = 0
    low_total = 0
    # Connect to DB:
    connectDB = mysql.connector.connect(host="localhost", user="root", passwd="", database="osrsprices", port=3303)
    cursor = connectDB.cursor()
    for x in myItem[0:-1]:
        select_tuple = (str(x), )
        cursor.execute(select_high, select_tuple)
        myresult = cursor.fetchone()
        high_total = high_total + myresult[0]
        low_total = low_total + myresult[1]
    connectDB.commit()
    cursor.close()
    connectDB.close()
    return high_total, low_total


# Links:
# Rename Strings to insert into URL:
def rename_link_pt(item_name):
    new_item_name = re.sub(r'[^\w\s]', '', item_name)
    final_item_name = re.sub(' ', '-', new_item_name)
    return final_item_name.lower()


def rename_link_getracker(item_name):
    new_item_name = re.sub('\'', "-", item_name)
    final_item_name = re.sub(' ', '-', new_item_name)
    return final_item_name.lower()


def rename_link_wiki(item_name):
    new_item_name = re.sub('\'', "%27", item_name)
    final_item_name = re.sub(' ', '_', new_item_name)
    return final_item_name.lower()


def itemLinks(myItem = [], *args):
    all_links = tuple()
    # Connect to DB:
    connectDB = mysql.connector.connect(host="localhost", user="root", passwd="", database="osrsprices", port=3303)
    cursor = connectDB.cursor()
    # Create Links:
    for x in myItem:
        select_tuple = (str(x), )
        cursor.execute(select_name, select_tuple)
        myresult = cursor.fetchone()
        rswiki = link_pricesrswiki + rename_link_wiki(myresult[0])
        item_rename = rename_link_pt(str(myresult[0]))
        p_link = link_platinumtokens + item_rename
        ge_link = link_getracker + rename_link_getracker(str(myresult[0]))
        link_tuple = (myresult[0], rswiki, p_link, ge_link)
        all_links = all_links + (link_tuple, )
    connectDB.commit()
    cursor.close()
    connectDB.close()
    return all_links