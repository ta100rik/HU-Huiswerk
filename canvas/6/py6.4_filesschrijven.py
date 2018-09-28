# unlimited loop
while True:
    #
    userfunctioncall = int(input('\nWhat do you want to see?\n1. insert a new runner\n2. Show all runners\n Insert the number of choose\n'))
    if userfunctioncall == 1:
        runner = input('What is the runnes his/her/its name')
        import datetime
        today = datetime.datetime.today()
        currenttime = today.strftime("%a %d %b %Y, %H:%M:%S")
        file = open("Runnerlijst.txt", "a")
        template = '{}, {}\n'
        file.write(template.format(currenttime,runner))
        file.close()
    elif userfunctioncall == 2:
        file = open('Runnerlijst.txt', 'r')
        for line in file:
            template = '{}'
            print(template.format(line.rstrip()))
        file.close()
    else:
        print('That is not a option')