from datetime import datetime , date , timedelta
import time
from helper import int_input , text_input


# date functions ------------------------------------------------

def current_date_time():
    
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def date_difference():
    while True:    
        try:

            first_date = datetime.strptime(text_input("Enter first date (YYYY-MM-DD) : "), "%Y-%m-%d")
            second_date = datetime.strptime(text_input("Enter second date (YYYY-MM-DD) : "), "%Y-%m-%d")

            days = abs(first_date - second_date).days
            return days
        
        except ValueError:
            print("invalid formate !!")
            continue

def time_difference():
    while True:
        try:
             
            start_time = datetime.strptime(text_input("Enter start time (H:M:S) : "), "%H:%M:%S")
            end_time = datetime.strptime(text_input("Enter end time (H:M:S) : "), "%H:%M:%S")
            
            time = abs(start_time - end_time)
            return time
        except ValueError:
            print("invalid formate !!")
            continue
            

def date_formating():
    while True:
        try:
            
            now = datetime.strptime(text_input("Enter date (YYYY-MM-DD) : "),"%Y-%m-%d")
            
        except ValueError:
            print("invalid formate !!")
            continue
        
        print("Original date : ",now.strftime("%d-%m-%Y"))
        print("DD-MM-YYYY : ",now.strftime("%d-%m-%Y"))
        print("MM-DD-YYYY : ",now.strftime("%m-%d-%Y"))
        print("Month : ",now.strftime("%B"))
        print("Day : ",now.strftime("%A"))
        break
        
        
    
def stopwatch():
    
    start_time = None
    elapsd_time = 0
        
    while True:
        
        print()
        print("stopwatch : ")
        print("1. start")
        print("2. stop")
        print("3. reset")
        print("4. exit")
        
        choice = int_input("enter your choice : ",1,4)
    
        if choice == 1:
           
           if start_time is None:
               
               start_time = time.time()
               print("stop start ......")
            
           else:
               print("stop watch is already running.....!!")
        
        elif choice == 2 :
            
            if start_time is not None:
                
                elapsd_time = elapsd_time + (time.time() - start_time)
                start_time = None
                
                print("stop watch stoped .......")
                print("Time : ",round(elapsd_time,2),"seconds")
                
            else:
                
                print("first start stopwatch with choice 1")
        
        elif choice == 3:
            
            start_time = None
            elapsd_time = 0
            print("stop watch reset !!")
        
        
        elif choice == 4 :
            
            print("existing stopwatch programme ! bye !")
            
            break    


def countdown(seconds):

    while seconds > 0:
        
        print(seconds)
        time.sleep(1)
        
        seconds -= 1
    print("Time's up !")
    




    