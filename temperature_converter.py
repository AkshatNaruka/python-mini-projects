print("temperature converter")
opt=int(input("1.celsius to fahrenheit\n 2.fahrenheit to celsius"))
if opt==1:
    celsius=int(input("enter temperature in celsius"))
    fahrenheit=(9/5*celsius)+32
    print(fahrenheit)
elif opt==2:
    fahrenheit=int(input("enter temperature in fahrenheit"))
    celsius=(fahrenheit-32)*5/9
    print(celsius)
else :
    print("choose the correct option") 