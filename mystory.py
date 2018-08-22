#!/usr/bin/python2.7
nendings = ["es"]
nendings2 = ["s","i"]
nendings3 = ["ss","as","us"]

print("Welcome to the story maker")

ch1 = raw_input("Enter a character name: ")
ch2 = raw_input("Enter another character name: ")
ch3 = raw_input("Enter a third character name: ")

n1 = raw_input("Enter a singular noun: ")
while n1[-2:] in nendings or n1[-1:] in nendings2 and n1[-2:] not in nendings3:
    print("That is a plural noun.")
    n1 = raw_input("Enter a SINGULAR noun: ")
n2 = raw_input("Enter a second singular noun: ")
while n2[-2:] in nendings or n2[-1:] in nendings2 and n2[-2:] not in nendings3:
    print("That is a plural noun.")
    n2 = raw_input("Enter a SINGULAR noun: ")

vendings = ["ed","id","ht"]
virregular = ["shot","crept","slept","threw","made","went","took","came","saw","knew","got","gave","found","thought","told","became","left","felt","put","brought","began","kept","held","wrote","stood","heard","let","meant","set","met","ran","paid","sat","spoke","lay","led","read","grew","lost","fell","sent","built","understood","drew","broke","spent","cut","rose","drove","bought","wore","chose"]

def wv():
    print("That is not a past-tense verb")
def wv2():
    print("That is not a present-tense verb")

v1 = raw_input("Enter a past-tense verb: ")
while v1[-2:] not in vendings and v1 not in virregular:
    wv()
    v1 = raw_input("Enter a PAST-TENSE verb: ")
v2 = raw_input("Enter a second past-tense verb: ")
while v2[-2:] not in vendings and v2 not in virregular:
    wv()
    v2 = raw_input("Enter a PAST-TENSE verb: ")
v3 = raw_input("Enter a third past-tense verb: ")
while v3[-2:] not in vendings and v3 not in virregular:
    wv()
    v3 = raw_input("Enter a PAST-TENSE verb: ")
v4 = raw_input("Enter a fourth past-tense verb: ")
while v4[-2:] not in vendings and v4 not in virregular:
    wv()
    v4 = raw_input("Enter a PAST-TENSE verb: ")
v5 = raw_input("Enter a present-tense verb: ")
while v5[-2:] in vendings or v5 in virregular:
    wv2()
    v5 = raw_input("Enter a PRESENT-TENSE verb: ")
v6 = raw_input("Enter a fifth past-tense verb: ")
while v6[-2:] not in vendings and v6 not in virregular:
    wv()
    v6 = raw_input("Enter a PAST-TENSE verb: ")

avendings = ["ly","ally","ily"]

def wav():
    print("That is not an adverb")

av1 = raw_input("Enter an adverb: ")
while av1[-2:] not in avendings and av1[-3:] not in avendings and av1[-4:] not in avendings:
    wav()
    av1 = raw_input("Enter an ADVERB: ")
av2 = raw_input("Enter a second adverb: ")
while av2[-2:] not in avendings and  av2[-3:] not in avendings and av2[-4:] not in avendings:
    wav()
    av2 = raw_input("Enter an ADVERB: ")

l1 = raw_input("Enter a location: ")
l2 = raw_input("Enter a second location: ")
l3 = raw_input("Enter a third location: ")

print  ch1,v1,"a",n1,"and",av1,v2,"it. However,",ch2," had a ",n2,"and",v3,"it",av2,"."

print "Somewhere else,",ch3,v4,"at",l1,"for about 3 hours.",ch2,"ended up bumping into",ch3,"at",l1,"and they decided to go to",l2,"to",v5,"."

print "Finally,",ch2,"and",ch3,"found",ch1,"again after their shenanigans. They all",v6,"towards",l3,"to end the day off."

