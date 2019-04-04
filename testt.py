from firebase import firebase

firebase = firebase.FirebaseApplication('https://anres-test.firebaseio.com/', None)

username = input("Username : ")
password = input("Password : ")

all_user = firebase.get('users/',None)

if username in list(all_user.keys()):
    print("have")

if all_user[username] == password:
    print("Correct")
else:
    print("error")

print(all_user)

print(list(all_user.keys()))