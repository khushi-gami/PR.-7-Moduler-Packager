# ---------------- for safe user input ----------------------

def int_input(message,minimum,maximum):
    while True:
        try:
            number = int(input(message))
            if number < minimum or number > maximum:
                print(f"enter number between {minimum} to {maximum}")
                print()
            else:
                return number
        except ValueError:
            print("Invalid value enterted !")
            print()

def text_input(message):
    while True:
        text = input(message).strip()
        if text == "":
            print("This field cannot be empty.")
            print()
        else:
            return text
        
def float_input(message):
    while True:
        try:
            number = float(input(message))
            if number < 0:
                print("Value cannot be negative.")
                print()
            else:
                return number
        except ValueError:
            print("Invalid input ! Please enter a number.")
            print()


def explore_module(module):
    
    modules = ["math","random","datetime","time","uuid"]
    
    if module in modules:
        print(dir(module))
        print()
    else:
        print("module not found !")
        
