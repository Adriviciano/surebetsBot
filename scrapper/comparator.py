from searchForProfit import searchForProfit as profit
def comparator(web1, web2):
    l=web1.size()
    if(web2.size()>l):
        l=web2.size()

    for i in range(l):
        profit()