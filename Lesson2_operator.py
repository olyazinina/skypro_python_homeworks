#user_login = "olga"
#user_password = "xxx123"

#login = input("Login: ")
#password = input("Password: ")

#if (login == user_login) and (password == user_password):
#    print("Secret is open")
#else:
#    print("Locked")

crit1 = "red"
crit2 = "lock"

color = input("Color: ")
feature = input("Feature: ")

if(color == crit1) or (feature == crit2):
    print("Buy it!")
else:
    print("Похожу, ещё посмотрю")