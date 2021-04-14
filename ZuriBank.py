#  ***** ** Zuri  ATM mock project ** *****

import os
import time
import sysconfig
from time import time, ctime
import random
from random import randint

newUser = {}

# Variables definitions
# Internet homepage dashboard
print('^' * 65)
t = time()
print('                   Welcome to Zuri Bank')
print('                ', ctime(t))
print('1. Login \t\t\t\t\t 2. Register ')
print('*' * 65)

# Produce desired range of random numbers


def nDigit(d):
    rangeStart = 10 ** (d - 1)
    rangeEnd = (10 ** d) - 1
    return randint(rangeStart, rangeEnd)

# Registration of user on Zuri bank


def registerUser():
    newUserEmail = input('email: ')
    newUserFirstName = input('Enter your first Name: ')
    newUserLastName = input('Enter your last Name: ')
    newUserPhoneNumber = input('Enter phone number: ')
    newUserAddress = input('Enter address: ')
    newUserPassword = input('Creat paasssword: ')
    newUserAccount = nDigit(10)
    newUserBalance = 0
    newUser[newUserAccount] = [newUserEmail, newUserFirstName, newUserLastName, newUserAddress, newUserPhoneNumber, newUserBalance, newUserPassword]

    print(f'Welcome {newUserFirstName.upper(), newUserLastName.capitalize()} to Zuri Bank.\nYour Account number is {newUserAccount}')
    userLogin(registerUser)


# User login to zuri bank internet board

def userLogin(registerUser):
    print('\t\t Enter your login details')
    modeOfLogin = input(
        '\t\t\tLogin using\n1. Account Number\t\t\t2. Email\nEnter a number: ')
    for newUserAccount, newUserDetails in newUser.items():
        if modeOfLogin == '1':
            accountNoLogin = int(input('Enter account number: '))
            accountPassword = input('Enter Password: ')
            if (newUserAccount == accountNoLogin):
                if (newUserDetails[-1] == accountPassword):
                    bankOperation(newUser)
                else:
                    print('Wrong password')
                    userLogin(registerUser)
            else:
                print('Wrong details')
                userLogin(registerUser)
        elif modeOfLogin == '2':
            emailLogin = input('Enter Email: ')
            accountPassword = input('Enter Password: ')
            if (newUserDetails[0] == emailLogin):
                if (newUserDetails[-1] == accountPassword):
                    bankOperation(newUser)
                else:
                    print('Wrong password')
                    userLogin(registerUser)
            else:
                print('Wrong details')
                userLogin(registerUser)
        else:
            print('Invalid entry\nPlease enter number between 1 and 2')
            userLogin(registerUser)


# Bank operations


def bankOperation(newUser):
    for key, newUserDict in newUser.items():
        print(f'\nWelcome {newUserDict[1].capitalize()} \t\t  {ctime(t)}\n')
        print('Select service')
        print('\t 1. Cash Deposit')
        print('\t 2. Withdrawal')
        print('\t 3. Get Balance')
        print('\t 4. Complaint')
        print('\t 5. Recharge Phone')
        print('\t 6. Logout')
        print('\t 7. Exit')
        options = input('Select Service: ')
        try:
            if (options == '1'):
                depositOption()
                bankOperation(newUser)
            elif (options == '2'):
                withdrawalOption()
                bankOperation(newUser)
            elif (options == '3'):
                checkBalanceOption()
                bankOperation(newUser)
            elif (options == '4'):
                comlaintOption()
                bankOperation(newUser)
            elif (options == '5'):
                phoneRechargeOption()
                bankOperation(newUser)
            elif (options == '6'):
                logoutOption()
            elif (options == '7'):
                exitOption()
            else:
                print('Please select an option ')
                bankOperation(newUser)
        except ValueError:
            print('Enter number')
            bankOperation(newUser)


def withdrawalOption():
    print('How much would you love to withdraw ')
    withdrawalAmount = int(input('Enter amount: '))
    for key, newUserDict in newUser.items():
        if withdrawalAmount < newUserDict[-2]:
            newUserDict[-2] -= withdrawalAmount
            print(f'Take your cash\n{withdrawalAmount} left your account')

        else:
            print('insufficient funds')
            print(f'Your account balance is {newUserDict[-2]}')


def depositOption():
    for key, newUserDict in newUser.items():
        print('How much would you love to deposit ')
        depositAmount = int(input('Enter amount: '))
        newUserDict[-2] += depositAmount
        print(f'{depositAmount} has been deposited into your account')


def checkBalanceOption():
    for key, newUserDict in newUser.items():
        print(f'Your account balance is {newUserDict[-2]}')


def phoneRechargeOption():
    print('\t 1. Globalcom Nigeria')
    print('\t 2. Airtel Nigeria')
    print('\t 3. MTN')
    print('\t 4. 9mobile')
    selectNetwork = input('Select mobile network: ')
    phoneNumber = input('Enter phone number: ')
    rechargeAmount = int(input('Enter amount: '))
    for key, amount in newUser.items():
        amount[-2] -= rechargeAmount

        if len(phoneNumber) == 11:
            if selectNetwork == '1':
                print('*' * 25)
                print(nDigit(15))
                print('*' * 25)
                print('Thank you for banking with us!!')
                print('*' * 25)
            elif selectNetwork == '2':
                print('*' * 25)
                print(nDigit(16))
                print('*' * 25)
                print('Thank you for banking with us!!')
            elif (selectNetwork == '3'):
                print('*' * 25)
                print(nDigit(16))
                print('*' * 25)
                print('Thank you for banking with us!!')
            elif selectNetwork == '4':
                print('*' * 25)
                print(nDigit(15))
                print('*' * 25)
                print('Thank you for banking with us!!')
        elif len(phoneNumber) < 11:
            print('Phone number not complete')
            phoneNumber = input('Enter phone number: ')
            bankOperation(newUser)
        elif len(phoneNumber) > 11:
            print('Phone number too long')
            phoneNumber = input('Enter phone number: ')
            bankOperation(newUser)
        else:
            bankOperation(newUser)

    # End programme


def exitOption():
    print('Thank you for banking with us')


def comlaintOption():
    print('What issue would you love to report')
    complaint = input('Leave a complaint\n')
    print('Thank you for contacting us\nWe will get back to you shortly')
    bankOperation(newUser)


def logoutOption():
    finished = False
    while not finished:
        userTerminate = input(
            'Do you want to perform another transaction Y/N: ')
        if userTerminate.upper() == 'N':
            userLogin(registerUser)
            finished = True
        elif userTerminate.upper() == 'Y':
            finished = False
            bankOperation(newUser)
        else:
            print('oohps Invalid input')


def initials():
    programReload = False
    visitor = input('Select option: ')
    while programReload == False:
        if visitor == '1':
            programReload = True
            userLogin(registerUser)
        elif visitor == '2':
            programReload = True
            registerUser()
        else:
            print('Invalid options')


initials()
