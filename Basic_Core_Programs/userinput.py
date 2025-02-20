while True:
    user_name = input("Hi! Your name ?:")
    
    if len(user_name) >= 3:
        break
    else:
        print(f"Please write a name of more than 3 letters")

template = "Hello <<UserName>>, How are you?"
message = template.replace("<<UserName>>", user_name)
print(message)
#Implement f string 