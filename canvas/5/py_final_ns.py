    '''
    Welcome to the NS distance price counter
    
    The distance 12.5 will return a price of 10 euro without discount
    The functions are all made that you can return more than 1 value for ech function 
    At the moment I only use 1 because the current assignment said so.
    '''

    def standaardtarief(afstandkm):
        # default value is 0.80 cent and starting budget 0
        cos_each_km = 0.80
        result = 0
        # if the distance is greater than 50 there is a starting budget of 15 + 50 km of default value and every
        #  km bigger than 50 will get 0.60
        if afstandkm > 50:
            result = 15.00
            result = (50 * cos_each_km) + result
            # result has the 15 starting budget with 50 km of the default value
            afstandkm = afstandkm - 50
            # we need to substract the 50 km because we already calculated this above
            cos_each_km = 0.60
            # the new price for each km
        elif afstandkm < 0: # if distance is below 0 than we need to set the km to 0
            afstandkm = 0
        #result will be calculated for each left km with the current distancecount and the
        #old result value will also be added to the result
        result = (afstandkm * cos_each_km) + result
        #returning the result to the user
        return result
    def ritprijs(leeftijd,weekendrit,afstand):
        #getting the default price of the trip
        tarief = standaardtarief(afstand)
        #looking how much discount they get depending on age and weakend trip
        if leeftijd < 12 or leeftijd >= 65:
            #default vars
            korting = 30
            #expection vars
            if weekendrit:
                korting = 35
        else:
            #default vars
            korting = 0
            #expecting vars
            if weekendrit:
                korting = 40
        #the default price will be calculated to the price with discount sometimes
        result = (tarief / 100) * (100 - korting)
        #every used var can be returned here in a list or a tulpe or just single value.
        return result

    leeftijd        = int(input('Geef je leeftijd op: '))
    workday_bol     = input('Is het weekend? (Y/N): ')
    afstand         = float(input('Hoeveel km heb je gereisd: '))
    workday_bol     = True if workday_bol == 'Y' else False

    print('Je betaalt voor deze rit ' + str(ritprijs(leeftijd,workday_bol,afstand)))


