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


# Get data for web page:
def createPage(myItem = [], *args):
    item_row = itemTable.itemTableData(myItem)
    item_graph_high = itemGraph.itemGraphHigh(myItem)
    item_graph_low = itemGraph.itemGraphLow(myItem)
    item_ind_calc = itemOther.indCalc(myItem)
    item_links = itemOther.itemLinks(myItem)
    all_info = [item_row, item_graph_high, item_graph_low, item_ind_calc, item_links]
    return all_info


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


# Barrows:
# Ahrim
@app.route("/sets/ahrim-s-armour-set/")
def ahrim():
    page = createPage(itemList.Ahrim)
    return render_template("barrows/ahrim.html", item_html_link = page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Dharok
@app.route("/sets/dharok-s-armour-set/")
def dharok():
    page = createPage(itemList.Dharok)
    return render_template("barrows/dharok.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Guthan
@app.route("/sets/guthan-s-armour-set/")
def guthan():
    page = createPage(itemList.Guthan)
    return render_template("barrows/guthan.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Karil
@app.route("/sets/karil-s-armour-set/")
def karil():
    page = createPage(itemList.Karil)
    return render_template("barrows/karil.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Torag
@app.route("/sets/torag-s-armour-set/")
def torag():
    page = createPage(itemList.Torag)
    return render_template("barrows/torag.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Verac
@app.route("/sets/verac-s-armour-set/")
def verac():
    page = createPage(itemList.Verac)
    return render_template("barrows/verac.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Gold-Trimmed Standard Metal (lg)
# Bronze:
@app.route("/sets/bronze-gold-trimmed-set-(lg)/")
def bronzeGTSMLG():
    page = createPage(itemList.Bronze_gt_lg)
    return render_template("goldtrimmedsmlg/bronzegtslg.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Iron:
@app.route("/sets/iron-gold-trimmed-set-(lg)/")
def ironGTSMLG():
    page = createPage(itemList.Iron_gt_lg)
    return render_template("goldtrimmedsmlg/irongtslg.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Steel:
@app.route("/sets/steel-gold-trimmed-set-(lg)/")
def steelGTSMLG():
    page = createPage(itemList.Steel_gt_lg)
    return render_template("goldtrimmedsmlg/steelgtslg.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Black:
@app.route("/sets/black-gold-trimmed-set-(lg)/")
def blackGTSMLG():
    page = createPage(itemList.Black_gt_lg)
    return render_template("goldtrimmedsmlg/blackgtslg.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Mithril:
@app.route("/sets/mithril-gold-trimmed-set-(lg)/")
def mithrilGTSMLG():
    page = createPage(itemList.Mithril_gt_lg)
    return render_template("goldtrimmedsmlg/mithrilgtslg.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Adamant:
@app.route("/sets/adamant-gold-trimmed-set-(lg)/")
def adamantGTSMLG():
    page = createPage(itemList.Adamant_gt_lg)
    return render_template("goldtrimmedsmlg/adamantgtslg.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Rune:
@app.route("/sets/rune-gold-trimmed-set-(lg)/")
def runeGTSMLG():
    page = createPage(itemList.Rune_gt_lg)
    return render_template("goldtrimmedsmlg/runegtslg.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Gilded:
@app.route("/sets/gilded-armour-set-(lg)/")
def gildedGTSMLG():
    page = createPage(itemList.Gilded_gt_lg)
    return render_template("goldtrimmedsmlg/gildedslg.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Gold-Trimmed Standard Metal (sk)
# Bronze:
@app.route("/sets/bronze-gold-trimmed-set-(sk)/")
def bronzeGTSMSK():
    page = createPage(itemList.Bronze_gt_sk)
    return render_template("goldtrimmedsmsk/bronzegtssk.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Iron:
@app.route("/sets/iron-gold-trimmed-set-(sk)/")
def ironGTSMSK():
    page = createPage(itemList.Iron_gt_sk)
    return render_template("goldtrimmedsmsk/bronzegtssk.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Steel:
@app.route("/sets/steel-gold-trimmed-set-(sk)/")
def steelGTSMSK():
    page = createPage(itemList.Steel_gt_sk)
    return render_template("goldtrimmedsmsk/steelgtssk.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Black:
@app.route("/sets/black-gold-trimmed-set-(sk)/")
def blackGTSMSK():
    page = createPage(itemList.Black_gt_sk)
    return render_template("goldtrimmedsmsk/blackgtssk.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Mithril:
@app.route("/sets/mithril-gold-trimmed-set-(sk)/")
def mithrilGTSMSK():
    page = createPage(itemList.Mithril_gt_sk)
    return render_template("goldtrimmedsmsk/mithrilgtssk.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# adamant:
@app.route("/sets/adamant-gold-trimmed-set-(sk)/")
def adamantGTSMSK():
    page = createPage(itemList.Adamant_gt_sk)
    return render_template("goldtrimmedsmsk/adamantgtssk.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Rune:
@app.route("/sets/rune-gold-trimmed-set-(sk)/")
def runeGTSMSK():
    page = createPage(itemList.Rune_gt_sk)
    return render_template("goldtrimmedsmsk/runegtssk.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Gilded:
@app.route("/sets/gilded-armour-set-(sk)/")
def gildedGTSMSK():
    page = createPage(itemList.Gilded_gt_sk)
    return render_template("goldtrimmedsmsk/gildedssk.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Trimmed Standard Metal (lg)
# Bronze:
@app.route("/sets/bronze-trimmed-set-(lg)/")
def bronzeTMLG():
    page = createPage(itemList.Bronze_t_lg)
    return render_template("trimmedsmlg/bronzesmlg.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Iron:
@app.route("/sets/iron-trimmed-set-(lg)/")
def ironTMLG():
    page = createPage(itemList.Iron_t_lg)
    return render_template("trimmedsmlg/ironsmlg.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Steel:
@app.route("/sets/steel-trimmed-set-(lg)/")
def steelTMLG():
    page = createPage(itemList.Steel_gt_t_lg)
    return render_template("trimmedsmlg/steelsmlg.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Black:
@app.route("/sets/black-trimmed-set-(lg)/")
def blackTMLG():
    page = createPage(itemList.Black_gt_t_lg)
    return render_template("trimmedsmlg/blacksmlg.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Mithril:
@app.route("/sets/mithril-trimmed-set-(lg)/")
def mithrilTMLG():
    page = createPage(itemList.Mithril_t_lg)
    return render_template("trimmedsmlg/mithrilsmlg.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Adamant:
@app.route("/sets/adamant-trimmed-set-(lg)/")
def adamantTMLG():
    page = createPage(itemList.Adamant_t_lg)
    return render_template("trimmedsmlg/adamantsmlg.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Rune:
@app.route("/sets/rune-trimmed-set-(lg)/")
def runeTMLG():
    page = createPage(itemList.Rune_t_lg)
    return render_template("trimmedsmlg/runesmlg.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Trimmed Standard Metal (sk)
# Bronze:
@app.route("/sets/bronze-trimmed-set-(sk)/")
def bronzeTMSK():
    page = createPage(itemList.Bronze_t_sk)
    return render_template("trimmedsmsk/bronzesmsk.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Iron:
@app.route("/sets/iron-trimmed-set-(sk)/")
def ironTMSK():
    page = createPage(itemList.Iron_t_sk)
    return render_template("trimmedsmsk/ironsmsk.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Steel:
@app.route("/sets/steel-trimmed-set-(sk)/")
def steelTMSK():
    page = createPage(itemList.Steel_gt_t_sk)
    return render_template("trimmedsmsk/steelsmsk.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Black:
@app.route("/sets/black-trimmed-set-(sk)/")
def blackTMSK():
    page = createPage(itemList.Black_gt_t_sk)
    return render_template("trimmedsmsk/blacksmsk.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Mithril:
@app.route("/sets/mithril-trimmed-set-(sk)/")
def mithrilTMSK():
    page = createPage(itemList.Mithril_t_sk)
    return render_template("trimmedsmsk/mithrilsmsk.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Adamant:
@app.route("/sets/adamant-trimmed-set-(sk)/")
def adamantTMSK():
    page = createPage(itemList.Adamant_t_sk)
    return render_template("trimmedsmsk/adamantsmsk.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Rune:
@app.route("/sets/rune-trimmed-set-(sk)/")
def runeTMSK():
    page = createPage(itemList.Rune_t_sk)
    return render_template("trimmedsmsk/runesmsk.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# God-blessed Dragonhide
# Guthix:
@app.route("/sets/guthix-dragonhide-set")
def guthixDHS():
    page = createPage(itemList.guthix_dhide)
    return render_template("godblessed/guthix.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Saradomin:
@app.route("/sets/saradomin-dragonhide-set")
def saradominDHS():
    page = createPage(itemList.saradomin_dhide)
    return render_template("godblessed/saradomin.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Zamorak:
@app.route("/sets/zamorak-dragonhide-set")
def zamorakDHS():
    page = createPage(itemList.zamorak_dhide)
    return render_template("godblessed/zamorak.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Ancient:
@app.route("/sets/ancient-dragonhide-set")
def ancientDHS():
    page = createPage(itemList.ancient_dhide)
    return render_template("godblessed/ancient.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Armadyl:
@app.route("/sets/armadyl-dragonhide-set")
def armadylDHS():
    page = createPage(itemList.armadyl_dhide)
    return render_template("godblessed/armadyl.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


# Bandos:
@app.route("/sets/bandos-dragonhide-set")
def bandosDHS():
    page = createPage(itemList.bandos_dhide)
    return render_template("godblessed/bandos.html", item_html_link=page[4], ItemRow=page[0], low_labels=page[2][0],
                           low_values=page[2][1], high_labels=page[1][0], high_values=page[1][1],
                           itemHighTotal=page[3][0], itemLowTotal=page[3][1])


if __name__ == "__main__":
    app.run(debug=True)