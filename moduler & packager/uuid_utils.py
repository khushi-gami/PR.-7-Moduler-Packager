import uuid

def uniq_id():
    
    id = uuid.uuid4()
    print("Generated uuid : ",id)
    
if __name__ == "__main__":
    print("this scripts run directly.")
    uniq_id()
    

