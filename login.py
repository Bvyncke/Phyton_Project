def login():
    myfile=open(r"C:\Users\vynck\Desktop\adminwachtwoord.txt","r")
    my_passwd=myfile.readline()
    myfile.close()
    my_chances=0
    print(my_passwd)
    while my_chances<5:
        user = input("Geef de username ")
        ww=input("Geef het wachtwoord ")


        if user=="Phyton" and  ww== my_passwd:
            return True
        else:
            my_chances +=1
            print(f"De logingegevens zijn fout. Kans {my_chances}/5")
    return False

