import math
from helper import float_input,int_input

def factorial(number):
    
    print(f"Factorial of {number} is : ",math.factorial(number))
    
    
def compound_interest():
    
    print()
    principal_amount = float_input("Enter Principal amount : ")
    rate = float_input("Enter interest rate (%) : ")
    years = float_input("Enter time in years : ")
    
    print()
    amount = principal_amount * (1 + rate / 100) ** years
    interest = amount - principal_amount  
    
    print(f"Compound interest: {interest:.2f}")
    print(f"Final amount: {amount:.2f}")   
       
    
def trigonometrey(angle):
    
    print()
 
    radians = math.radians(angle)
    
    print("Sine : ",round(math.sin(radians),4))
    print("Cosine : ",round(math.cos(radians),4))
    print("Tangent : ",round(math.tan(radians),4))
    
    
if __name__ == "__main__":
    print("the script excuted directly !")
    
    print()
    print("factorial : ")
    factorial(int_input("enter a number : ",1,30))