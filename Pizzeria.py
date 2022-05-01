# Dio cane

def main():

    price = 14
    
    print("Welcome to Porco Dio's pizzeria!")

    print("What is your name?")

    name = input()

    if name.lower() == "bergoglio":
        print("You are not welcome here, get out Dio cane!")
        return
    elif name.lower() == "germano":
        print("Guarda un po' chi c'è, Dio stracane maledetto!! Lei ha il diritto ad uno sconto!")
        price = 10

    print(f"Hello {name}, welcome to our pizzeria!")
    
    print("Are you vegeterian?")
    
    if input().lower() == "yes":
        menu = "Rompipalle vegan, Sterco di Gallina, Piselli"
        price = 20
    else:
        menu = "Vaffanculo, Madonna Santa, Bastardo, Testa di Cazzo, Baldracca"

    print(f"Here is our menu:\n{menu}")

    order = input("What would you like to order?\n")

    print(f"How many {order}s would you like?")

    amount = input()

    print(f"Your total is {price * int(amount)}€")

    print(f"Thank you {name}, your {amount} {order}s will be ready soon!")
    
main()