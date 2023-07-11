fs_pairs = {'bob': 'bobby',
            'apple': 'tree',
            'dog': 'wolf'}
choice = None
def choices():
    print('''

           Your choices right now:

           1: Exit
           2: Add son father pair
           3: Replace a son's father with another 
           4: Delete son father pair
           5: View son father pairs

           ''')
while choice != '1':
    choices()
    choice = input('What is your choice? : ')

    while choice != '1' or '2' or '3' or '4' or '5':
        print('\nTry Again')
        choices()
        choice = input('What is your choice? : ')

        if choice == '1':
            print('Bye')
        elif choice == '2':
            print('Your choice was add son father pair')
            son_add = input('What would the son\'s name be? : ')
            father_add = input('What would ' + son_add + ' \'s father\'s name be? : ')
            fs_pairs.update({son_add: father_add})
            print('You added ' + father_add + ' to be the father of ' + son_add)
        elif choice == '3':
            print('Your choice was to replace a son\'s father with another')
            print(fs_pairs)
            son = input('Which son\'s father would you like to replace? : ')
            if son in fs_pairs:
                replace = input('What do you want the new father\'s name to be? : ')
                fs_pairs[son] = replace
        elif choice == '4':
            should_see_pairs_before_deletion = input('Would you like to see the son father pairs before you delete a pair? (y/n) :')
            if should_see_pairs_before_deletion == 'y':
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


