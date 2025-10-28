numar_1 = 7
numar_2 = 8

if numar_1 > numar_2:
    print ("Numarul 1 este mai mare decat numarul 2")
elif numar_1 < numar_2:
    print("Numarul 1 este mai mic decat numarul 2")
else:
    print('Numarul 1 este egal cu numarul 2')

    print('-----------------------')
    #verificam daca un numar e par sau impar
numar = 11
if numar % 2 == 0:
    print('Numarul este par')
else:
    print('Numarul este impar')
sir = "orice"

    #Verificam daca un sir de caractere este sau nu un gol
if len(sir) == 0:
    print("Sirul este gol")
else:
    print("Sirul nu este gol")

    #in operator ce verifica daca un element se afla intr-o colectie (sir de caractere,etc)
    #element in colectie    ->  returneaza true sau false
    #"@" in sir:
if "@" in sir:
    print("sirul contine @")
else:
    print("Sirul nu contine @")


    print ("-------------------")
#verificam daca sirul e palindrom


#numaram daca apare litera a de numar par de ori intr-un sir

sir = "Azi este o zi frumoasa"
numar_caractere_a = sir.count("a")
if numar_caractere_a % 2 == 0:
    print ("Litera a apare de numar par de ori")
else:
    print("Litera a apare de numar de impar de ori")

# structuri repetitive: for , while
# sintaxa:
# for element in colectie:
#    bloc de cod

# range (star, stop, pas) - genereaza o secventa de numere
# start - de unde incepem (inclusiv)
# stop - unde ne oprim (exclusiv)

for i in range(10):
    print (i, end=" ")
print()
# for sir de caractere
# metoda 1 -  parcurgere directa
# metoda 2 - parcurgere cu index
# nu am mai continuat


# exercitiu - numaram cate vocale sunt intr-un sir de caractere
sir = "Azi este o zi frumoasa"
vocale = "aeiouAEIOU"
numar_vocale = 0
for caracter in sir:
        if caracter in vocale:
            numar_vocale += 1
print(numar_vocale)

print("--------------")
# pe ce pozitii se afla in spatiile intr-un sir de caractere
sir = "Azi este o zi frumoasa"

for pozitie in range(len(sir)):
    if sir[pozitie] == "  ":                    #pozitie e indexul caracterului curent
        print("Spatiu gasit pe pozitia", pozitie)
