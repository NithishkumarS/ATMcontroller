import numpy as np
import ATMcontroller
import ATMserver
import ATMinterface

def main():
    
    server = ATMserver.ATMserver()
    interface = ATMinterface.ATMinterface()
    controller = ATMcontroller.ATMcontroller(interface, server)

#     (twenty_notes, fifty_notes) = controller.parse_input_arg()

    controller.transaction()

if __name__ == '__main__':
    main()