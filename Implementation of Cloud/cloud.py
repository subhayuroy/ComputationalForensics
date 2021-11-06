import os
import random
import hashlib
import string
import enchant  # Rainbow tables with enchant
import cloud  # importing pi-cloud

def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))

def mainroutine():
    engdict = enchant.Dict("en_US")
    fileb = open("password.txt", "a+")

    # Capture the values from the text file named password
    while True:
        randomword0 = randomword(6)
        if engdict.check(randomword0) == True:
            randomkey0 = randomword0 + str(random.randint(0, 99))
        elif engdict.check(randomword0) == False:
            englist = engdict.suggest(randomword0)
            if len(englist) > 0:
                randomkey0 = englist[0] + str(random.randint(0, 99))
            else:
                randomkey0 = randomword0 + str(random.randint(0, 99))

        randomword3 = randomword(5)
        if engdict.check(randomword3) == True:
            randomkey3 = randomword3 + str(random.randint(0, 99))
        elif engdict.check(randomword3) == False:
            englist = engdict.suggest(randomword3)
            if len(englist) > 0:
                randomkey3 = englist[0] + str(random.randint(0, 99))
            else:
                randomkey3 = randomword3 + str(random.randint(0, 99))

        if 'randomkey0' and 'randomkey3' and 'randomkey1' in locals():
            whasher0 = hashlib.new("md5")
            whasher0.update(randomkey0)
            whasher3 = hashlib.new("md5")
            whasher3.update(randomkey3)
            whasher1 = hashlib.new("md5")
            whasher1.update(randomkey1)
            print(randomkey0 + " + " + str(whasher0.hexdigest()) + "\n")
            print(randomkey3 + " + " + str(whasher3.hexdigest()) + "\n")
            print(randomkey1 + " + " + str(whasher1.hexdigest()) + "\n")
            fileb.write(randomkey0 + " + " + str(whasher0.hexdigest()) + "\n")
            fileb.write(randomkey3 + " + " + str(whasher3.hexdigest()) + "\n")
            fileb.write(randomkey1 + " + " + str(whasher1.hexdigest()) + "\n")

jid = cloud.call(randomword)  # square(3) evaluated on PiCloud
cloud.result(jid)
print('Value added to cloud')
print('Password added')
mainroutine()
