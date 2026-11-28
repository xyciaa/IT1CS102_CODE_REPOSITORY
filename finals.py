#menu
print(' ============================================== ')
name = input(' enter name --> ')

while True: 
    ans = input(' Hello, are you ready to learn python? (yes/no) - ' )

    if ans == 'yes':
        print(' Which python code do you want to learn ? ') 
        print(' 1- print \n 2- data types \n 3- escape sequence \n 4- operations \n 5- assignments ')
        choice = int(input(' Enter the number of the python code that you want to learn: '))
    
        if choice == 1:
            print(' ============================================== ')
            print(' print is use to show an output. For example, if you want to say "hi" or "hello" \n you can type: print("hello") and the outcome will be: \n hello')
            print(' Now you try it! ')
            pri = input('>>> ').strip()

            # Check if they typed print("...") or print('...')
            if (pri.startswith('print("') and pri.endswith('")')) or (pri.startswith("print('") and pri.endswith("')")):
                # Extract the text inside the quotes and print it
                user_text = pri[7:-2]
                print(' Output:')
                print('\t', user_text)
                print(' Great job! ')
            else:
                print('Oops! Make sure to type print("your message") with parentheses and make sure to use the same quotes.')
    else:
        break 