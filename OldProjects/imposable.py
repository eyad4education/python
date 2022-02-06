age = int(input("Entrer votre age: "))
gender = str(input("Femme ou Homme (F/H): "))
# Method 1
# if (age >= 20) and (gender == "Homme","homme","h","H") or (age >= 18 and age <= 35 and gender == "Femme","femme","f","F"):
#     print("L'ahbitant est imposable!")
# else:
#     print("L'ahbitant est ne pas imposable!")
# Method 2
f = age >= 18 and age <= 35 and gender == "Femme", "femme", "f", "F"
h = (age >= 20) and (gender == "Homme", "homme", "h", "H")
if f or h:
    print("L'ahbitant est imposable!")
else:
    print("L'ahbitant est ne pas imposable!")
