import sys
import hashlib
import getpass


def main(argv):
    print('\nUser & Password Storage Program in Linux for forensic detection v.01\n')

    if input('The file ' + sys.argv[1] + ' will be erased or overwrite if it exists .\nDo you wish to continue (Y/n): ') not in ('Y','y') :
        sys.exit('\nChanges were not recorded\n')

    user_name = input('Please Enter a User Name: ')
    password = hashlib.sha224(getpass.getpass('Please Enter a Password:')).hexdigest()

    # Passwords which are hashed
    try:
        file_conn = open(sys.argv[1], 'w')
        file_conn.write(user_name + '\n')
        file_conn.write(password + '\n')
        file_conn.close()
    except:
        sys.exit('There was a problem writing the passwords to file!')


if __name__ == "__main__":
    main(sys.argv[1:])