

def faren():
    """Funkcja przelicza podane przez uzytkownika stopnie Celsjusza na stopie w Farenheitach."""
    x = input("Podaj stopnie Celsjusza: ")
    farenheity = 32 + 1.8 * float(x)
    print("Wzor na obliczenie temperatury Farenheita to: Farenheity = 32 + 1.8 * " + x + "(Temperatura  podana w Celsjuszach)")
    print("Twoja temperatura w Farenheitach to: " + str(farenheity))

def parzystosc():
    """Funkcja sprawdza czy podana liczba jest parzysta czy nie"""
    a = int(input("Wprowadz liczbe: "))

    if (a % 2 == 0):
        print("Liczba jest parzysta.")
    else:
        print("Liczba nie jest parzysta.")

def prostokat():
    """Funkcja rysuje prostokat o podanych przez uzytkownika wymiarach"""
    a = int(input("Podaj dlugosc boku a: "))
    b = int(input("Podaj dlugosc boku b: "))

    print(("+" + a * "-" + "+" + "\n") + ("|" + " " * a + "|" + '\n') * b + ("+" + a * "-" + "+"))

def podzielnosc():
    """Funkcja sprawdza czy liczba jest podzielna przez 3, 5 lub 7."""
    a = int(input("Wprowadz liczbe: "))

    if (a % 3 == 0):
        print("Liczba jest podzielna przez 3.")
    elif (a % 5 == 0):
        print("Liczba jest podzielna przez 5.")
    elif (a % 7 == 0):
        print("Liczba jest podzielna przez 7.")

def pole_kola():
    """Funkcja oblicza pole kola, o podanym przez uzytkownika promieniu."""
    import math
    r = float(input("Podaj promien kola: "))
    rkwadrat = r ** 2
    pi = math.pi

    pole_kola = pi * r ** 2

    print("Wzor na pole kola to P= pi * r^2.")
    print("Wlaczajac Twoje dane: P= " + str(pi) + " * " + str(rkwadrat))
    print("Pole Twojego kola to: " + str(pole_kola))

def przestepnosc():
    """Funkcja sprawdza czy podany rok jest rokiem przestepnym"""
    rok = int(input("Podaj rok: "))

    if(rok % 4 == 0 and rok % 100 != 0):
        print("Rok jest przestepny.")
    elif(rok % 400 == 0):
        print("Rok jest przestepny.")
    else:
        print("Rok nie jest przestepny.")

def liczby():
    """Funkcja wyswietla pierwsza i ostaatnia cyfre z wprowadzonego ciagu liczb"""

    liczba = input("Podaj swoja liczbe: ")
    pierwsza = liczba[0]
    ostatnia = liczba[-1:]

    if (liczba.isdigit()):
        print("Wprowadzona dana jest liczba.")
        print("Twoja liczba to: " + liczba)
        print("Piewsza cyfra Twojej liczby to: " + pierwsza)
        print("Ostatnia cyfra w Twojej liczbie to: " + ostatnia)

    else:
        print("Wprowadzaona dana nie jest liczba." + '\n' + "Sprobuj ponownie.")

def piramida():
    """funkcja rysuej piramide o okreslonej wartosci uzywajac znaku #"""
    n = input("Podaj wielkosc piramidy:")
    n = int(n)
    j = i = 1
    m = n

    while (i < n + 1):
        while (j):
            print(m * " " + j * "#")
            m = m - 1
            j = j + 2
            break
        i = i + 1

def cels():
    """Funkcja przelicza podane przez uzytkownika stopnie Celsjusza na stopie w Farenheitach."""
    x = input("Podaj stopnie Farenheita: ")
    celsjusz = 5/9 * (float(x) - 32)
    print("Wzor na obliczenie temperatury Farenheita to: Celsjusze = 5/9 * " + "(Temperatura  podana w Farenheitach - 32)")
    print("Twoja temperatura w Celsjuszach to: " + str(celsjusz))


def print_menu():
    print(30 * "-", "MENU", 30 * "-")
    print("1.Stopnie C->F.")
    print("2.Stopnie F->C.")
    print("3.Czy liczba jest parzysta?")
    print("4.Rysuj prostokat.")
    print("5.Czy liczba jest podzielna przez 3, 5 lub 7?")
    print("6.Pole kola.")
    print("7.Czy rok jest przestepny?")
    print("8.Pierwsza i ostatniacyfra ciagu.")
    print("9.Piramida")
    print("0.Exit")
    print(67 * "-")


loop = True

while loop:
    print_menu()
    choice = input("Wybierz program [0-9]: ")
    if choice == "1":
        faren()
    elif choice == "2":
        cels()
    elif choice == "3":
        parzystosc()
    elif choice == "4":
        prostokat()
    elif choice == "5":
        podzielnosc()
    elif choice == "6":
        pole_kola()
    elif choice == "7":
        przestepnosc()
    elif choice == "8":
        liczby()
    elif choice == "9":
        piramida()
    elif choice == "0":
        print("Dzieki za skorzystanie z programu :)")
        loop = False
    else:
        input("Niepoprawny wybor, sprobuj ponownie.")