while True:           
    user_ = "username"    
    pass_ = "password"   
    username = input("Username : ")  
    password = input("Password : ")  
    if username != user_:    
        input("Username Salah!")  
        continue  
    elif password != pass_:   
        input("Password Salah!")   
        continue   
    else:        
        input("Login Berhasil!")  
        break  