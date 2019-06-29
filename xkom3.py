# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from time import sleep


imie = "Kamil"
nazwisko = "Niepowiem"
mail = "emailprojektowyselenium@kk.pl"
haslo_xkom = 'Qweasd123'

"""
Scenariusz:
Rejestracja nowego użytkownika w sklepie internetowym x-kom.pl wraz z wyrażeniem wszystkich zgód marketingowych.

Przypadki testowe:
I. Rejestracja nowego użytkownika z użyciem niezbędnych do rejestracji danych

Warunki wstępne:
1. Użytkownik którego dane są wprowadzane nie jest już zarejestrowany
2. Przeglądarka otwarta na stronie https://www.x-kom.pl/rejestracja/

Kroki:
1. Wpisz imię
2. Wpisz nazwisko
3. Wpisz adres e-mail
4. Wpisz hasło
5. Zaznacz pole typu checkbox "Akceptuję regulamin sklepu"
6. Kliknij "Załóż konto"
7. Przejdź do strony https://www.x-kom.pl/konto/zgody celem wyrażenia zgód marketingowych
8. Kliknij pole typu checkbox "Zaznacz wszystkie"
9. Kliknij "zapisz zmiany"


Oczekiwany rezultat:
1. Zarejestrowany użytkownik 
2. Wyrażone zgody marketingowe ( zaznaczone wszystkie checkboxy z zakładki "Twoje zgody")
"""

class XkomRejestracja(unittest.TestCase):
    """
    Scenariusz:
    Rejestracja nowego użytkownika w sklepie x-kom.pl
    """
    def setUp(self):
        """
        Warunki wstępne:
        1. Użytkownik nigdy nie był zarejestrowany
        2. Przeglądarka otwarta na stronie https://www.x-kom.pl/rejestracja/
        """
        #profile = webdriver.FirefoxProfile()
        #profile.set_preference("geo.enabled", False)
        #self.driver = webdriver.Firefox(firefox_profile=profile)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.x-kom.pl/rejestracja/")

    def zamkniecie(self):
        """
        Zakończenie
        """
        self.driver.quit()

    def test_rejestracja_xkom(self):
        """
        Przypadek testowy:
        I. Rejestracja nowego użytkownika w sklepie x-kom.pl oraz wyrażenie wszystkich zgód marketingowych

        Kroki:
        """
        driver = self.driver

        # 1. Wpisz imię
        name_field = driver.find_element_by_id("firstName")
        name_field.send_keys(imie)
        sleep(2)
        # 2. Wpisz nazwisko
        surname_field = driver.find_element_by_id('lastName')
        surname_field.send_keys(nazwisko)
        sleep(2)
        # 3. Wpisz email
        #name_field.click()
        email = driver.find_element_by_id('email')
        email.send_keys(mail)
        sleep(2)
        # 4. Wpisz hasło
        haslo = driver.find_element_by_id('password')
        haslo.send_keys(haslo_xkom)
        sleep(2)
        # 5. Zaakceptuj regulamin sklepu
        regulamin = driver.find_element_by_id('termsOfUseAcceptation')
        regulamin.click()
        sleep(2)
        # 6. Kliknij założenie nowego konta
        zaloz_konto = driver.find_element_by_xpath ('//button[@type="submit"]')
        zaloz_konto.click()
        sleep(2)
        # 7. Idź do strony logowania
        self.driver.get("https://www.x-kom.pl/konto/zgody")
        # 8. Wyraź zgodę
        zgoda = driver.find_element_by_id('checkAllAgreements')
        zgoda.click()
        sleep(2)
        # 9. Zapisz zmiany
        zapisz_zmiany = driver.find_element_by_id('saveAccountAgreements')
        zapisz_zmiany.click()
        sleep(10)


        #### Oczekiwany rezultat: ####
        #Wyświetlenie informacji o pozytywnej rejestracji użytkownika
        #Odznaczenie wszystkich zgód marketingowych


if __name__ == "__main__":
    unittest.main(verbosity=2)