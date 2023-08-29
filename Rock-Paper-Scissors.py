from random import randint

t = ["Schere", "Stein", "Papier"]
computer = t[randint(0,2)]
player = False

while player == False:
    player = input("Schere, Stein, Papier?")
    if player == computer:
        print("Unentschieden!")
    elif player == "Stein":
        if computer == "Papier":
            print("Du hast Verloren!", computer, "umwickelt", player)
        else:
            print("Du hast Gewonnen!", player, "zerstört", computer)
    elif player == "Papier":
        if computer == "Schere":
            print("Du hast Verloren!", computer, "schneidet", player)
        else:
            print("Du hast Gewonnen!", player, "umwickelt", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("Du hast Verloren...", computer, "zerstört", player)
        else:
            print("Du hast Gewonnen!", player, "schneidet", computer)
    else:
        print("Falsche Dateneingabe. Achte auf die Rechtschreibung!")
    player = False
    computer = t[randint(0,2)]
