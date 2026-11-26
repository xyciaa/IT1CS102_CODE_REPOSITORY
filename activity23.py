shonen = [ ]
korean = [ ]
isekai = [ ]
adventure = [ ]
fantasy = [ ]

while True:
    sagot = input(' Do you watch or read anime? yes/no ').lower()
 
    if sagot == 'yes':
        print(' What kind of anime do you watch/read ?  ')
        print('\n 1- shonen \n 2- korean \n 3- isekai \n 4- adventure \n 5- fantasy')

        choice = int(input(' Enter genre ---> '))

        if choice == 1:
            print (' Genre: Shonen')
            title = input(' \n Please input the title of the anime---> ')
            shonen.append(title)
            print(' List of Shonen: ')
            print(shonen)
            con = input(' Do you wish to continue? yes/no ').lower()
            if con == 'yes':
                continue

            rem = input('Do you want to remove something? yes/no ').lower()
            if rem == 'yes':
                title = input(' Enter the anime that you want to remove: ')
                shonen.remove(title)
                print(shonen)
            else:
                break

        elif choice == 2:
                print (' Genre: Korean')
                title = input('\n Please input the title of the anime---> ')
                korean.append(title)
                print(' List of Korean: ')
                print(korean)
                con = input(' Do you wish to continue? yes/no ').lower()
                if con == 'yes':
                    continue
    
        else:
            print('INVALID choice')
    else:
        break
        



