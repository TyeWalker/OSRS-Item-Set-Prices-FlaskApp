from flask import Flask, redirect, url_for, render_template
import os
import itemHome
import itemOther
import itemTable
import itemList
import itemGraph

# Links:
link_pricesrswiki = "https://prices.runescape.wiki/osrs/item/"          # takes itemID
link_platinumtokens = "https://platinumtokens.com/item/"                # takes name
link_getracker = "https://www.ge-tracker.com/item/"                     # takes name


app = Flask(__name__)
imageFolder = os.path.join('templates', 'pics')


# Home Page:
@app.route("/")
def home():
    barrows_set = itemHome.homePage(itemList.Barrows)
    gold_trimmed_legs_set = itemHome.homePage(itemList.Gold_trimmed_sm_lg)
    trimmed_sm_legs_set = itemHome.homePage(itemList.Trimmed_sm_lg)
    gold_trimmed_skirt_set = itemHome.homePage(itemList.Gold_trimmed_sm_sk)
    trimmed_sm_sk_set = itemHome.homePage(itemList.Trimmed_sm_sk)
    god_blessed_set = itemHome.homePage(itemList.God_blessed_dhide)
    return render_template("home.html", barrows = barrows_set, gtlegs = gold_trimmed_legs_set,
                           tsmlegs = trimmed_sm_legs_set, gtskirt = gold_trimmed_skirt_set,
                           tsmskirt = trimmed_sm_sk_set, godblessed = god_blessed_set)

