class BankAccount:
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance


    def print_statement(self):
        print(f"Full name: {self.full_name}, Account number: {self.account_number}, Balance: {self.balance}")


mitchellAccount = BankAccount("Mitchell Trubisky", "58432883", "0")
mitchellAccount.print_statement()        

    