def namen():
    # global vars
    studentlist = {}
    counter = 0
    # looping until the user give's use no string
    while True:
        givename = input('Name plz: ')
        # no string run results
        if givename == '':
            for name,count in studentlist.items():
                if count > 1:
                    template =  'Er is {} student met de naam {}'
                else:
                    template =  'Er zijn {} student met de naam {}'
                print(template.format(str(count),name))
            break

        else:
            if counter == 0:
                studentlist[givename] = 1
                counter += 1
            else:
                newone = True
                for name,count in studentlist.items():
                    if name == givename:
                        studentlist[givename] += 1
                        newone = False
                if newone:
                    studentlist[givename] = 1


namen()