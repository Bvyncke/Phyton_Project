import keuzes
from login import login
login_check=login()

my_boardgames=keuzes.twee()
my_keuze=""
menu="""
1 - Boardgame toevoegen
2 - Spelletjes opnieuw ophalen
3 - Admin wachtwoord veranderen
4 - Script stoppen
"""

if login_check:
    while my_keuze !="4":
        print(menu)
        my_keuze=input("Geef je keuze ")
        if my_keuze=="1":
            keuzes.een(my_boardgames)

        elif my_keuze=="2":
            my_boardgames=keuzes.twee()

        elif my_keuze=="3":
            keuzes.drie()

else:
    print("te veel pogingen, het programma sluit af")
    exit()