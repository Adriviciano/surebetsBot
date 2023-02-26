from searchForProfit import getProfit as profit
def comparator():
    '''l=web1.size()
    if(web2.size()>l):
        l=web2.size()

    for i in range(l):
        profit()'''
    sportium_str = "1:2.50/X:3.00/2:3.50"
    juegging_str = "1:4/X:3.00/2:2.95"
    sportium_do_str = "1X:12/12:1.45/X2:15"
    juegging_do_str = "1X:1.45/12:1.40/X2:1.70"

    resultado = profit(sportium_str, juegging_str, sportium_do_str, juegging_do_str)
    print(resultado)

comparator()
