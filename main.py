from classes.Auto import *
from classes.Szemelyauto import *
from classes.Teherauto import *
from classes.Autokolcsonzo import *
from classes.Berles import *

autokolcsonzo = Autokolcsonzo()

berles1 = Berles("2025-05-13","Mihály")
berles2 = Berles("2025-05-03","János")
berles3 = Berles("2025-04-10","Krisztina")
berles4 = Berles("2025-05-25","Dóra")

tesztauto1 = Teherauto("XYZ-123", "40000")
tesztauto1.berlesek.append(berles1)
autokolcsonzo.autok.append(tesztauto1)

tesztauto2 = Teherauto("ABC-123", "30000")
tesztauto2.berlesek.append(berles2)
autokolcsonzo.autok.append(tesztauto2)

tesztauto3 = Szemelyauto("JKL-1678", "10000")
tesztauto3.berlesek.append(berles3)
tesztauto3.berlesek.append(berles4)
autokolcsonzo.autok.append(tesztauto3)


while True:
    print("Válasszon az alábbiak közül: \n1. Autó bérlése \n2. Bérlés lemondása \n3. Bérlések listázása \n4. Kilépés")
    valasz = input()
    print("\n")
    if valasz == "1":
        autokolcsonzo.auto_berlese()
    elif valasz == "2":
        autokolcsonzo.auto_berles_lemondasa()
    elif valasz == "3":
        autokolcsonzo.autok_berlesek_listazasa()
    elif valasz == "4":
        break
    else:
        print("Kérjük próbálja újra!")
        continue
