fs_pairs = {'bob': 'bobby',
            'apple': 'tree',
            'dog': 'wolf'}
choice = None

while choice != '1':
    print('''

    Your choices right now:

    1: Exit
    2: add son father pair
    3: replace a son's father with another 
    4: delete son father pair
    5: view son father pairs

    ''')
    choice = input('What is your choice? : ')
    if choice == '1':
        print('Bye')
    elif choice == '2':
        print('Your choice was add son father pair')
        add = input('What would the son\'s name be? : ')
        add2 = input('What would ' + add + ' \'s father\'s name be? : ')
        fs_pairs.update({add: add2})
        print('You added ' + add2 + ' to be the father of ' + add)
    elif choice == '3':
        print('Your choice was to replace a son\'s father with another')
        print(fs_pairs)
        index = input('Which son\'s father would you like to replace? : ')
        if index in fs_pairs:
            replace = input('What do you want the new father\'s name to be? : ')
            fs_pairs[index] = replace
    elif choice == '4':
        pair = input('Would you like to see the son father pairs before you delete a pair? (y/n) :')
        if pair == 'y':
            for key in fs_pairs:
                print(key + '\'s father is ')
                print(fs_pairs.get(key), '\n')
            d_del = input('Which son father pair would you like to get rid of  : ')
            if d_del in fs_pairs:
                del fs_pairs[d_del]
                print('You deleted ' + d_del + '')
        else:
            d_del = input('Which son father pair would you like to get rid of  : ')
            if d_del in fs_pairs:
                del fs_pairs[d_del]
                print('You deleted ' + d_del + '')
    elif choice == '5':
        if fs_pairs:
            for key in fs_pairs:
                print('Who\'s your father' + key + '?')
                print(fs_pairs.get(key) + '\n')
        else:
            print('You don\'t have any pairs')

 x
