import os
import time
import sysconfig
from time import time, ctime
import random
from random import randint
from ZuriBank import nDigit

print("|" * 75)
print('*' * 75)
t = time()
print('                 Welcome to Zuri Bank')
print('              ', ctime(t))
print('*' * 75)
customerName = ['Oluwaseun', 'Moses', 'Ayoola']
customerPin = ['1234', '4567', '8901']
customerBalance = [3000, 4000, 5000]
userName = input('Enter name: ')
userPin = input('Enter your pin: ')
finished = False
while not finished:
    if userName in customerName:
        customerId = (customerName.index(userName))
        if userPin == (customerPin[customerId]):
            print(f'\nWelcome {userName} \t  {ctime(t)}\n')
            print('Select service')
            print('\t 1. Cash Deposit')
            print('\t 2. Withdrawal')
            print('\t 3. Get Balance')
            print('\t 4. Complaint')
            print('\t 5. Recharge Phone')
            options = input('Select Service: ')

            if (options == '1'):
                print('How much would you love to deposit ')
                depositAmount = int(input('Enter amount: '))
                customerBalance[customerId] += depositAmount
                print(f'{depositAmount} has been deposited into your account')
                print(f'Your account balance is {customerBalance[customerId]}')

            elif (options == '2'):
                print('How much would you love to withdraw ')
                withdrawalAmount = int(input('Enter amount: '))

                if withdrawalAmount < customerBalance[customerId]:
                    customerBalance[customerId] -= withdrawalAmount
                    print(f'Take your cash\nYour balance is {customerBalance[customerId]}')

                else:
                    print('insufficient funds')
                    print(f'Your account balance is {customerBalance[customerId]}')
            elif (options == '3'):
                print(f'Your account balance is {customerBalance[customerId]}')

            elif (options == '4'):
                print('What issue would you love to report')
                complaint = input('Leave a complaint\n')
                print('Thank you for contacting us\nWe will get back to you shortly')
            elif (options == '5'):
                print('\t 1. Globalcom Nigeria')
                print('\t 2. Airtel Nigeria')
                print('\t 3. MTN')
                print('\t 4. 9mobile')
                selectNetwork = input('Select mobile network: ')
                phoneNumber = input('Enter phone number: ')
                if len(phoneNumber) == 11:
                    if selectNetwork == '1':
                        print(nDigit(15))
                        print('*' * 25)
                        print('Thank you for banking with us!!')
                        print('*' * 25)
                    elif selectNetwork == '2':
                        print(nDigit(16))
                        print('*' * 25)
                        print('Thank you for banking with us!!')
                        print('*' * 25)
                    elif (selectNetwork == '3'):
                        print(nDigit(16))
                        print('*' * 25)
                        print('Thank you for banking with us!!')
                        print('*' * 25)
                    elif selectNetwork == '4':
                        print(nDigit(15))
                        print('*' * 25)
                        print('Thank you for banking with us!!')
                        print('*' * 25)
                else:
                    print('Invalid input, Enter number between 1-4')

            else:
                print('invalid option selected')
                options = input('Select Service: ')
        else:
            print("oops!! Wrong password!!!")
            userPin = input('Enter your pin: ')

    else:
        print('Kindly walk into any of our branchs to register\nThank you for banking with us')
    userTerminate = input('Do you want to perform another transaction Y/N: ')
    if userTerminate.upper() == 'N':
        finished = True
    elif userTerminate.upper() == 'Y':
        finished = False
    else:
        print('oohps Invalid input')
        userTerminate = input('Do you want to perform another transaction Y/N: ')
