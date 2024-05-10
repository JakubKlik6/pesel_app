# Importuje funkcję randint z modułu random
from random import randint

# Funkcja sprawdzająca poprawność formatu daty urodzenia
def sprawdz_format_daty(data_urodzenia):
    if len(data_urodzenia) != 10 or data_urodzenia[4] != '-' or data_urodzenia[7] != '-':
        return False
    return True

# Funkcja sprawdzająca poprawność wprowadzonej płci
def sprawdz_wartosc_plci(plec):
    if plec.lower() not in ['k', 'm']:
        return False
    return True

# Funkcja sprawdzająca poprawność formatu kodu miejsca urodzenia
def sprawdz_format_kodu_miejsca(miejsce_urodzenia):
    if not miejsce_urodzenia.isnumeric() or len(miejsce_urodzenia) != 4:
        return False
    return True

# Funkcja generująca numer PESEL
def generuj_pesel(data_urodzenia, plec, miejsce_urodzenia):
    if not sprawdz_format_daty(data_urodzenia):  # Sprawdzenie formatu daty urodzenia
        return "Błędny format daty urodzenia. Wprowadź datę w formacie RRRR-MM-DD."

    if not sprawdz_wartosc_plci(plec):  # Sprawdzenie wartości płci
        return "Błędna wartość płci. Wprowadź 'k' dla kobiety lub 'm' dla mężczyzny."

    if not sprawdz_format_kodu_miejsca(miejsce_urodzenia):  # Sprawdzenie formatu kodu miejsca urodzenia
        return "Błędny kod miejsca urodzenia. Wprowadź 4-cyfrowy numer."

    # Wyodrębnienie poszczególnych części daty urodzenia
    rok = int(data_urodzenia[:4])
    miesiac = int(data_urodzenia[5:7])
    dzien = int(data_urodzenia[8:])

    # Sprawdzenie poprawności daty urodzenia
    if miesiac < 1 or miesiac > 12 or dzien < 1 or dzien > 31:
        return "Błędna data urodzenia."

    # Sprawdzenie poprawności dnia w zależności od miesiąca
    if miesiac in [4, 6, 9, 11] and dzien > 30:
        return "Błędna data urodzenia."
    elif miesiac == 2:
        if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):  # Rok przestępny
            if dzien > 29:
                return "Błędna data urodzenia."
        elif dzien > 28:
            return "Błędna data urodzenia."

    # Generowanie pozostałych cyfr numeru PESEL
    miesiac_pesel = miesiac + (80 if rok >= 1800 and rok < 1900 else 0)  # Dopełnienie miesiąca dla lat 1800-1899
    rok_pesel = str(rok)[2:]
    dzien_pesel = str(dzien).zfill(2)
    miesiac_pesel = str(miesiac_pesel).zfill(2)
    miejsce_urodzenia_pesel = miejsce_urodzenia.zfill(4)
    cyfra_kontrolna = randint(0, 9)  # Losowanie cyfry kontrolnej

    # Utworzenie numeru PESEL
    pesel = rok_pesel + miesiac_pesel + dzien_pesel + miejsce_urodzenia_pesel + str(cyfra_kontrolna)

    # Ustalenie cyfry kontrolnej na podstawie algorytmu wag cyfr
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
    suma = sum(int(pesel[i]) * wagi[i] for i in range(11))
    cyfra_kontrolna = (10 - (suma % 10)) % 10

    # Aktualizacja numeru PESEL o poprawną cyfrę kontrolną
    pesel = pesel[:-1] + str(cyfra_kontrolna)

    return pesel

# Główna pętla programu
while True:
    # Wprowadzanie daty urodzenia i sprawdzanie jej poprawności
    while True:
        data_urodzenia = input("Podaj datę urodzenia (RRRR-MM-DD): ")
        if sprawdz_format_daty(data_urodzenia):
            break
        else:
            print("Błędny format daty urodzenia. Wprowadź datę w formacie RRRR-MM-DD.")

    # Wprowadzanie płci i sprawdzanie jej poprawności
    while True:
        plec = input("Podaj płeć (k/m): ")
        if sprawdz_wartosc_plci(plec):
            break
        else:
            print("Błędna wartość płci. Wprowadź 'k' dla kobiety lub 'm' dla mężczyzny.")

    # Wprowadzanie kodu miejsca urodzenia i sprawdzanie jego poprawności
    while True:
        miejsce_urodzenia = input("Podaj kod miejsca urodzenia (w tym przypadku możesz podać losowe cyfry jeżeli nie znasz swojego kodu urodzenia): ")
        if sprawdz_format_kodu_miejsca(miejsce_urodzenia):
            break
        else:
            print("Błędny kod miejsca urodzenia. Wprowadź 4-cyfrowy numer.")

    # Wywołanie funkcji generującej numer PESEL i wyświetlenie wyniku
    print("Wygenerowany numer PESEL:", generuj_pesel(data_urodzenia, plec, miejsce_urodzenia))
