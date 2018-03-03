# from abc import ABCMeta, abstractmethod
# from random import randint
#
# class Account(metaclass = ABCMeta):
#     @abstractmethod
#     def createAccount():
#         return 0
#     @abstractmethod
#     def authenticate():
#         return 0
#     @abstractmethod
#     def withdraw():
#         return 0
#     @abstractmethod
#     def depositx():
#         return 0
#     @abstractmethod
#     def show():
#         return 0
#
# class SavingsAccount(Account):
#     def __init__(self):
#         self.accounts = {}
#     def info(self):
#         print(self.accounts)
#     def createAccount(self, name, deposit):
#         self.name = name
#         self.deposit = int(deposit)
#         self.accountNumber = randint(100,999)
#         self.accounts[self.accountNumber] = {'name': self.name, 'balance': self.deposit}
#         print('Account Number = {}'.format(self.accountNumber))
#         print('made by {} with {}'.format(self.name, self.deposit))
#     def authenticate(self, name, accountNumber):
#         if accountNumber in self.accounts:
#
#             if self.accounts[accountNumber]['name'] == name:
#                 self.accountNumber = accountNumber # make the given acc# the instance attr for the rest of process
#                 print('made by {} authentic'.format(self.accounts[self.accountNumber]['name'])) #or can just use 'name'
#                 return True
#             else:
#                 print('made by {} FAILED'.format(self.accounts[self.accountNumber]['name']))
#                 print('authentication failed')
#                 return False
#         else:
#             print('made by {} FAILEDXXX'.format(self.accounts[self.accountNumber]['name']))
#             print('authentication failed')
#             return False
#
#     def withdraw(self, amount):
#         if amount > self.accounts[self.accountNumber]['balance']:
#             print('too much {}'.format(self.accounts[self.accountNumber]['name']))
#         else:
#             self.accounts[self.accountNumber]['balance'] -= int(amount)
#         self.show()
#
#     def depositx(self, amount):
#         self.accounts[self.accountNumber]['balance'] += int(amount)
#         self.show()
#
#     def show(self):
#         print('you {} dis much left {}'.format(self.accounts[self.accountNumber]['name'], self.accounts[self.accountNumber]['balance']))
#
# aaa = SavingsAccount()
#
#
# # aaa.createAccount('niim', 1000)
# # aaa.withdraw(50)
# # aaa.depositx(10)
# # print(aaa.accounts)
# while True:
#     try:
#         reply = int(input('1 - create, 2 - access, 3 - quit or 4-info'))
#         if reply == 1:
#             name = input('What is your name: ')
#             deposit = input ('How much to deposit: ')
#             aaa.createAccount(name, deposit)
#         elif reply == 2:
#             name = input('What is your name: ')
#             accNumber = int(input('What is your accNumber: '))
#             if aaa.authenticate(name, accNumber):
#                 while True:
#                     reply = int(input('1 - withdraw, 2 - deposit, 3 - show, 4 - quit'))
#                     if reply is 1:
#                         try:
#                             x = int(input('how much to withdraw'))
#                             aaa.withdraw(x)
#                         except ValueError:
#                             print ('v error ')
#                     elif reply is 2:
#                         try:
#                             x = int(input('how much to deposit'))
#                             aaa.depositx(x)
#                         except ValueError:
#                             print ('v error 2')
#                     elif reply is 3:
#                         aaa.show()
#                     elif reply is 4:
#                         break
#                     else:
#                         print('pick a valid number')
#         elif reply == 3:
#             print('have a good day')
#             break
#         elif reply is 4:
#             aaa.info()
#     except ValueError:
#         print('please giv valid noomber')
#
#
#
#
#
#
#
#
