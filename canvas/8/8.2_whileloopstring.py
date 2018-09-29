while True:
    word = input('Geef een string van vier letters: ')
    if len(word) == 4:
        print('Good job het woord {} is 4 lang'.format(word))
        break
    else:
        print('{} heeft {} letters'.format(word,len(word)))