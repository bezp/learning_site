
#test py page for udemy course on OOP
from random import randint

pplDict = {111: {'name': 'a', 'balance': 22}}

# print(pplDict[111]['name'])
while True:
    reply = input('Would you like to create or access an account?')

    if reply == 'create':
        name = input('name: ')
        while True:
            try:
                deposit = int(input('deposit amount: '))
                break
            except ValueError:
                print('insert number values')


        accountNumber = randint(100,999)
        print ('your account number is {}'.format(accountNumber))
        pplDict[accountNumber] = {'name': name, 'balance': deposit}

    if reply == 'access':
        while True:
            leave = input('quit? Y/N? ')
            if leave == 'y':
                break
            name = input('name: ')

            while True:
                try:
                    accountNumber = int(input('whats ur acc number?' ))
                    break
                except ValueError:
                    print('insert number values')
            # print(name)
            # print(pplDict[111]['name'])
            try:
                if pplDict[accountNumber]['name'] == name:
                    accessReply = input('would you like to WITHDRAW, DEPOSIT, or SHOW balance? QUIT ')

                    if accessReply == 'withdraw':
                        pass
                    if accessReply == 'deposit':
                        pass
                    if accessReply == 'show':
                        print(pplDict[accountNumber]['balance'])
                    if accessReply == 'quit':
                        break
            except KeyError:
                print ('doesnt match')


    if reply == 'quit':
        break

print (pplDict)




