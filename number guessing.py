import random
print("DECIDE YOUR RANGE FOR GUESSING THE NUMBERS BETWEEN THE RANGE")
a=int(input("Enter value of a(range starts from this number)"))
b=int(input("Enter value of b(range ends here)"))
num = random.randint(a, b)
guess = None

while guess != num:
    guess = input("guess a number between a and b: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        print("Your guess was right ,the number was", guess )
    else:
        print("nope, sorry. try again!")
