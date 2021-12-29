import random
length=int(input("Enter length of password"))
x="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
password = "".join(random.sample(x,length))
print(password)
