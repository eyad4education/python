ad = str(input("Enter votre addresse email: "))
nm = ad[0:ad.find(".")]
ch = ad[ad.find("@")+1:len(ad)]
serv = ch[0:ch.find(".")]
print("Le nom est", nm, "et le nom de serveur est:", serv)