import urllib.request
from urllib.request import urlopen
import re

def go():
    x = input("\n\nEnter a name to look up: ")
    words = urlopen("http://hiscore.runescape.com/index_lite.ws?player="+ x + "").read().decode("utf-8")

    newlist = re.split(r',*\n*', words)
    numberedlist = {}
    count = 0

    for i in newlist:
        numberedlist.__setitem__(count, i)
        count += 1

    


    globalrank = numberedlist[0]
    totallevel = numberedlist[1]
    totalxp = numberedlist[2]
    attrank = numberedlist[3]
    attlevel = numberedlist[4]
    attxp = numberedlist[5]
    defrank = numberedlist[6]
    deflevel = numberedlist[7]
    defxp = numberedlist[8]
    strrank = numberedlist[9]
    strlevel = numberedlist[10]
    strxp = numberedlist[11]
    conrank = numberedlist[12]
    conlevel = numberedlist[13]
    conxp = numberedlist[14]
    rngrank = numberedlist[15]
    rnglevel = numberedlist[16]
    rngxp = numberedlist[17]
    pryrank = numberedlist[18]
    prylevel = numberedlist[19]
    pryxp = numberedlist[20]
    print("\n\n" +x+ " is ranked "+ globalrank + " in the world.")
    print("\n" + x + "'s total level is " + totallevel + ".")
    print("\n" + x + " has a total of " + totalxp + " experience.")
    print("\n" + x + "'s attack level is " + attlevel + ".")
    print("\n" + x + "'s strength level is " + strlevel + ".")
    print("\n" + x + "'s defence level is " + deflevel + ".")
    print("\n" + "att xp: " + attxp + "  def xp: " + defxp + "  str xp: " + strxp + "  constitution xp: " + conxp + "  range xp: " + rngxp + "  prayer xp: " + pryxp)
    
    
    go()

go()
