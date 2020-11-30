class ATMcontroller:
    def __init__(self, _interface, _server=None):
        self.interface = _interface
        self.server = _server
        self.operation = {}
    
    def transaction(self):
        self.interface.welcome_message()
        (acc_id, pin)= self.interface.input_user_credentials()
        
        if self.verify(acc_id, pin):
            self.mode = self.interface.select_mode()
            if int(self.mode) ==1 :
                self.interface.current_balance(1000)
                self.operation["total"] =1000
            if int(self.mode) ==2:
                self.amount = input("Enter amount:")
                print("here")
            if int(self.mode) ==3:
                self.amount = input("Enter amount:")
                print("here1")
            self.operation["status"] = True
            self.operation["mode"] = self.mode
            self.operation["total"] = self.amount
            self.interface.transaction_result(self.operation) 
            
        else:
            self.operation["status"] = False
            self.interface.transaction_result(self.operation) 
    
    def isValid(self, amount):
        if amount < 0:
            print("Enter a positive value")
        elif amount > 10000:
            print("Transaction limit < 10000")
        else 
            return True
        return False
        
    def verify(self, acc_id, pin):
        return True