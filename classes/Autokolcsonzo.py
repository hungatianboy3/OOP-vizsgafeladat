from classes.Berles import *
class Autokolcsonzo():
    kolcsonzo_neve = "Lajos & Ágnes Autókölcsönző Corporation"

    def __init__(self):
        self.autok = []

    def autok_berlesek_listazasa(self):
        for auto in self.autok:
            print(f"{auto.rendszam} {auto.berleti_dij}")
            for berles in auto.berlesek:
                print(f"{berles.datum} {berles.nev}")
            print("\n")

    def auto_berlese(self):
        index = 0
        print(">>>A bérelni kívánt autó sorszámát írja be a bérléshez.<<<")
        print("Sorszám  Típus  Rendszám  Bérleti díj/Nap")
        
        for auto in self.autok:
            print(f"{index}.    {auto.tipus}    {auto.rendszam}    {auto.berleti_dij}")
            index += 1

        while True:
            auto_kival = int(input(f"Válassza ki a bérelendő autó sorszámát 0.-{len(self.autok) - 1}.: "))
            if auto_kival <= len(self.autok) - 1 and auto_kival > -1:
                berlo_nev = input("Adja meg a bérlő nevét: ")
                while True:
                    berlesek_list = []
                    ber_datum = input("Adja meg a bérlés dátumát ebben a formátumban: 2005-04-29")
                    if len(ber_datum) == 10 and ber_datum.count("-") == 2:
                        
                        for berles in self.autok[auto_kival].berlesek:
                            berlesek_list.append(berles.datum)
                        print(berlesek_list)
                        
                        if ber_datum not in berlesek_list:
                            self.autok[auto_kival].berlesek.append(Berles(ber_datum,berlo_nev))
                            break
                        else:
                            print("Ez az autó erre a napra már nem bérelhető, válasszon másik napot!")
                    else:
                        print("Rossz formátum, próbálja újra!")
                break
            else:
                print("Ilyen sorszám nem létezik, próbálja újra!")


    def auto_berles_lemondasa(self):
        index_auto = 0
        
        print(">>>A lemondani kívánt autó sorszámát írja be a bérléshez.<<<")
        print("Sorszám  Típus  Rendszám  Bérleti díj/Nap")
        auto_berles_lemondas_lista = []
        
        for auto in self.autok:
            print(f"{index_auto}.    {auto.tipus}    {auto.rendszam}    {auto.berleti_dij}")
            index_berles = 0
            for berles in auto.berlesek:
                print(f"    {index_berles}. {berles.datum} {berles.nev}")
                index_berles += 1
            auto_berles_lemondas_lista.append([index_auto, auto])
            index_auto+= 1

                

        while True:
            auto_kival = int(input(f"Adja meg az autó sorszámát 0.-{len(auto_berles_lemondas_lista) - 1}.: "))
            berles_kival = int(input("Adja meg a lemondani kívánt bérlés sorszámát: "))
            if auto_kival <= len(auto_berles_lemondas_lista) - 1 and auto_kival > -1:
                auto_berles_lemondas_lista[auto_kival][1].berlesek.pop(berles_kival)
                break
            else:
                print("Ilyen sorszám nem létezik, próbálja újra!")