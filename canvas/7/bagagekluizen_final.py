    '''
    Welcome to the Locker safe,
    
    This locker safe is not hashed because the assignment didn't told me to
    Salt is already placed but not fully because als the assignment was not right
    '''
    # welcome message
    print('Welcome,\n To the luggage lock system\n')

    def lockfree():
        # opening the file
        File = open('lockers.txt')
        # counting var for looking the lines
        countline = 0
        # looping through the line and counting them
        for line in File:
            # increase after every line
            countline += 1
        # looking if the lines are above 12 or on 12 then there are no lockers
        if countline >= 12:
            # printing the status and filling res
            print('No lockers are available')
            res = False
        else:
            # printing the status and filling res
            template = 'There are {} locker availa1ble'
            print(template.format(12 - countline))
            res = True
        # Don't want dirty code so closing the file
        File.close()
        # returning the result
        return res
    def newlock():
        # opening the file
        File = open('lockers.txt')
        # looking if the save is possible and giving feedback to the user
        Freebol = lockfree()
        # if there are vailable we run want to write
        if Freebol:
            # first lets look what is taken and put it in a list
            takenlockers = []
            # looking each line wich locker number it has
            for line in File:
                # splitting the line number with accesscode remember \n is there and the accesscode can't contain ; or \n
                line = line.split(';')
                # appending the number to the list
                takenlockers.append(int(line[0]))
            # Close the file
            File.close()
            locksalt = True
            while locksalt:
                # asking the code for the new locker
                userpass = input('Wat lock code do you want to use? ')
                    # checking if the user used ; in his pass
                    if ';' not in userpass and '\n' not in userpass:
                        locksalt = False
                    # show the user that he used the wrong salt
                    else:
                        print('Sorry but the chars ; and \n are not ailable ')
            # making variable for looking locker
            bollock = True
            # looping throught every possible locker and
            while bollock:
                # looping every possible lock
                for lockernumber in range(1,12,1):
                    # grabbing first number of not taken locker
                    if lockernumber not in takenlockers:
                        # opening the file again but now with append permission
                        File = open("lockers.txt", "a")
                        # template for writing the file
                        filewritetemplate = '{};{}'
                        # writing it in the file
                        File.write(filewritetemplate.format(str(lockernumber),str(userpass)))
                        # Showing the user his lock number
                        print('You claimed locker {}.'.format(lockernumber))
                        # Stopping the while loop
                        bollock = False
                        #Closing the file
                        File.close()
                        # stoping the for loop
                        break
    def openlock(lockernumber,lockercode):
        # opening the lockers file
        File = open('lockers.txt')
        # just a bol var to return backend to use the function for more than 1 thing
        accesgranted = False
        # looping throught the file lines
        for line in File:
            # splitting every line for locknumber and lockcode4
            line = line.split(';')
            # putting the number and code in 2 vars and removing the breakline(\n)
            locknumber = int(line[0])
            lockcode = line[1].rstrip()
            # looking if the users input is correct with the code and locker
            if lockernumber == lockernumber and lockcode == lockercode:
                # printing access
                print('You have access to your locker')
                # change bol for return later on
                accesgranted = True
        # giving the user feedback that his code and number is not a match
        if not accesgranted:
            print('That code or locker isn\'t correct')
        # close my file just to make it not dirty
        File.close()
        # returning if the access was granted or not
        return accesgranted

    def deletelocker(lockernumber,lockercode):
        # looking if the user can access the locker
        useraccess = openlock(lockernumber,lockercode)
        # if the user has access the python will have true and remove the line
        if useraccess:
            # because there is no remove in python we need to make the file in a list
            # and than rewrite it to the same file with the new values
            # opening the file with read permissions
            file = open('lockers.txt', 'r')
            # Formatting and grabbing the line that will be deleted
            rmstring = '{};{}\n'.format(str(lockernumber),str(lockercode))
            # making a list to copy the new file in with out the current line
            list = []
            # looping throught the lines
            for line in file:
                # look if the line is a match and than replacing the line with a empty string
                if rmstring in line:
                    line = line.replace(rmstring, '')
                # appending the empty line or just the basic value to the list
                list.append(line)
            # closing the read permission and file
            file.close()
            # opening the file again
            file = open('lockers.txt', 'w')
            #looping throught every line and overwriting the current value
            for line in list:
                # writing the new line it will match or just only overwrite current with ''
                file.write(line)
            #closing the current file
            file.close()
            print('Your Locker is free for the next person to take')
    while runbol:

        # default bolean to stop the code and exit python
        runbol = True
        print('Your option\'s are: \n')
        print('{}\n{}\n{}\n{}\n{}\n'.format('1. how many locks are free','2. I want a new lock','3. I want to unlock my locker','4. I want do give up my locker','5. Stop this script'))
        Option = int(input('Choose what you want to do: '))
        # elif because python doesn't have a switch statement
        if Option == 1:
            lockfree()
        elif Option == 2:
            newlock()
        elif Option == 3:
            lockernumber = int(input('Give me your locker number? '))
            lockercode = input('Give me your locker code?')
            openlock(lockernumber,lockercode)
        elif Option == 4:
            lockernumber = int(input('Give me your locker number? '))
            lockercode = input('Give me your locker code?')
            deletelocker(lockernumber,lockercode)
        elif Option == 5:
            # turning it in to false to stop the script
            runbol = False
        else:
            # print parameter says what it does
            print('That is not a option')


