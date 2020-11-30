class ATMcontroller:
    def __init__(self, _interface, _server=None):
        self.interface = _interface
        self.server = _server
        self.operation = {}
    
    def transaction(self):
        self.interface.welcome_message()
        (acc_id, pin)= self.interface.input_user_credentials()
        
        if self.server.verify_pin(acc_id, pin):
            while True:
                self.mode = int(self.interface.select_mode())
                if self.mode == 4:
                    break
                if self.mode ==1 :
                    amount = self.server.return_balance(acc_id, pin)
                    self.interface.current_balance(amount)
                    self.operation["total"] = amount
                if self.mode ==2:
                    amount = int(input("Enter amount:"))
                    if self.isValid(amount):
                        print("in")
                        self.server.update_balance(acc_id, pin, amount, self.mode)
                if self.mode ==3:
                    amount = int(input("Enter amount:"))
                    if self.isValid(amount):
                        print("in")
                        self.server.update_balance(acc_id, pin, amount, self.mode)
                self.operation["status"] = True
                self.operation["mode"] = self.mode
                self.operation["total"] = self.server.return_balance(acc_id, pin)
                self.interface.transaction_result(self.operation) 
            
        else:
            self.operation["status"] = False
            self.interface.transaction_result(self.operation) 
    
    def isValid(self, amount):
        if amount < 0:
            print("Enter a positive value")
        elif amount > 10000:
            print("Transaction limit < 10000")
        else:
            return True
        return False