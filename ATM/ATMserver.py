# import account
import json
import os

class ATMserver:
    dir_path = os.path.dirname(os.path.realpath(__file__))
        
#     def __init__():
        
        
    def verify_pin(self, acc_id, pin):
        account_object = self.load_obj(acc_id)
        return account_object["pin"] == pin
    
    def update_balance(self, acc_id, pin, amount, mode):
        account_object = self.load_obj(acc_id)
        
        if account_object["pin"] == pin and mode == 2:
            print("Before::",account_object["balance"])
            account_object["balance"] += amount
            print("Update::",account_object["balance"])
        if account_object["pin"] == pin and mode == 3:
            account_object["balance"] -= amount + int(account_object["fee"])
        with open(ATMserver.dir_path+'/Database/'+str(acc_id)+'.json', 'w') as f:
              json.dump(account_object, f)
               
    def load_obj(self, acc_id):
        with open(ATMserver.dir_path+'/Database/'+str(acc_id)+'.json') as f:
            data = json.load(f)
        
        return data
    
    def return_balance(self,acc_id, pin):
        account_object = self.load_obj(acc_id)
        account_object["balance"] = int(account_object["balance"])
        if account_object["pin"] == pin:
            return account_object["balance"]
        
if __name__ == '__main__':
    person_dict = {"name": "Nithish Kumar",
    "languages": ["English", "Tamil"],
    "pin" : "1234",
    "type" : "checkings",
    "acc_id": 221335260,
    "balance": 10000,
    "fee": "2"
    }
     
    with open('Database/'+str(person_dict["acc_id"])+'.json', 'w') as json_file:
      json.dump(person_dict, json_file)