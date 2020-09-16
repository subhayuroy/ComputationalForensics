import uuid, hashlib


def hash_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_psswd, user_psswd):
    password, salt = hashed_psswd.split(':')
    return password == hashlib.sha256(salt.encode() + user_psswd.encode()).hexdigest()


new_pass = input("Enter required password= ")
hashed_psswd = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_psswd)
old_pass = input("Re-enter new password= ")

if check_password(hashed_psswd, old_pass):
    print("You entered the correct password")
else:
    print("The passwords don't match")