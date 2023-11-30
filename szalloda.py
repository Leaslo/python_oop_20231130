from datetime import datetime

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=12000, szobaszam=szobaszam)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=18000, szobaszam=szobaszam)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class Szalloda:
    def __init__(self, nev, szobak, foglalasok):
        self.nev = nev
        self.szobak = szobak
        self.foglalasok = foglalasok

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                for foglalas in self.foglalasok:
                    if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                        return None

                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return foglalas

        return None

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            return True

        return False

    def foglalasok_listazasa(self):
        for foglalas in self.foglalasok:
            print(f"Szoba száma: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")

szobak = [EgyagyasSzoba(1), KetagyasSzoba(2), EgyagyasSzoba(3)]
foglalasok = [
    Foglalas(szobak[0], datetime(2023, 12, 15)),
    Foglalas(szobak[1], datetime(2023, 12, 15)),
    Foglalas(szobak[0], datetime(2023, 12, 16)),
    Foglalas(szobak[1], datetime(2023, 12, 18)),
    Foglalas(szobak[2], datetime(2023, 12, 18))
]
szalloda = Szalloda("OOP Szálloda", szobak, foglalasok)

while True:
    print("Válasszon az alábbi műveletek közül!:")
    print("1 - Szoba foglalása")
    print("2 - Foglalás lemondása")
    print("3 - Foglalások listázása")
    print("4 - Kilépés")

    valasztas = input("Kiválasztott menü: ")

    if valasztas == "1":
        szobaszam = int(input("Szobaszám(1-2-3): "))
        datum_str = input("Dátum (Év-Hónap-Nap): ")
        datum = datetime.strptime(datum_str, "%Y-%m-%d")

        foglalas = szalloda.foglalas(szobaszam, datum)

        if foglalas is None:
            print("Nem található ilyen szobaszám vagy a választott szoba ebben az időben foglalt!")
        else:
            print("Sikeres foglalás!")

    elif valasztas == "2":
        szobaszam = int(input("Szobaszám: "))
        datum_str = input("Dátum (yyyy-mm-dd): ")
        datum = datetime.strptime(datum_str, "%Y-%m-%d")

        foglalas = None
        for f in szalloda.foglalasok:
            if f.szoba.szobaszam == szobaszam and f.datum == datum:
                foglalas = f
                break

        if foglalas is None:
            print("Nem található ilyen foglalás.")
        else:
            if szalloda.lemondas(foglalas):
                print("Lemondás sikeres!")
            else:
                print("Lemondás sikertelen!")

    elif valasztas == "3":
        szalloda.foglalasok_listazasa()

    elif valasztas == "4":
        break

    else:
        print("Érvénytelen művelet.")