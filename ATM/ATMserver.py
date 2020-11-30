# import account
import json
class ATMserver:
#     def __init__():
        
        
    def verify_pin(self, acc_no, pin):
        account_object = self.load_obj(acc_no)
        return account_object["pin"] == pin
    
    def modify_balance(self, acc_no, pin, balance):
        account_object = self.load_obj(acc_no)
        if account_object["pin"] == pin:
            account_object["balance"] = balance
    
    
    def load_obj(self, acc_no):
        with open('Database/'+str(acc_no)+'.json') as f:
            data = json.load(f)
        return data
        
if __name__ == '__main__':
    person_dict = {"name": "Nithish Kumar",
    "languages": ["English", "Tamil"],
    "pin" : 1234,
    "type" : "checkings",
    "acc_no:": 221335260,
    "balance": 10000
    }
     
    with open('Database/110114059.json', 'w') as json_file:
      json.dump(person_dict, json_file)