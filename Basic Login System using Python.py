#!/usr/bin/env python
# coding: utf-8

# In[17]:


granted = False
def grant():
    global granted
    granted = True
def login(name,password):
    success = False
    file = open("user_detail.txt","r")
    for i in file:
         a,b = i.split(",")
         b = b.strip()
         if(a==name and b==password):
             success = True
             break
    file.close()
    if(success):
        print("Login Successful")
        grant()
    else:
        print("wrong user name or password")
        
def register(name,password):
    file = open("user_detail.txt","a")
    file.write("\n"+name+","+password)
    grant()
def access(option):
    global name
    if(option=="login"):
        #used to login into the site 
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        login(name,password)
    else:
        #used to register into the site
        print("Enter your name and password to register")
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        register(name,password)

def begin():
    global option
    print("Hey User! Hitesh Welcomes you to this site")
    option = input("login or register (login,reg): ")
    if(option!="login" and option!="reg"):
        begin()
        
begin()
access(option)

if(granted):
    print("Hey User! Hitesh Welcomes you to this site")
    print("### USER DETAILS ###")
    print("Username: ",name)


# In[ ]:




