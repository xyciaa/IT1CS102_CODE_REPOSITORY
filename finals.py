#menu
print(' ============================================== ')
#name = input(' enter name --> ')

#colors
PINK = '\033[38;2;219;68;118m' 
RED = '\033[38;2;220;76;76m'
BLUE = '\033[38;2;52;120;214m'
PURPLE = '\033[38;2;142;84;200m' 
RESET = '\033[0m'

while True: 
    ans = input(' Hello, are you ready to learn python? (yes/no) - ' )

    if ans == 'yes':
        print(' Which python code do you want to learn ? ') 
        print(' 1- print \n 2- data types \n 3- escape sequence \n 4- operations \n 5- assignments ')
        choice = int(input(' Enter the number of the python code that you want to learn: '))
    
        if choice == 1:
            print(' ============================================== ')
            print(f'• {PINK} print {RESET} is a built-in command (or function) that displays text, numbers, or other information on the screen so the user or programmer can see it. For example, if you want to say "hi" or "hello" you can type: print("hello") or (\'hello\') and the outcome will be: \n {PINK}hello{RESET}')
            print('• When using print we have to remember these steps: \n - First is make sure to type "print" in small letters. \n - Second is make sure to use open and close parentheses and not bracket. \n - Lastly is make sure to use the same qoutes, either \'\' or \"\"  ')
            
            while True: #user will now try 
                print(' ---------------------------------------------- ')
                print(' | Now you try it!                            | ')
                pri = input(' | >>> ').strip()
                print(' ---------------------------------------------- ')
                 
                if (pri.startswith('print("') and pri.endswith('")')) or (pri.startswith("print('") and pri.endswith("')")):
                    user_text = pri[7:-2]
                    print(' Output:')
                    print(f'\t {PINK}{user_text}{RESET}')
                    print(' You did it! Great job! ')
                    break  
                else:
                    print(f'{RED}Oops! Make sure to type print("your message") with parentheses and make sure to use the same quotes. Try again!{RESET}')

            con = input(' Do you wish to continue? yes/no - ').lower()
            if con == 'yes':
                continue
            else:
                break
    else:
        break
