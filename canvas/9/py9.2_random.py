import random
def monopolyworp():
    counter = 0
    while True:
        random1 = random.randint(1, 6)
        random2 = random.randint(1, 6)
        template = '{} + {} = {}'
        total = random1 + random2
        if random1 == random2:
            if counter == 3:
                print(template.format(str(random1),str(random2),str(total) + ' (direct naar de gevangenis)'))
                break
            else:
                print(template.format(str(random1),str(random2),str(total) + ' (dubbel)'))
                counter += 1
        else:
            print(template.format(str(random1),str(random2),str(total)))
            break

monopolyworp()