import argparse

class ATMinterface:
    def __init__(self):
        self.bin_balance = 10000
        self.detect_card_swipe = False
        self.available_twenty_notes = 100
        self.available_fifty_notes = 100
    
    def update_bin(self, _balance):
        self.bin_balance = _balance
            
    def return_bin_capacity(self):
        return (self.bin_balance, self.available_fifty_notes, self.available_twenty_notes)
    
    def parse_input(self, arg):
        parser = argparse.ArgumentParser(description='This is an ATM simulator')
        parser.add_argument('--twenty_notes', metavar='twenty_notes', type=self.validate_num_notes, 
            help='The number of notes with $20 value', required=True)
        parser.add_argument('--fifty_notes', metavar='fifty_notes', type=self.validate_num_notes, 
            help='The number of notes with $50 value', required=True)
        args = parser.parse_args()
        return (args.twenty_notes, args.fifty_notes)
    
    def welcome_message(self):
        print("Welcome to this ATM")
        
    def input_user_credentials(self):
        acc_id = input("Swipe card / Enter Card number:")
        pin = input("PIN: ")
        return (acc_id, pin)
    
    def select_mode(self): 
        type = input("Choose account type (1.checkings / 2. savings):")
        print("Modes:")
        print("1) Check balance")
        print("2) Deposit")
        print("3) Withdraw")
        print("4) Exit")
        mode = input("Choose one of the options:")
        return mode
    
    def current_balance(self, _balance):
        print(" Current Account balance: ",_balance)
        
    def transaction_result(self, operation):
        if operation["status"]:
            print("Successful ", operation["mode"])
            print("Total amount: ", operation["total"])
        else:
            print("Transaction failed")

# def main():
#     print("main")
#     obj =  ATMinterface()
#     obj.welcome_message()
# 
# if __name__ == '__main__':
#     main()