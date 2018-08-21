#!/usr/bin/python2.7

amount = int(raw_input("How many items: "))

while amount < 0:
    print("Please enter a valid integer greater than zero")
    amount = int(raw_input("Again, how many items: "))

word = raw_input("What do you want to pluralize: ")

if amount > 0:
    amount = str(int(amount))

def basic():
    print("You have "+ amount +" "+ word +"s")

def ife():
    print("You have "+ amount +" "+ word[:-3] +"ives")

def h():
    print("You have "+ amount +" "+ word +"es")

def xy():
    print("You have"+ amount +" "+ word +"s")
    
def us():
    print("You have "+ amount +" "+ word[:-2] +"i")

def i():
    print("You have "+ amount +" "+ word[:-1] +"ies")

endings2 = ["ife","sh","ch","us","ay","oy","ey","uy"]
endingsh = ["sh","ch"]
endingsxy = ["ay","oy","ey","uy"]
endingsus = ["us"]
endingy = ["y"]

if word[-3:] in endings2:
    ife()

elif word[-2:] in endingsh:
    h()
    
elif word[-2:] in endingsxy:
    basic()

elif word[-2:] in endingsus:
    us()

elif word[-1:] in endingy and word[-1:] not in endings2:
    i()

else:
    basic()
