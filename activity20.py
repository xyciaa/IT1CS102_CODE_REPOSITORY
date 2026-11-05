from getpass import getpass

u = 'cia'
p = 'ani123'

isLogin = False

while isLogin == False:
    user = input('ENTER USERNAME --->')
    passw = getpass('ENTER PASSWORD --->')

    if user == u and passw == p :
        print('LOGIN SUCCESSFULLY!')
        isLogin = True

    else:
        print('LOGIN DENIED ')
        isLogin = False