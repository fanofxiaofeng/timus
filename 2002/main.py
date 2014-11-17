# python 2.7.3
import sys
import math

n = input()

password = {}
userInSys = set()

for i in range(n):
    line = sys.stdin.readline()
    words = line.split()
    user = words[1]
    if words[0] == 'register':        
        passwd = words[2]
        if user in password:
            print 'fail: user already exists'
        else:
            password[user] = passwd
            print 'success: new user added'        
    elif words[0] == 'login':
        passwd = words[2]
        if user not in password:
            print 'fail: no such user'
        elif password[user] != passwd:
            print 'fail: incorrect password'
        elif user in userInSys:
            print 'fail: already logged in'
        else:
            userInSys.add(user)
            print 'success: user logged in'        
    elif words[0] == 'logout':
        if user not in password:
            print 'fail: no such user'
        elif user not in userInSys:
            print 'fail: already logged out'
        else:
            print 'success: user logged out'
            userInSys.remove(user)
    else:
        raise ValueError
    
