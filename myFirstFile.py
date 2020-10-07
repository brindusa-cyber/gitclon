print('Acesta este primul mesaj')
a = input("Apasa tasta r")  # raw_input in 2.7
print(a)
print("Ana are mere \n ion")
variabila1 = 1
Variabila2 = 2
Variabila3 = f"blabla {variabila1} labla {Variabila2}"
print(Variabila3)
Variabila4 = "Ana are {1} mere si {0} pere".format(variabila1, Variabila2)
print(Variabila4)
Variabila5 = "Mara are {1} mere si {1} prune    ".format(variabila1, Variabila2)
print(Variabila5)

print("Variabila4 =>>", type(Variabila4))
print("Variabila5 =>>", type(Variabila5))
Variabila6 = "blabla" + str(Variabila4) + "blablab"
print(Variabila6)

