

name = input("What is your name? ")
age = int(input("How old are you? "))
hasTicket = True

if age >= 60 and hasTicket:
    print("You are a senior and is able to watch the movie paying a senior discounted price for the ticket")

elif age >= 18 and hasTicket:
    print("You are an adult and is able to watch the movie paying full price for the ticket")

elif age >= 7 and hasTicket:
    print("You are able to watch the ticket with a student discount and with supervision")

elif age == 0:
    print("You are just born")

elif age >= 60 and not hasTicket:
    print("You are a senior and is not able to watch the movie as you do not have a ticket")

elif age >= 18 and not hasTicket:
    print("You are an adult and is not able to watch the movie as you do not have a ticket")

elif age >= 7 and not hasTicket:
    print("You are not able to watch the movie as you do not have a ticket")

elif age == 0:
    print("You are just born")