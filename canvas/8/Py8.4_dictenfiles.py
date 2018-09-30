def ticker(filename):
    File = open(filename)
    ticker = {}
    for line in File:
        line = line.split(':')
        totalname = line[0]
        shortname = line[1].rstrip()
        ticker[shortname] = totalname
    return ticker

def searchticker(searchvalue,filename):
    tickersdic = ticker(filename)
    res = 'You search is not found'
    for shortname, name in tickersdic.items():
        if searchvalue == name:
            res = shortname
        elif searchvalue == shortname:
            res = name
    return res
uservalue = input('Give us your ticker or Companynae')
print(searchticker(uservalue,'tickers.txt'))
