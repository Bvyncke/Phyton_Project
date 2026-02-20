import ast
import re

# Lijst met spelletjes ophalen
def een(games):
    my_exit=False
    ophalen=input("wil je eerst de lijst van boardgames opnieuw ophalen? j/n")
    if ophalen.lower()=="j":
        twee()
    while not my_exit:
        my_exit=True
        my_genre=input("geef het genre ")
        if my_genre !="actie"   and my_genre !="avontuur":
            print("Het genre kan enkel actie/avontuur zijn!")
            my_exit=False


    while my_exit:
        my_exit=False
        my_uitgever= input("geef de uitgever ")
        if my_uitgever != "Mattel" and my_uitgever != "Hasbro":
            print("De uitgever kan enkel Hasbro of Mattel zijn !")
            my_exit=True

    while not my_exit:
        my_exit=True
        try:
            aantal_spelers=int(input("Geef het aantal spelers "))
            if aantal_spelers<1 or aantal_spelers>9:
                print("Het aantal spelers moet tussen 0 en 9 liggen ")
                my_exit=False
        except ValueError:
            print("Dit is geen getal!")
            my_exit=False

    while my_exit:
        my_exit=False
        my_naam=input("Geef een unieke naam voor het spel")
        for game in games:
            if game["naam"] == my_naam:
                print("Deze naam bestaat al")
                my_exit=True
    my_file=open(r"C:\Users\vynck\Desktop\spelletjes.txt","a")
    my_file.write(str({"naam":my_naam,"genre":my_genre,"uitgever":my_uitgever,"spelers":aantal_spelers})+"\n")
    my_file.close()

def twee ():
    my_list=[]
    my_page=open(r"C:\Users\vynck\Desktop\spelletjes.txt","r")
    my_games=my_page.readlines()
    my_page.close()

    for game in my_games:
        game=game.strip()
        my_list.append(ast.literal_eval(game))
    return my_list

# Wachtwoord wijzigen

def drie():
    check=False
    while not check:
        check=True
        nieuw_ww=input("geef een nieuw wachtwoord")
        patern=re.compile(r"\d")
        matches=patern.findall(nieuw_ww)
        if len(matches)==0:
            print("er zit geen cijfer in")
            check=False
        patern=re.compile(r'\w[a-z]')
        matches=patern.findall(nieuw_ww)
        if len(matches)==0:
            print("er zit geen kleine letter in")
            check=False
        patern = re.compile(r'\w[A-Z]')
        matches = patern.findall(nieuw_ww)
        if len(matches) == 0:
            print("er zit geen grote letter in")
            check = False
    my_file=open(r"C:\Users\vynck\Desktop\adminwachtwoord.txt","w")
    my_file.write(nieuw_ww)
    my_file.close()






