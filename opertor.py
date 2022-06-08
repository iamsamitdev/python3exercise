print("Please enter user/password")

username = input('Username: ')
password = input('Password: ')

# ตรวจเงื่อนไขด้วย if...else
if(username == "admin" and password == "1234"):
    print('Login Success')
else:
    print('Login Fail!')
