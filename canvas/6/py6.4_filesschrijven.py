# unlimited loop
import datetime
while True:
    #
    userfunctioncall = int(input('\nWhat do you want to see?\n1. insert a new runner\n2. Show all runners\n Insert the number of choose\n'))#asking the user for the function
    # looking if the user has the right number else it will print that it is not
    if userfunctioncall == 1:
        # asking the name of the users
        runner = input('What is the runnes his/her/its name: ')
        #grabbing the current date full like all the paramaters
        today = datetime.datetime.today()
        # formatting the time to a nice format
        currenttime = today.strftime("%a %d %b %Y, %H:%M:%S")
        # opening the file with append permissions
        file = open("Runnerlijst.txt", "a")
        # making template
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