#
# Barrows:
# Ahrim
@app.route("/sets/ahrim-s-armour-set/")
def ahrim():
    item_row = itemTable.itemTableData(itemList.Ahrim)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Ahrim)
    item_graph_low = itemGraph.itemGraphLow(itemList.Ahrim)
    item_ind_calc = itemOther.indCalc(itemList.Ahrim)
    item_links = itemOther.itemLinks(itemList.Ahrim)
    return render_template("barrows/ahrim.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Dharok
@app.route("/sets/dharok-s-armour-set/")
def dharok():
    item_row = itemTable.itemTableData(itemList.Dharok)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Dharok)
    item_graph_low = itemGraph.itemGraphLow(itemList.Dharok)
    item_ind_calc = itemOther.indCalc(itemList.Dharok)
    item_links = itemOther.itemLinks(itemList.Dharok)
    return render_template("barrows/dharok.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Guthan
@app.route("/sets/guthan-s-armour-set/")
def guthan():
    item_row = itemTable.itemTableData(itemList.Guthan)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Guthan)
    item_graph_low = itemGraph.itemGraphLow(itemList.Guthan)
    item_ind_calc = itemOther.indCalc(itemList.Guthan)
    item_links = itemOther.itemLinks(itemList.Guthan)
    return render_template("barrows/guthan.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Karil
@app.route("/sets/karil-s-armour-set/")
def karil():
    item_row = itemTable.itemTableData(itemList.Karil)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Karil)
    item_graph_low = itemGraph.itemGraphLow(itemList.Karil)
    item_ind_calc = itemOther.indCalc(itemList.Karil)
    item_links = itemOther.itemLinks(itemList.Karil)
    return render_template("barrows/karil.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Torag
@app.route("/sets/torag-s-armour-set/")
def torag():
    item_row = itemTable.itemTableData(itemList.Torag)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Torag)
    item_graph_low = itemGraph.itemGraphLow(itemList.Torag)
    item_ind_calc = itemOther.indCalc(itemList.Torag)
    item_links = itemOther.itemLinks(itemList.Torag)
    return render_template("barrows/torag.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Verac
@app.route("/sets/verac-s-armour-set/")
def verac():
    item_row = itemTable.itemTableData(itemList.Verac)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Verac)
    item_graph_low = itemGraph.itemGraphLow(itemList.Verac)
    item_ind_calc = itemOther.indCalc(itemList.Verac)
    item_links = itemOther.itemLinks(itemList.Verac)
    return render_template("barrows/verac.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Gold-Trimmed Standard Metal (lg)
# Bronze:
@app.route("/sets/bronze-gold-trimmed-set-(lg)/")
def bronzeGTSMLG():
    item_row = itemTable.itemTableData(itemList.Bronze_gt_lg)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Bronze_gt_lg)
    item_graph_low = itemGraph.itemGraphLow(itemList.Bronze_gt_lg)
    item_ind_calc = itemOther.indCalc(itemList.Bronze_gt_lg)
    item_links = itemOther.itemLinks(itemList.Bronze_gt_lg)
    return render_template("goldtrimmedsmlg/bronzegtslg.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Iron:
@app.route("/sets/iron-gold-trimmed-set-(lg)/")
def ironGTSMLG():
    item_row = itemTable.itemTableData(itemList.Iron_gt_lg)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Iron_gt_lg)
    item_graph_low = itemGraph.itemGraphLow(itemList.Iron_gt_lg)
    item_ind_calc = itemOther.indCalc(itemList.Iron_gt_lg)
    item_links = itemOther.itemLinks(itemList.Iron_gt_lg)
    return render_template("goldtrimmedsmlg/irongtslg.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Steel:
@app.route("/sets/steel-gold-trimmed-set-(lg)/")
def steelGTSMLG():
    item_row = itemTable.itemTableData(itemList.Steel_gt_lg)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Steel_gt_lg)
    item_graph_low = itemGraph.itemGraphLow(itemList.Steel_gt_lg)
    item_ind_calc = itemOther.indCalc(itemList.Steel_gt_lg)
    item_links = itemOther.itemLinks(itemList.Steel_gt_lg)
    return render_template("goldtrimmedsmlg/steelgtslg.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Black:
@app.route("/sets/black-gold-trimmed-set-(lg)/")
def blackGTSMLG():
    item_row = itemTable.itemTableData(itemList.Black_gt_lg)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Black_gt_lg)
    item_graph_low = itemGraph.itemGraphLow(itemList.Black_gt_lg)
    item_ind_calc = itemOther.indCalc(itemList.Black_gt_lg)
    item_links = itemOther.itemLinks(itemList.Black_gt_lg)
    return render_template("goldtrimmedsmlg/blackgtslg.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Mithril:
@app.route("/sets/mithril-gold-trimmed-set-(lg)/")
def mithrilGTSMLG():
    item_row = itemTable.itemTableData(itemList.Mithril_gt_lg)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Mithril_gt_lg)
    item_graph_low = itemGraph.itemGraphLow(itemList.Mithril_gt_lg)
    item_ind_calc = itemOther.indCalc(itemList.Mithril_gt_lg)
    item_links = itemOther.itemLinks(itemList.Mithril_gt_lg)
    return render_template("goldtrimmedsmlg/mithrilgtslg.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Adamant:
@app.route("/sets/adamant-gold-trimmed-set-(lg)/")
def adamantGTSMLG():
    item_row = itemTable.itemTableData(itemList.Adamant_gt_lg)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Adamant_gt_lg)
    item_graph_low = itemGraph.itemGraphLow(itemList.Adamant_gt_lg)
    item_ind_calc = itemOther.indCalc(itemList.Adamant_gt_lg)
    item_links = itemOther.itemLinks(itemList.Adamant_gt_lg)
    return render_template("goldtrimmedsmlg/adamantgtslg.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Rune:
@app.route("/sets/rune-gold-trimmed-set-(lg)/")
def runeGTSMLG():
    item_row = itemTable.itemTableData(itemList.Rune_gt_lg)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Rune_gt_lg)
    item_graph_low = itemGraph.itemGraphLow(itemList.Rune_gt_lg)
    item_ind_calc = itemOther.indCalc(itemList.Rune_gt_lg)
    item_links = itemOther.itemLinks(itemList.Rune_gt_lg)
    return render_template("goldtrimmedsmlg/runegtslg.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Gilded:
@app.route("/sets/gilded-armour-set-(lg)/")
def gildedGTSMLG():
    item_row = itemTable.itemTableData(itemList.Gilded_gt_lg)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Gilded_gt_lg)
    item_graph_low = itemGraph.itemGraphLow(itemList.Gilded_gt_lg)
    item_ind_calc = itemOther.indCalc(itemList.Gilded_gt_lg)
    item_links = itemOther.itemLinks(itemList.Gilded_gt_lg)
    return render_template("goldtrimmedsmlg/gildedslg.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Gold-Trimmed Standard Metal (sk)
# Bronze:
@app.route("/sets/bronze-gold-trimmed-set-(sk)/")
def bronzeGTSMSK():
    item_row = itemTable.itemTableData(itemList.Bronze_gt_sk)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Bronze_gt_sk)
    item_graph_low = itemGraph.itemGraphLow(itemList.Bronze_gt_sk)
    item_ind_calc = itemOther.indCalc(itemList.Bronze_gt_sk)
    item_links = itemOther.itemLinks(itemList.Bronze_gt_sk)
    return render_template("goldtrimmedsmsk/bronzegtssk.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Iron:
@app.route("/sets/iron-gold-trimmed-set-(sk)/")
def ironGTSMSK():
    item_row = itemTable.itemTableData(itemList.Iron_gt_sk)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Iron_gt_sk)
    item_graph_low = itemGraph.itemGraphLow(itemList.Iron_gt_sk)
    item_ind_calc = itemOther.indCalc(itemList.Iron_gt_sk)
    item_links = itemOther.itemLinks(itemList.Iron_gt_sk)
    return render_template("goldtrimmedsmsk/bronzegtssk.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Steel:
@app.route("/sets/steel-gold-trimmed-set-(sk)/")
def steelGTSMSK():
    item_row = itemTable.itemTableData(itemList.Steel_gt_sk)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Steel_gt_sk)
    item_graph_low = itemGraph.itemGraphLow(itemList.Steel_gt_sk)
    item_ind_calc = itemOther.indCalc(itemList.Steel_gt_sk)
    item_links = itemOther.itemLinks(itemList.Steel_gt_sk)
    return render_template("goldtrimmedsmsk/steelgtssk.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Black:
@app.route("/sets/black-gold-trimmed-set-(sk)/")
def blackGTSMSK():
    item_row = itemTable.itemTableData(itemList.Black_gt_sk)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Black_gt_sk)
    item_graph_low = itemGraph.itemGraphLow(itemList.Black_gt_sk)
    item_ind_calc = itemOther.indCalc(itemList.Black_gt_sk)
    item_links = itemOther.itemLinks(itemList.Black_gt_sk)
    return render_template("goldtrimmedsmsk/blackgtssk.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Mithril:
@app.route("/sets/mithril-gold-trimmed-set-(sk)/")
def mithrilGTSMSK():
    item_row = itemTable.itemTableData(itemList.Mithril_gt_sk)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Mithril_gt_sk)
    item_graph_low = itemGraph.itemGraphLow(itemList.Mithril_gt_sk)
    item_ind_calc = itemOther.indCalc(itemList.Mithril_gt_sk)
    item_links = itemOther.itemLinks(itemList.Mithril_gt_sk)
    return render_template("goldtrimmedsmsk/mithrilgtssk.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# adamant:
@app.route("/sets/adamant-gold-trimmed-set-(sk)/")
def adamantGTSMSK():
    item_row = itemTable.itemTableData(itemList.Adamant_gt_sk)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Adamant_gt_sk)
    item_graph_low = itemGraph.itemGraphLow(itemList.Adamant_gt_sk)
    item_ind_calc = itemOther.indCalc(itemList.Adamant_gt_sk)
    item_links = itemOther.itemLinks(itemList.Adamant_gt_sk)
    return render_template("goldtrimmedsmsk/adamantgtssk.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Rune:
@app.route("/sets/rune-gold-trimmed-set-(sk)/")
def runeGTSMSK():
    item_row = itemTable.itemTableData(itemList.Rune_gt_sk)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Rune_gt_sk)
    item_graph_low = itemGraph.itemGraphLow(itemList.Rune_gt_sk)
    item_ind_calc = itemOther.indCalc(itemList.Rune_gt_sk)
    item_links = itemOther.itemLinks(itemList.Rune_gt_sk)
    return render_template("goldtrimmedsmsk/runegtssk.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Gilded:
@app.route("/sets/gilded-armour-set-(sk)/")
def gildedGTSMSK():
    item_row = itemTable.itemTableData(itemList.Gilded_gt_sk)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Gilded_gt_sk)
    item_graph_low = itemGraph.itemGraphLow(itemList.Gilded_gt_sk)
    item_ind_calc = itemOther.indCalc(itemList.Gilded_gt_sk)
    item_links = itemOther.itemLinks(itemList.Gilded_gt_sk)
    return render_template("goldtrimmedsmsk/gildedssk.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Trimmed Standard Metal (lg)
# Bronze:
@app.route("/sets/bronze-trimmed-set-(lg)/")
def bronzeTMLG():
    item_row = itemTable.itemTableData(itemList.Bronze_t_lg)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Bronze_t_lg)
    item_graph_low = itemGraph.itemGraphLow(itemList.Bronze_t_lg)
    item_ind_calc = itemOther.indCalc(itemList.Bronze_t_lg)
    item_links = itemOther.itemLinks(itemList.Bronze_t_lg)
    return render_template("trimmedsmlg/bronzesmlg.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Iron:
@app.route("/sets/iron-trimmed-set-(lg)/")
def ironTMLG():
    item_row = itemTable.itemTableData(itemList.Iron_t_lg)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Iron_t_lg)
    item_graph_low = itemGraph.itemGraphLow(itemList.Iron_t_lg)
    item_ind_calc = itemOther.indCalc(itemList.Iron_t_lg)
    item_links = itemOther.itemLinks(itemList.Iron_t_lg)
    return render_template("trimmedsmlg/ironsmlg.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Steel:
@app.route("/sets/steel-trimmed-set-(lg)/")
def steelTMLG():
    item_row = itemTable.itemTableData(itemList.Steel_gt_t_lg)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Steel_gt_t_lg)
    item_graph_low = itemGraph.itemGraphLow(itemList.Steel_gt_t_lg)
    item_ind_calc = itemOther.indCalc(itemList.Steel_gt_t_lg)
    item_links = itemOther.itemLinks(itemList.Steel_gt_t_lg)
    return render_template("trimmedsmlg/steelsmlg.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Black:
@app.route("/sets/black-trimmed-set-(lg)/")
def blackTMLG():
    item_row = itemTable.itemTableData(itemList.Black_gt_t_lg)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Black_gt_t_lg)
    item_graph_low = itemGraph.itemGraphLow(itemList.Black_gt_t_lg)
    item_ind_calc = itemOther.indCalc(itemList.Black_gt_t_lg)
    item_links = itemOther.itemLinks(itemList.Black_gt_t_lg)
    return render_template("trimmedsmlg/blacksmlg.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Mithril:
@app.route("/sets/mithril-trimmed-set-(lg)/")
def mithrilTMLG():
    item_row = itemTable.itemTableData(itemList.Mithril_t_lg)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Mithril_t_lg)
    item_graph_low = itemGraph.itemGraphLow(itemList.Mithril_t_lg)
    item_ind_calc = itemOther.indCalc(itemList.Mithril_t_lg)
    item_links = itemOther.itemLinks(itemList.Mithril_t_lg)
    return render_template("trimmedsmlg/mithrilsmlg.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Adamant:
@app.route("/sets/adamant-trimmed-set-(lg)/")
def adamantTMLG():
    item_row = itemTable.itemTableData(itemList.Adamant_t_lg)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Adamant_t_lg)
    item_graph_low = itemGraph.itemGraphLow(itemList.Adamant_t_lg)
    item_ind_calc = itemOther.indCalc(itemList.Adamant_t_lg)
    item_links = itemOther.itemLinks(itemList.Adamant_t_lg)
    return render_template("trimmedsmlg/adamantsmlg.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Rune:
@app.route("/sets/rune-trimmed-set-(lg)/")
def runeTMLG():
    item_row = itemTable.itemTableData(itemList.Rune_t_lg)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Rune_t_lg)
    item_graph_low = itemGraph.itemGraphLow(itemList.Rune_t_lg)
    item_ind_calc = itemOther.indCalc(itemList.Rune_t_lg)
    item_links = itemOther.itemLinks(itemList.Rune_t_lg)
    return render_template("trimmedsmlg/runesmlg.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Trimmed Standard Metal (sk)
# Bronze:
@app.route("/sets/bronze-trimmed-set-(sk)/")
def bronzeTMSK():
    item_row = itemTable.itemTableData(itemList.Bronze_t_sk)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Bronze_t_sk)
    item_graph_low = itemGraph.itemGraphLow(itemList.Bronze_t_sk)
    item_ind_calc = itemOther.indCalc(itemList.Bronze_t_sk)
    item_links = itemOther.itemLinks(itemList.Bronze_t_sk)
    return render_template("trimmedsmsk/bronzesmsk.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Iron:
@app.route("/sets/iron-trimmed-set-(sk)/")
def ironTMSK():
    item_row = itemTable.itemTableData(itemList.Iron_t_sk)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Iron_t_sk)
    item_graph_low = itemGraph.itemGraphLow(itemList.Iron_t_sk)
    item_ind_calc = itemOther.indCalc(itemList.Iron_t_sk)
    item_links = itemOther.itemLinks(itemList.Iron_t_sk)
    return render_template("trimmedsmsk/ironsmsk.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Steel:
@app.route("/sets/steel-trimmed-set-(sk)/")
def steelTMSK():
    item_row = itemTable.itemTableData(itemList.Steel_gt_t_sk)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Steel_gt_t_sk)
    item_graph_low = itemGraph.itemGraphLow(itemList.Steel_gt_t_sk)
    item_ind_calc = itemOther.indCalc(itemList.Steel_gt_t_sk)
    item_links = itemOther.itemLinks(itemList.Steel_gt_t_sk)
    return render_template("trimmedsmsk/steelsmsk.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Black:
@app.route("/sets/black-trimmed-set-(sk)/")
def blackTMSK():
    item_row = itemTable.itemTableData(itemList.Black_gt_t_sk)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Black_gt_t_sk)
    item_graph_low = itemGraph.itemGraphLow(itemList.Black_gt_t_sk)
    item_ind_calc = itemOther.indCalc(itemList.Black_gt_t_sk)
    item_links = itemOther.itemLinks(itemList.Black_gt_t_sk)
    return render_template("trimmedsmsk/blacksmsk.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Mithril:
@app.route("/sets/mithril-trimmed-set-(sk)/")
def mithrilTMSK():
    item_row = itemTable.itemTableData(itemList.Mithril_t_sk)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Mithril_t_sk)
    item_graph_low = itemGraph.itemGraphLow(itemList.Mithril_t_sk)
    item_ind_calc = itemOther.indCalc(itemList.Mithril_t_sk)
    item_links = itemOther.itemLinks(itemList.Mithril_t_sk)
    return render_template("trimmedsmsk/mithrilsmsk.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Adamant:
@app.route("/sets/adamant-trimmed-set-(sk)/")
def adamantTMSK():
    item_row = itemTable.itemTableData(itemList.Adamant_t_sk)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Adamant_t_sk)
    item_graph_low = itemGraph.itemGraphLow(itemList.Adamant_t_sk)
    item_ind_calc = itemOther.indCalc(itemList.Adamant_t_sk)
    item_links = itemOther.itemLinks(itemList.Adamant_t_sk)
    return render_template("trimmedsmsk/adamantsmsk.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Rune:
@app.route("/sets/rune-trimmed-set-(sk)/")
def runeTMSK():
    item_row = itemTable.itemTableData(itemList.Rune_t_sk)
    item_graph_high = itemGraph.itemGraphHigh(itemList.Rune_t_sk)
    item_graph_low = itemGraph.itemGraphLow(itemList.Rune_t_sk)
    item_ind_calc = itemOther.indCalc(itemList.Rune_t_sk)
    item_links = itemOther.itemLinks(itemList.Rune_t_sk)
    return render_template("trimmedsmsk/runesmsk.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# God-blessed Dragonhide
# Guthix:
@app.route("/sets/guthix-dragonhide-set")
def guthixDHS():
    item_row = itemTable.itemTableData(itemList.guthix_dhide)
    item_graph_high = itemGraph.itemGraphHigh(itemList.guthix_dhide)
    item_graph_low = itemGraph.itemGraphLow(itemList.guthix_dhide)
    item_ind_calc = itemOther.indCalc(itemList.guthix_dhide)
    item_links = itemOther.itemLinks(itemList.guthix_dhide)
    return render_template("godblessed/guthix.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Saradomin:
@app.route("/sets/saradomin-dragonhide-set")
def saradominDHS():
    item_row = itemTable.itemTableData(itemList.saradomin_dhide)
    item_graph_high = itemGraph.itemGraphHigh(itemList.saradomin_dhide)
    item_graph_low = itemGraph.itemGraphLow(itemList.saradomin_dhide)
    item_ind_calc = itemOther.indCalc(itemList.saradomin_dhide)
    item_links = itemOther.itemLinks(itemList.saradomin_dhide)
    return render_template("godblessed/saradomin.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Zamorak:
@app.route("/sets/zamorak-dragonhide-set")
def zamorakDHS():
    item_row = itemTable.itemTableData(itemList.zamorak_dhide)
    item_graph_high = itemGraph.itemGraphHigh(itemList.zamorak_dhide)
    item_graph_low = itemGraph.itemGraphLow(itemList.zamorak_dhide)
    item_ind_calc = itemOther.indCalc(itemList.zamorak_dhide)
    item_links = itemOther.itemLinks(itemList.zamorak_dhide)
    return render_template("godblessed/zamorak.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Ancient:
@app.route("/sets/ancient-dragonhide-set")
def ancientDHS():
    item_row = itemTable.itemTableData(itemList.ancient_dhide)
    item_graph_high = itemGraph.itemGraphHigh(itemList.ancient_dhide)
    item_graph_low = itemGraph.itemGraphLow(itemList.ancient_dhide)
    item_ind_calc = itemOther.indCalc(itemList.ancient_dhide)
    item_links = itemOther.itemLinks(itemList.ancient_dhide)
    return render_template("godblessed/ancient.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Armadyl:
@app.route("/sets/armadyl-dragonhide-set")
def armadylDHS():
    item_row = itemTable.itemTableData(itemList.armadyl_dhide)
    item_graph_high = itemGraph.itemGraphHigh(itemList.armadyl_dhide)
    item_graph_low = itemGraph.itemGraphLow(itemList.armadyl_dhide)
    item_ind_calc = itemOther.indCalc(itemList.armadyl_dhide)
    item_links = itemOther.itemLinks(itemList.armadyl_dhide)
    return render_template("godblessed/armadyl.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


# Bandos:
@app.route("/sets/bandos-dragonhide-set")
def bandosDHS():
    item_row = itemTable.itemTableData(itemList.bandos_dhide)
    item_graph_high = itemGraph.itemGraphHigh(itemList.bandos_dhide)
    item_graph_low = itemGraph.itemGraphLow(itemList.bandos_dhide)
    item_ind_calc = itemOther.indCalc(itemList.bandos_dhide)
    item_links = itemOther.itemLinks(itemList.bandos_dhide)
    return render_template("godblessed/bandos.html", item_html_link = item_links, ItemRow=item_row, low_labels=item_graph_low[0],
                           low_values=item_graph_low[1], high_labels=item_graph_high[0], high_values=item_graph_high[1],
                           itemHighTotal=item_ind_calc[0], itemLowTotal=item_ind_calc[1])


if __name__ == "__main__":
    app.run(debug=True)