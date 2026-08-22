import random

animals = ["Rabbit", "Lion", "Dolphin", "Snake"]
item = random.choice(animals)

print("Guess the Animal")
print("Start!!")

if item == "Rabbit":
    print("Hint 1 = It has four legs")
    take1 = input()
    if take1 == item:
        print("Guessed it right")
    else:
        print("Hint 2 = It lives on land")
        take2 = input()
        if take2 == item:
            print("Guessed it right")
        else:
            print("Hint 3 = It has long ears and is furry")
            take3 = input()
            if take3 == item:
                print("Guessed it right")
            else:
                print("Hint 4 = It likes carrots")
                take4 = input()
                if take4 == item:
                    print("Guessed it right")
                else:
                    print("You lost! The animal was", item)

elif item == "Lion":
    print("Hint 1 = It has four legs")
    take1 = input()
    if take1 == item:
        print("Guessed it right")
    else:
        print("Hint 2 = It is a wild animal")
        take2 = input()
        if take2 == item:
            print("Guessed it right")
        else:
            print("Hint 3 = The male has a mane")
            take3 = input()
            if take3 == item:
                print("Guessed it right")
            else:
                print("Hint 4 = It is called the king of the jungle")
                take4 = input()
                if take4 == item:
                    print("Guessed it right")
                else:
                    print("You lost! The animal was", item)

elif item == "Dolphin":
    print("Hint 1 = It lives in water")
    take1 = input()
    if take1 == item:
        print("Guessed it right")
    else:
        print("Hint 2 = It is a mammal")
        take2 = input()
        if take2 == item:
            print("Guessed it right")
        else:
            print("Hint 3 = It is very intelligent")
            take3 = input()
            if take3 == item:
                print("Guessed it right")
            else:
                print("Hint 4 = It can jump out of water")
                take4 = input()
                if take4 == item:
                    print("Guessed it right")
                else:
                    print("You lost! The animal was", item)

elif item == "Snake":
    print("Hint 1 = It has no legs")
    take1 = input()
    if take1 == item:
        print("Guessed it right")
    else:
        print("Hint 2 = It has scales")
        take2 = input()
        if take2 == item:
            print("Guessed it right")
        else:
            print("Hint 3 = It can crawl")
            take3 = input()
            if take3 == item:
                print("Guessed it right")
            else:
                print("Hint 4 = It can be poisonous")
                take4 = input()
                if take4 == item:
                    print("Guessed it right")
                else:
                    print("You lost! The animal was", item)
