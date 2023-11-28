# 1.Создайте класс BankAccount, который будет иметь следующие свойства: account_number, balance, owner, type. Также, класс должен иметь следующие методы: deposit(), withdraw(), check_balance(), change_owner().

#     - Метод deposit() должен принимать один аргумент amount и добавлять это количество к балансу счета.

#     - Метод withdraw() должен принимать один аргумент amount и вычитать это количество из баланса счета. Перед вычитанием проверьте, достаточно ли средств на счете. Если средств недостаточно, выведите сообщение об ошибке.

#     - Метод check_balance() должен возвращать текущий баланс счета.

#     - Метод change_owner() должен принимать один аргумент new_owner и изменять владельца счета на нового владельца.

# 2.Создайте несколько объектов класса BankAccount и вызовите каждый из методов для каждого из объектов.

# 3.Добавьте в класс BankAccount метод transfer(), который будет принимать два аргумента: amount и other_account. Этот метод должен переводить указанную сумму со счета на other_account. Проверьте, достаточно ли средств на счете для перевода. Если средств недостаточно, выведите сообщение об ошибке.

# 4.Создайте еще один объект класса BankAccount и используйте метод transfer() для перевода средств с одного счета на другой


class BankAccount:
    def __init__(self, account_number, balance, owner, type):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.type = type

    def deposit(self, amount):
        self.balance += amount
        print(f"Депозит на сумму {amount} успешно открыт. Новый баланс составляет {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Недостаточно средств")
        else:
            self.balance -= amount
            print(f"Снятие {amount} успешно завершено. Новый баланс составляет {self.balance}")

    def check_balance(self):
        print(f"Текущий баланс: {self.balance}")

    def change_owner(self, new_owner):
        self.owner = new_owner
        print(f"Смена владельца счёта. Новый владелец {new_owner}")

    def transfer(self, amount, other_account):
        if self.balance < amount:
            print("Недостаточно средств для перевода")
        else:
            self.balance -= amount
            other_account.balance += amount
            print(f"Перевод в размере {amount} успешно завершён. Новый баланс составляет {self.balance}")

# Creating objects of BankAccount class
account1 = BankAccount("123456", 1000, "John Doe", "Savings")
account2 = BankAccount("654321", 2000, "Jane Doe", "Current")

# Calling methods on account1
account1.deposit(500)
account1.withdraw(200)
account1.check_balance()
account1.change_owner("Иван")

# Calling methods on account2
account2.deposit(1000)
account2.withdraw(300)
account2.check_balance()
account2.change_owner("Олег")

# Transferring money from account1 to account2
account1.transfer(300, account2)