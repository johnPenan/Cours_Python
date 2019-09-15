annee = int(input("Veillez saisir une année: "))

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'année {} est bissextile".format(annee))    

else:
    print("L'année {} n'est pas bissextile".format(annee))





    