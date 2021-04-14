
#    ***** ** Zuri  Budget Mock project ** *****


class budget:

    def __init__(self, categories=['Food', 'Clothing', 'Entertainment'], categoryBalance=[0, 0, 0]):

        self.categories = categories
        self.categoryBalance = categoryBalance

    def deposit(self):
        amount = int(input('Enter amount to deposit: '))
        try:
            self.categoryBalance[self.selectedCategory] += amount
            print(f'{amount} as been deposited successfully into your {self.categorySelected} budget')
            self.openApp()
        except ValueError:
            print('oohps!! use digits')

    def withdrawal(self):
        withdrawalAmount = int(input('Enter amount to withdraw: '))
        try:
            if self.categoryBalance[self.selectedCategory] >= withdrawalAmount:
                self.categoryBalance[self.selectedCategory] -= withdrawalAmount
                print(f'Withdrawal successful \n {withdrawalAmount} left your {self.categorySelected} budget')
                self.openApp()
            else:
                print('insufficeint balance')
                self.openApp()
        except ValueError:
            print('please enter digit')
            self.openApp()

    def checkBalance(self):
        print(f'Your account balance is {self.categoryBalance[self.selectedCategory]} in {self.categorySelected}')
        self.openApp()

    def transfer(self):
        transCat = int(input('Categories:\n1. Food\n2. Clothing\n3. Entertainment\nEnter category to transfer: '))
        toCategory = transCat - 1
        try:
            transferCategory = self.categories[toCategory]
            transferAmount = int(input('Enter amount to transfer: '))
            try:
                if self.categorySelected != transferCategory:
                    if self.categoryBalance[self.selectedCategory] > transferAmount:
                        self.categoryBalance[self.selectedCategory] -= transferAmount
                        self.categoryBalance[toCategory] += transferAmount
                        print(f'{transferAmount} left your {self.categorySelected} budget to {transferCategory} budget')
                        self.openApp()
                    else:
                        print('insufficient balance')
                        self.openApp()
                else:
                    print("Can't transfer into same account")
                    self.openApp()
            except ValueError:
                print('please use number')
                self.openApp()
        except IndexError:
            print('operation not found please select between 1 - 3')
            self.openApp()
        except ValueError:
            print('use digits')
            self.openApp()

    def openApp(self):
        print('************* Welcome to BudgetApp *************')
        for category in self.categories:
            print(f"{self.categories.index(category) + 1}. {category}")
        selectCategory = int(input('Choose category: '))
        try:
            try:
                self.selectedCategory = selectCategory - 1
                self.categorySelected = self.categories[self.selectedCategory]
                operations = ['Deposit', 'Withdrawal', 'Transfer', 'Check Balance' ]
                for operation in operations:
                    print(f"{operations.index(operation) + 1}. {operation}")
                selectOperation = int(input('Enter operaions: '))
                try:
                    if selectOperation == 1:
                        self.deposit()
                    elif selectOperation == 2:
                        self.withdrawal()
                    elif selectOperation == 3:
                        self.transfer()
                    elif selectOperation == 4:
                        self.checkBalance()
                    else:
                        print('Enter digits between 1 -4')
                        self.openApp()
                except ValueError:
                    print('Value not accepted!!\n Use digit')
                    self.openApp()

            except ValueError:
                print('please use digits')
                self.openApp()
        except ValueError:
            print('please use digits')
            self.openApp()
        except IndexError:
            print('operation not found; use digit between 1 - 4')


category = budget()
category.openApp()
