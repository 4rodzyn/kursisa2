rok = int(input("Podaj rok: "))

if(rok % 4 == 0 and rok % 100 != 0):
    print("Rok jest przestepny.")
elif(rok % 400 == 0):
    print("Rok jest przestepny.")
else:
    print("Rok nie jest przestepny.")
