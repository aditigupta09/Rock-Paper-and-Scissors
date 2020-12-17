import random
import pyttsx3


engine = pyttsx3.init()
def play():
    print("Rules ")

    print("Rock vs paper --> paper wins")
    print("Rock vs scissor --> rock wins")
    print("Scissor vs paper --> scissor wins \n")
    engine.say(
        "Rules for the game are :       Rock vs paper then paper wins , Rock vs scissor then rock wins and Scissor vs paper then scissor wins")
    engine.runAndWait()
    choice()

def choice():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    engine.say("please enter your choice number ")
    engine.runAndWait()
    n = int(input("please enter your choice no. :  "))


    if n==1:
        print("So, your choice is Rock!!")
        engine.say("So, your choice is Rock!!")
        engine.runAndWait()
    elif n==2:
        print("So, your choice is Paper!!")
        engine.say("So, your choice is Paper!!")
        engine.runAndWait()
    elif n==3:
        print("So, your choice is Scissor!!")
        engine.say("So, your choice is Scissor!!")
        engine.runAndWait()
    else:
        print("Sorry!!")
        engine.say("Sorry!!")
        engine.runAndWait()

    print()
    print("Now, it's computer turn to iniate.......")


    comp = random.randint(1,3)
    while comp == n:
         comp = random.randint(1,3)
    print()
    if comp==1:
         print("And, computer's choice is Rock!! \n")
         engine.say("And, computer's choice is Rock!!")
         engine.runAndWait()
    elif comp==2:
         print("And, computer's choice is Paper!! \n")
         engine.say("And, computer's choice is Paper!!")
         engine.runAndWait()
    elif comp==3:
         print("And, computer's choice is Scissor!! \n")
         engine.say("And, computer's choice is Scissor!!")
         engine.runAndWait()
    print()

    if ((n == 1 and comp == 2) or (n == 2 and comp == 1)):
        print("Paper wins !!")
        engine.say("Paper wins !!")
        engine.runAndWait()
    elif ((n == 1 and comp == 3) or (n == 3 and comp == 1)):
        print("Rock wins !!")
        engine.say("Rock wins !! yep yep")
        engine.runAndWait()
    elif ((n == 2 and comp == 3) or (n == 3 and comp == 2)):
        print("Scissor wins !!")
        engine.say("Scissor wins !! yep yep")
        engine.runAndWait()
    else:
        print("sorry")

    ask()

def ask():
    print("you wanna play ? yes or no")
    engine.say("you wanna play ? yes or no")
    engine.runAndWait()
    value = input(" ?? : ")

    if value == "yes":
        play()
    else:
        print("bye bye!!")
        engine.say("okayy bye bye have a good day")
        engine.runAndWait()


ask()