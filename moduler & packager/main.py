print("==================== Welcome to Multi-Utility Toolkit =======================")


# import modules

from helper import text_input,int_input,float_input,explore_module
import math_utils 
import utilities
import geometry
import random_utils
import uuid_utils


        
class MultiUtilityToolkit:
    
    def date_time(self):
        
        
        while True:
            
            print()
            print("Datetime and Time Operations :")
            print("1. Display current date and time")
            print("2. Calculate difference between two dates/times")
            print("3. Format date into custom format")
            print("4. Stopwatch")
            print("5. Countdown Timer")
            print("6. Back to Main Menu")
            print()
        
            date_time_option = int_input("Select a option (1 to 6) : ",1,6)
            
            if date_time_option == 1 :
                
                print("current date and time : ",utilities.current_date_time())
                
            elif date_time_option == 2 :
                
                while True:
                    
                    print()
                    print("Difference : Date or Time ? :")
                    print("1. Date")
                    print("2. Time")
                    print("3. Back")
                    print()
                    
                    differnce_option = int_input("Select a option : ",1,4)
                    
                    if differnce_option == 1:
                        
                        print("Diffeence between two dates : ",utilities.date_difference(), "days")
                        
                    elif differnce_option == 2:
                        
                        print("Duration between given time : ",utilities.time_difference())
                        
                    elif differnce_option == 3:
                        
                        break
                
            elif date_time_option == 3 :
                
                utilities.date_formating()
                
            elif date_time_option == 4 :
                
                utilities.stopwatch()
                
            elif date_time_option == 5 :
                
                print()
                utilities.countdown(int_input("enter seconds value : ",1,30))
                
            elif date_time_option == 6 :
                break
            
    def math_calculation(self):
        
        
        while True:
            
            print()
            print("Mathematical Operations :")
            print("1. Calculate Factorial")
            print("2. Solve Compound Interest")
            print("3. Trigonometric Calculations")
            print("4. Area of Geometric Shapes")
            print("5. Back to Main Menu")
            print()
            
            math_option = int_input("Select a option (1 to 5) : ",1,5)
            
            if math_option == 1:
                
                print()
                math_utils.factorial(int_input("Enter a number : ",1,30))
                
                
            elif math_option == 2:
                
                math_utils.compound_interest()
                
            elif math_option == 3:
                
                math_utils.trigonometrey(float_input("Enter angle in degrees : "))
                
            elif math_option == 4:
                
                
                while True:
                    
                    print()
                    print("Area of Geometric Shapes :")
                    print("1. Circle")
                    print("2. Triangle")
                    print("3. Back")
                    print()
                    
                    shape_option = int_input("Select a option : ",1,3)
                    
                    if shape_option == 1:
                        
                        print()
                        geometry.circle_area(float_input("Enter the value of radius : "))
                        
                    elif shape_option == 2:
                        
                        print()
                        geometry.triangle_area(float_input("Enter base value : "),float_input("Enter height value : "))
                        
                    elif shape_option == 3:
                        break
                 
            elif math_option == 5:
                break
    
    def random_data(self):
        
        
        
        while True:
            
            print()
            print("Random Data Generation :")
            print("1. Generate Random Number")
            print("2. Generate Random List")
            print("3. Create Random Password")
            print("4. Generate Random OTP")
            print("5. Back to Main Menu")
            print()
            
            random_option = int_input("Select a option (1 to 5) : ",1,5)
            
            if random_option == 1:
                
                print()
                random_utils.random_number(int_input("Enter minimum number : ",1,100),int_input("Enter maximum number : ",1,100))
                
            elif random_option == 2:
                
                print()
                random_utils.random_list(int_input("Enter list length : ",1,20),int_input("Enter minimum number : ",1,100),int_input("Enter maximum number : ",1,100))
                
            elif random_option == 3:
                
                print()
                random_utils.random_password(int_input("Enter password length : ",1,8))
                
            elif random_option == 4:
                
                print()
                random_utils.random_otp(int_input("Enter OTP length : ",1,8))
                
            elif random_option == 5:
                break
            
    def uniq_id(self):
        
        print()
        uuid_utils.uniq_id()
    
    def file_operation(self):
        
        
        while True :
            
            print()
            print("File Operations :")
            print("1. Create a new file")
            print("2. Write to a file")
            print("3. Read from a file")
            print("4. Append to a file")
            print("5. Back to Main Menu")
            print()
                       
            file_option = int_input("Select a option (1 to 5) : ",1,6)
            
            if file_option == 1:
                
                print()
                utilities.create_file(text_input("Enter file name : "))
                
            elif file_option == 2:
                
                print()
                utilities.write_content(text_input("Enter file name : "),text_input("Write file content here : "))
                
            elif file_option == 3:
                
                print()
                utilities.read_file(text_input("Enter file name : "))
                
            elif file_option == 4:
                
                print()
                utilities.append_content(text_input("Enter file name : "),text_input("Write file content to append : "))
                
            elif file_option == 5:
                break
            
    def explore_dir(self):
        
        print()
        explore_module(text_input("Enter module name : "))
        
    
def main():    
    
    toolkit = MultiUtilityToolkit()

        
    while True:
        
        print()
        print("Choose an option :")

        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print()
            
        main_option = int_input("Select a option (1 to 7) : ",1,7)
            
        if main_option == 1:
            
            toolkit.date_time()
            
        elif main_option == 2:
            
            toolkit.math_calculation()
            
        elif main_option == 3:
            
            toolkit.random_data()
            
        elif main_option == 4:
            
            toolkit.uniq_id()
            
        elif main_option == 5:
            
            toolkit.file_operation()
            
        elif main_option == 6:
            
            toolkit.explore_dir()
            
        elif main_option == 7:
            
            print("================================================================")
            print("Thank you for using the Multi-Utility Toolkit !")
            print("================================================================")
            
            break
            
if __name__ == "__main__":
    main()        
    
    
    
