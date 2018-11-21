i = 2
while i < 5:
    liczba = input("Podaj swoja liczbe: ")
    pierwsza = liczba[0]
    ostatnia = liczba[-1:]


    if(liczba.isdigit()):
        print("Wprowadzona dana jest liczba.")
        print("Twoja liczba to: " + liczba)
        print("Piewsza cyfra Twojej liczby to: " + pierwsza)
        print("Ostatnia cyfra w Twojej liczbie to: " + ostatnia)

    else:
        print("Wprowadzaona dana nie jest liczba." + '\n' + "Sprobuj ponownie.")

