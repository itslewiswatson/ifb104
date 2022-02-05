def yeet():
    names = ['a', 'a', 'a']

    if (names[0] > names[1]):
        print('1')
        names[0], names[1] = names[1], names[0]
    if (names[1] > names[2]):
        print('2')
        names[1], names[2] = names[2], names[1]
    if (names[0] > names[1]):
        print('3')
        names[0], names[1] = names[1], names[0]

    print(names)

yeet()