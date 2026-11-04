email= "Aadarshpatil@gmail.com"

Position = email.find("@")
username = email[:Position]

print("Username =",username)
u2=email[3:Position]
print(u2)