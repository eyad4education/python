def arithmetique(chaine):
    if chaine.find("+") != -1:
        x = int(chaine[:chaine.find("+")])
        y = int(chaine[chaine.find("+")+1:len(chaine)])
        return x+y
    elif chaine.find("-") != -1:
        x = int(chaine[:chaine.find("-")])
        y = int(chaine[chaine.find("-")+1:len(chaine)])
        return x-y
    elif chaine.find("*") != -1:
        x = int(chaine[:chaine.find("*")])
        y = int(chaine[chaine.find("*")+1:len(chaine)])
        return x*y
    elif chaine.find("/") != -1:
        x = int(chaine[:chaine.find("/")])
        y = int(chaine[chaine.find("/")+1:len(chaine)])
        return x/y
    else:
        return "Expression Inconnue"


ch = str(input("Donner l'expression: "))
print(arithmetique(ch))
