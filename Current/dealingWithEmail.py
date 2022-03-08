adress = str(input("Donner votre email: "))
ad = adress[0:adress.find('@')]
ad2 = adress[adress.find('@')+1:len(adress)]
domain = ad2[0:ad2.find('.')]
host = ad2[ad2.find('.')+1:len(ad2)]
print(ad)
print(domain)
print(host)