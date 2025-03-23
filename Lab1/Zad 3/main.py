import osoba
if __name__ == "__main__":
    m = osoba.Manager("Bartek", "Kowalski", 36, "Manager IT", 7000)
    p1 = osoba.Pracownik("Jan", "Nowak", 25, "Programista", 2500)
    p2 = osoba.Pracownik("Witolda", "Zielinski", 55, "Tester", 5000)
    m.dodaj_do_zespolu(p1)
    m.dodaj_do_zespolu(p2)
    print(m.przedstaw_sie())
