import random
import string

def random_number(minimum,maximum):
    if minimum < 0 or maximum < 0:
        print("negative number is not allowed !")
    elif maximum < minimum:
        print("minimum number is not greater then maximum number ! ")
    else :
        value = random.randint(minimum,maximum)
        print("Random number is : ",value)
        
        
def random_list(length,minimum,maximum):
    if minimum < 0 or maximum < 0:
        print("negative number is not allowed !")
    elif maximum < minimum:
        print("minimum number is not greater then maximum number ! ")
    else :
        list_data = []
        for i in range(length):
            list_data.append(random.randint(minimum,maximum))
        print("Random list is : ",list_data)
        
def random_password(length):
    
    values = string.ascii_letters + string.digits + string.punctuation
    
    password = "".join(random.choices(values,k=length))
    
    print("your password is : ",password)
    

def random_otp(length):
    
    otp = "".join(random.choices("0123456789",k=length))
    
    print("your otp is : ",otp)
    
    
if __name__ == "__main__":
    random_otp(6)