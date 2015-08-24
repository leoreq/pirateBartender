import random
drinkStyle={}
clientDrink=[]
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}
logo=[" The Pirate Bartender Welcomes Yall.",
 "||-.,.,.,.,,.,.,...-' ;",
 "||     _          _    |",
 "||   _( )        ( )_  | ",
 "||  (_  \ /\\//\ / ._) |",
 "||    '\ (  )(  ) /    |",
 "||       \\//\\//      |",
 "||        .))((.       |",
 "||      _/ |||| \_     |",
 "||    ('  /....\  ')   |" ,
 "||     '(_)    (_)'    |" ,
 "||-.,.,.,.,.,.,.,.,..-'" ,
 "||   ",
 "||  ",
 "||   -",
 "||  ",
 "*"]
def printPirate():
    for line in logo:
        print(line)
        
def askDrink():
    """This funciton will ask for style of drink, and store answer"""  
    
    print("Answer True or False to the following questions so that we can make err self a drink. Yarrrrr")
    for style in questions:
        isBoolean=True
        while isBoolean:
            clientPreference=raw_input(questions[style]+"[yes/no]")
            if (clientPreference.upper()=="YES") or (clientPreference.upper()=="NO"):
                drinkStyle[style]=clientPreference.upper()
                print("Noted")
                isBoolean=False
            else: 
                print("Not CLear... Just Say YES or NO...so....")
                print(type(clientPreference))


def mixDrink():
    """This funciton will take the drinking style , use the taste key to access ingredient dictionary and randomly mix the ingredientes for the coctail"""
    print("Lets start mixn ya drinkss")
    for style in drinkStyle:
        if drinkStyle[style]=="YES":
            ingredient=random.choice(ingredients[style])
            clientDrink.append(ingredient)

def serveDrink():
    """This function will explain the drink"""
    print (" Drink is Ready.")
    print(clientDrink)
    
def anotherDrink():
    understandInput=True
    while understandInput:
        another=raw_input("Want another Drink?")
        if (another.upper()=="YES") or (another.upper()=="NO"):
            if (another.upper()=="YES"):
                return(True)
            else:
                print(" N Joy your Drinkss and come again!!")
                return(False)     
        else: 
            print("Not CLear... Just Say YES or NO...so....")
               
if __name__ == '__main__':
    printPirate()
    anotherDrinkStatus=True
    while anotherDrinkStatus:
        askDrink()
        mixDrink()
        serveDrink()
        anotherDrinkStatus=anotherDrink()
        