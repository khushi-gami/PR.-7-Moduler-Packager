
 
def create_file(filename):
        
    try:
        
        with open(f"moduler & packager/{filename}", "x",encoding="utf-8") as file:
            file.write("File created with x mode.")
        print("file created successfully !")
        
    except FileExistsError:
        print(f"{filename} already exists!")
        
    except OSError as error:
        print(f"file operation failed : {error}")
        
        
def write_content(filename,content):
    
    try:    
        
        with open(f"moduler & packager/{filename}","w",encoding="utf-8") as file:
            file.write(content)
        print("content written successfully !")            
        
    except OSError as error:
        print(f"file operation failed : {error}")
    
def read_file(filename):
        
    try:    
        
        with open(f"moduler & packager/{filename}","r",encoding="utf-8") as file:
            file_content = file.read()
            
        if file_content == "":
            print("file is empty.")
        else:
            print("file content is : \n",file_content)
    
    except FileNotFoundError:
        print(f"{filename} not found !")
        
    except OSError as error:
        print(f"file operation failed : {error}")
            
def append_content(filename,content):
    try:  
          
        with open(f"moduler & packager/{filename}","a",encoding="utf-8") as file:
            file.write(content + "\n")
        print("content appended successfully !")
        
    except OSError as error:
        print(f"file operation failed : {error}")
        

            
    
        
