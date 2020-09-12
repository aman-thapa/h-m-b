import random

you = 0
computer = 0
lst = ["snake", "water", "gun"]
print("~For snake press 0\n~For water press 1\n~For gun press 2\n")
for i in range(1, 10):
    a = int(input())
    print("Your choice:- ", lst[a])
    b = random.randint(0, 2)
    print("computer choice:- ", lst[b])
    print("Your life is:- ", 10 - i)

    if a == b:
        print("You<---->Computer")
    elif a == 0 and b == 1:
        print("YOU WIN!")
        you += 1
    elif a == 1 and b == 0:
        print("COMPUTER WIN")
        computer += 1
    elif a == 1 and b == 2:
        print("YOU WIN")
        you += 1
    elif a == 2 and b == 1:
        print("COMPUTER WIN")
        computer += 1
    elif a == 2 and b == 0:
        print("YOU WIN")
        you += 1
    elif a == 0 and b == 2:
        print("COMPUTER WIN")
        computer += 1
print("\n\n\nYour score is", you, "\nComputer score is", computer)
if you > computer:
    print("Winner Winner Chicken Dinner")
elif you == computer:
    print("It's a tie !")
else:
    print("You lost! Try Again.")
