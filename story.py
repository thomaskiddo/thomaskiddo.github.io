#My Python Story
import time

time.sleep(1)

def greeting():
    print("Hello...")
    time.sleep(1)
    response=input("Do you want to play a game? (yes/no) ")
    return response


def second_choice():
    time.sleep(1)
    print("Great...")
    time.sleep(1)
    response=input("Which door do you open? (left/right) ")
    return response
def haters():
    print("Lame...Bye Then! ")

def third_choice():
    time.sleep(3)
    print("Congratulations, you survived the first round! ")
    time.sleep(3)
    response=input("WATCH OUT THERE'S A SHARK!! What do you do? (run/hide) ")
    return response

def left():
    print("You tripped and fell in lava... THE END ")

def run():
    time.sleep(3)
    print("The shark is faster than you. THE END ")

def last_choice():
    time.sleep(3)
    print("The shark did not see you. YOU HAVED SURVIVED COMRADE ")
    time.sleep(3)
    response=input("You've made it to the end of the game. Choose your faith and collect your reward.(one/two) ")
    return response

def shrimp():
    time.sleep(3)
    print("You have chosen the All-you-can-eat-shrimp for $4.99. Enjoy! ")

def hotpocket():
    time.sleep(3)
    print("You have chosen 100 Hot Pockets. Enjoy! ")
    
x = greeting()
if x== "yes":
    y = second_choice()
    if y== "right":
        z = third_choice()
        if z== "hide":
            a = last_choice()
            if a== "one":
                 b= shrimp()


            else:
                hotpocket()
        else:
            run()
    else:
        left()



else:
    haters()



