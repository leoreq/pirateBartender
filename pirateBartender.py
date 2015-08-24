import random
drinkStyle={}
clientDrink=[]
drinkName={}

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

piratestuff=['bucaneer','captain','chandler','bucaneer','corsair','coxswain']
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
    print ""
    print("Ill make ya some questions so that we can make err self a nice drink. Yarrrrr")
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
    #clientDrink=[]
    print ""
    print("Lets start mixn ya drinkss")
    for style in drinkStyle:
        if drinkStyle[style]=="YES":
            ingredient=random.choice(ingredients[style])
            clientDrink.append(ingredient)
            drinkName[style]=[ingredient]
            
def drinkNaming():
    """This function will name the drink"""
    #First the dominating taste
    domTaste=random.choice(drinkName.keys())
    #Piraty stuff
    piratyName=random.choice(piratestuff)
    #Dominant Drink
    VirginCheck=drinkName.get("strong",["virgin"])
    dList=["rum","whisky","gin","virgin"]
    for alcohol in dList:
        if alcohol in VirginCheck[0].split():
            dominantDrink=alcohol
    print ""
    print("And this drink will be known as ")
    print (" {} {} {}").format(domTaste,piratyName,dominantDrink)
    
def serveDrink():
    """This function will explain the drink"""
    print ""
    print (" Drink is Ready!!!")
    print("What youll be having is")
    for ingredient in clientDrink:
        print("A {}").format(ingredient)
    drinkNaming()
    clientDrink[:]=[]
    #drinkName={}
    
def anotherDrink():
    understandInput=True
    while understandInput:
        print ""
        another=raw_input("Want another Drink?")
        if (another.upper()=="YES") or (another.upper()=="NO"):
            if (another.upper()=="YES"):
                return(True)
            else:
                print(" N Joy your Drinkss and come again!!")
                return(False)     
        else: 
            print("Not CLear... Just Say YES or NO...so....")

def main():
    printPirate()
    anotherDrinkStatus=True
    while anotherDrinkStatus:
        askDrink()
        mixDrink()
        serveDrink()
        anotherDrinkStatus=anotherDrink()
        
if __name__ == '__main__':
    main()
        