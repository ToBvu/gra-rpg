import climage 
import sys, time
from colorama import Back, Style, init
from random import randint, choice

# a = 0.02
# b = 0.05
# c = 0.01
# d = 0.03
# e = 0.15
a = 0.02
b = 0.05
c = 0.01
d = 0.03
e = 0.15

RESET = '\033[0m'
BLACK = '\033[30m'
RED = '\033[38;2;255;0;0m' 
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033['
CYAN = '\033[36m'
WHITE = '\033[37m'
BROWN = '\033[33;2m'
ORANGE = '\033[38;2;255;165;0m'

napis1 = """            PPPPP    OOOO   TTTTTT  WW   WW   OOOO   RRRRR   MM   MM   AAAA   NN  NN  IIIIII   AAAA  
            PP  P   OO  OO    TT    WW   WW  OO  OO  RR  RR  MMM  MM  AA  AA  NNN NN    II    AA  AA 
            PPPPP   OO  OO    TT    WW W WW  OO  OO  RRRRR   MM M MM  AAAAAA  NN NNN    II    AAAAAA 
            PP      OO  OO    TT    WWWWWWW  OO  OO  RR  RR  MM   MM  AA  AA  NN  NN    II    AA  AA 
            PP       OOOO     TT     WW WW    OOOO   RR  RR  MM   MM  AA  AA  NN  NN  IIIIII  AA  AA """

def Slow_text(a, b):
    for char in a:
        sys.stdout.write(char)
        sys.stdout.flush()
        try:
            time.sleep(float(b))
        except ValueError:
            time.sleep(0.01)
    return a, b

#====================================================INTRO DO GRY============================================================================================================



Slow_text(RESET + ("="*100), a)
print(" ", end ="\n")
intro = "Witaj w grze:   "
Slow_text(intro, e)
print(" ", end ="\n")
Slow_text(CYAN + napis1 + RESET, 0.005)#<0.005=================================================================================================================================================
print(" ", end ="\n")
Slow_text(("="*100), a)
print(" ", end ="\n")
time.sleep(3) #<3===========================================================================================================================================================

#---------Atrybuty bohaterów-----------------------------------------------------------------------------------------------------------------------------------------------------------
mana = 0
hp = 0 
rasa = "brak"
textC = "Nazywam się Aleksander, a moje dzieciństwo upłynęło w spokojnej wiosce. Już od najwcześniejszych lat przejawiałem wyjątkową odwagę i zapał do nauki. Gdy nasza wioska padła ofiarą ataku bandytów, postanowiłem stanąć na czele obrony. Teraz, jako bohater zyskujący szacunek mieszkańców, ruszam w podróż, by zdobyć nowe doświadczenia i obronić świat przed ciemnymi siłami."
textE = "Jestem Elara, jestem młodą elfką o niezwykłych zdolnościach magicznych, urodzoną w elfiej osadzie otoczonej lasem. Od najwcześniejszych lat fascynowały mnie tajemnice natury i magii. Kiedy starożytne drzewo chroniące naszą osadę zaczęło słabnąć, postanowiłam wyruszyć w podróż w poszukiwaniu mocy przywracających równowagę. Moje cele to ochrona lasu i przywrócenie blasku elfickiej magii."
textM = "Nazywam się Aric, zaklinacz ognia i czarów, pochodzący z rodu potężnych magów. Moi rodzice, obrońcy królestwa, przekazali mi tajniki magii. Po tragicznym zdarzeniu, w wyniku którego straciłem bliskich, postanowiłem zdobyć jeszcze większą moc. Teraz, podróżując przez krainy, dążę do opanowania najpotężniejszych czarów, aby stawić czoła ciemnym siłom zagrażającym światu."
textB = "Jestem Gorn, jestem potężnym barbarzyńcą z górzystych regionów. Moje plemię żyje w symbiozie z surową naturą, a ja zawsze byłem uznawany za jednego z najdzielniejszych wojowników. Po odniesieniu zwycięstwa nad groźnym potworem, postanowiłem opuścić swoje plemię i podążyć ścieżką samodoskonalenia, by stawić czoła jeszcze większym wyzwaniom."
textN = "Jestem Frodo Niziołek, jestem zakapturzony i zwinny, urodziłem się w miejskiej osadzie otoczonej murami. Moja zręczność i talent do unikania niebezpieczeństw sprawiły, że szybko stałem się niezastąpionym kurierem w labiryncie wąskich uliczek miasta. Gdy tajemnicze zdarzenia zagroziły bezpieczeństwu miasta, postanowiłem opuścić swoje ukochane uliczki, aby odnaleźć źródło zagrożenia i ocalić swoje rodzinne miasto."
textO = "Nazywam się Gruk, jestem potężnym orkiem o twardym charakterze, wychowanym w plemieniu orków, znanym ze swojego nieustraszonego wojowniczego ducha. Zawsze marzyłem o wielkich bohaterskich czynach, które przyniosą sławę mojemu plemieniu. Po odkryciu starożytnej przepowiedni przewidującej nadchodzące niebezpieczeństwo, postanowiłem opuścić moje plemię i wyruszyć w podróż, by stać się bohaterem, który ocali świat przed zagładą." 
 


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def czlowiek():
    return 40, 100

def elf():
    return 60, 80

def mag():
    return 80, 60

def barbarzynca():
    return 20, 120

def niziolek():
    return 40, 100

def ork():
    return 0, 140

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------GŁÓWNA FUNKCJA------------------------------------------------------------------------------------------------------------------------------------------

text1 = "Rasy do wyboru:" + RESET
Slow_text(text1, b)
print(" ", end="\n")
text2 = WHITE + "Człowiek - waleczny ale to nie zawsze wystarczy" + RESET
Slow_text(text2, b)
print(" ", end="\n")
text3 = GREEN + "Elf - duże uszy pomocne w rzucaniu uroków" + RESET
Slow_text(text3, b)
print(" ", end="\n")
text4 = BLUE + "Mag - Czary mary dużo many" + RESET
Slow_text(text4, b)
print(" ", end="\n")
text5 = ORANGE + "Barbarzyńca - Zręcznie opróżnia kieszenie w mieście" + RESET
Slow_text(text5, b)
print(" ", end="\n")
Slow_text(MAGENTA + "NNiziołek - Tak niski że przejdzie przez każdą dziurę" + RESET, b)
print(" ", end="\n")
text7 = RED + "Ork - głupi, ale przetrwałby uderzenie pudziana" + RESET
Slow_text(text7, b)
print(" ", end="\n")
text8 = "Którą rasę wybierasz podróżniku?" + RESET
Slow_text(text8, b)
print(" ", end="\n")
rasa = input("Podaj rasę Bohatera: ").upper()
while True: 
    if rasa == "CZŁOWIEK" or rasa == "CZLOWIEK":
        mana, hp,  = czlowiek()
        Slow_text(textC, d)
        break
    elif rasa == "ELF":
        mana, hp = elf()
        Slow_text(textE, d)
        break
    elif rasa == "MAG":
        mana, hp = mag()
        Slow_text(textM, d)
        break
    elif rasa == "BARBARZYŃCA" or rasa == "BARBARZYNCA":
        mana, hp = barbarzynca()
        Slow_text(textB, d)
        break
    elif rasa == "NIZIOŁEK" or rasa == "NIZIOLEK":
        mana, hp = niziolek()
        Slow_text(textN, d)
        break
    elif rasa == "ORK":
        mana, hp = ork()
        Slow_text(textO, d)
        break
    else:
        print("Nieprawidłowa rasa. Spróbuj ponownie.")
        rasa = input("Podaj rasę Bohatera: ").upper()
print(" ", end = "\n")
Slow_text(GREEN + "Naciśnij" + YELLOW + " p" + GREEN +  ", aby zacząć rozgrywkę" + RESET, d)
print(" ", end="\n")
while True:
    c = input()
    if c == "p":
        break
    else:
        continue




print("Posiadasz: " + BLUE + str(mana) + " many" + RESET + " i " + RED + str(hp) + " życia" + RESET + ".")
Slow_text("Wylądowałeś w niebezpiecznych lochach, gdzie znajdziesz" + RED + " potwory" + RESET + ", ale też i " + BLUE + "potiony" + RESET + ", które dodają" + BLUE + " many." + RESET, d)
print(" ", end = "\n")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Start Gry
def zwykly_atak():
    a = randint(2, 10)
    return a
def MAGIC():
    global mana
    if mana < 20:
        Slow_text(RED + "Nie mogę wykonać tego ataku, mam za mało many" + RESET, d)
        return 0
    else:
        mana -= 20
        a = randint(10, 25)
        Slow_text(BLUE + "Magiczny" + GREEN + " atak wykonany!" + CYAN + " -20 many " + RESET, d)
        print(" ", end="\n")
        print("Posiadasz: " + BLUE + str(mana) + " many" + RESET + " i " + RED + str(hp) + " życia" + RESET + ".")
        return a
def Goblin_hp():
    hp = randint(5, 15)
    return hp
def Goblin_atak():
    atak = randint(1, 5)
    return atak
def Wiedzma_atak():
    atak = randint(5, 10)
    return atak
def Wiedzma_hp():
    hp = randint(15,20)
    return hp
def Wampir_atak():
    atak = randint(10, 15)
    return atak
def Wampir_hp():
    hp = randint(20, 25)
    return hp
def Boss_hp():
    hp = randint(40, 50)
    return hp
def Boss_atak():
    atak = randint(20, 25)
    return atak
def random_oponent():
    a = randint(1, 3)
    oponent = None
    if a == 1:
        oponent = "Wampir"
    elif a == 2:
        oponent = "Wiedźma"
    elif a == 3:
        oponent = "Goblin"
    return oponent


def walka_boss():
    global atak_oponenta
    global hp_oponenta
    global hp
    atak_oponenta = Boss_atak()
    hp_oponenta = Boss_hp()

    Slow_text(GREEN + "Walczysz teraz z " + RED + "Boss'em" + GREEN + "!" + RESET, d)
    print(" ", end="\n")
    while hp_oponenta > 0 and hp > 0:
        Slow_text(GREEN + "Zwykły atak - " + YELLOW + "z" + GREEN + ", specjalny atak -" + BLUE + " x" + RESET, c)
        print(" ", end="\n")
        a = input()

        if a == "z":
            obrazenia = zwykly_atak()
            hp_oponenta -= obrazenia 
            Slow_text(GREEN + "Użyłeś zwykłego ataku i zadałeś " + RED + str(obrazenia) + GREEN + " obrażeń." + RESET, c)
            print(" ", end="\n")
        elif a == "x":
            obrazenia = MAGIC()
            hp_oponenta -= obrazenia
            print(" ", end="\n")  
            Slow_text(GREEN + "Użyłeś magicznego ataku i zadałeś " + RED + str(obrazenia) + GREEN + " obrażeń." + RESET, c)
            print(" ", end="\n")
        else:
            print(RED + "Nieprawidłowy atak. Wybierz ponownie." + RESET, c)
            print(" ", end="\n")
            continue  

        if hp_oponenta <= 0:
            Slow_text(GREEN + "Brawo! Zabiłeś " + RED + "Boss'a" + GREEN + "!" + RESET, c)
            print(" ", end="\n")
            Slow_text(MAGENTA + "Przeszedłeś grę..." + RESET, 0.1)
            break
        else:
            Slow_text(RED + "Boss" + " zaatakował!" + RESET, c)
            hp -= atak_oponenta
            print(" ", end="\n")
            Slow_text(RED + "Boss" + GREEN + " zadał ci " + RED + str(atak_oponenta) + GREEN + " obrażeń." + RESET, c)
            print(" ", end="\n")
            Slow_text(GREEN + "Zostało ci " + RED + str(hp) + GREEN + " hp." + RESET, c)
            print(" ", end="\n")

        if hp <= 0:
            dead()
            break



def start():
    print(" ", end = "\n")
    Slow_text(RED + "Trafiłeś na pole startowe! Przegrałeś! :(" + RESET, d)
    print(" ", end = "\n")
    time.sleep(3)

def dead():
    print(" ", end = "\n")
    Slow_text(RED + "Game Over! Zginąłeś!" + RESET, d)
    print(" ", end = "\n")
    time.sleep(3)
    
    

def pokoj123():
    while True:
        Slow_text(YELLOW + "Trafiłeś do pokoju z trojgiem drzwi " + GREEN + "wybierz jedno z nich. " + YELLOW + "(1 lub 2 lub 3)" + RESET ,d)
        print(" ", end = "\n")
        y = input()
        if y == "1":
            potka()
            walka()
            start()
            break
        elif y == "2":
            lewo_prawo_przod()
            if x == "d":
                walka()
                przod()
                walka()
                przod()
                start()
                break
            elif x == "w":
                przod()
                start()
                break
            elif x == "a":
                print(" ", end="\n")
                potka()
                prawo()
                przod()
                walka_boss()
                break
        
        elif y == "3":
            potka()
            start()
            break
        else:
            print(" ", end = "\n")
            Slow_text(RED + "Nie ma takiego pokoju" + RESET, c)
            print(" ", end="\n")
            continue

def pokoj12():
    print(" ", end = "\n")
    while True:
        Slow_text(YELLOW + "Trafiłeś do pokoju z dwojgiem drzwi! " + GREEN + "wybierz jedno z nich. " + YELLOW + "(1 lub 2)" + RESET ,d)
        print(" ", end = "\n")
        print(" ", end = "\n")
        y = input()
        if y == "1":
            prosto_prawo()
            print(" ", end = "\n")
            if x == "d":
                start()
                break
            elif x == "w":
                prosto_prawo()
                if x == "w":
                    walka()
                    przod()
                    start()
                    break
                elif x == "d":
                    potka()
                    przod()
                    walka()
                    przod()
                    walka_boss()
                    break
        elif y == "2":
            przod()
            prosto_prawo()
            if x == "d":
                lewo()
                start()
                break
            elif x == "w":
                potka()
                przod()
                walka_boss()
                break
        else:
                Slow_text(RED + "Nie ma takiego pokoju" + RESET, c)
                print(" ", end="\n")
                continue
        







def walka():
    oponent =  random_oponent()
    global atak_oponenta
    global hp_oponenta
    global hp

    if oponent == "Wiedźma":
        hp_oponenta = Wiedzma_hp()
        atak_oponenta = Wiedzma_atak()
    elif oponent == "Wampir":
        hp_oponenta = Wampir_hp()
        atak_oponenta = Wampir_atak()
    elif oponent == "Goblin":
        hp_oponenta = Goblin_hp()
        atak_oponenta = Goblin_atak()

    Slow_text(GREEN + "Walczysz teraz z " + RED + oponent + GREEN + "!" + RESET, d)
    print(" ", end="\n")
    while hp_oponenta > 0 and hp > 0:
        Slow_text(GREEN + "Zwykły atak - " + YELLOW + "z" + GREEN + ", specjalny atak -" + BLUE + " x" + RESET, c)
        print(" ", end="\n")
        a = input()

        if a == "z":
            obrazenia = zwykly_atak()
            hp_oponenta -= obrazenia 
            Slow_text(GREEN + "Użyłeś zwykłego ataku i zadałeś " + RED + str(obrazenia) + GREEN + " obrażeń." + RESET, c)
            print(" ", end="\n")
        elif a == "x":
            obrazenia = MAGIC()
            hp_oponenta -= obrazenia
            print(" ", end="\n")  
            Slow_text(GREEN + "Użyłeś magicznego ataku i zadałeś " + RED + str(obrazenia) + GREEN + " obrażeń." + RESET, c)
            print(" ", end="\n")
        else:
            print(RED + "Nieprawidłowy atak. Wybierz ponownie." + RESET, c)
            print(" ", end="\n")
            continue  

        if hp_oponenta <= 0:
            Slow_text(GREEN + "Brawo! Zabiłeś " + RED + oponent + GREEN + "!" + RESET, c)
            break
        else:
            Slow_text(RED + oponent + " zaatakował!" + RESET, c)
            hp -= atak_oponenta
            print(" ", end="\n")
            Slow_text(RED + oponent + GREEN + " zadał ci " + RED + str(atak_oponenta) + GREEN + " obrażeń." + RESET, c)
            print(" ", end="\n")
            Slow_text(GREEN + "Zostało ci " + RED + str(hp) + GREEN + " hp." + RESET, c)
            print(" ", end="\n")

        if hp <= 0:
            dead()
            break


            



def Tuto_full():
    global hp_goblina
    Slow_text(GREEN + "Przechodzisz tutorial" + RESET, d)
    print(" ", end = "\n")
    Slow_text(GREEN + "Jesteś w miejscu startowym. Porusz się do przodu używając klawisza" + YELLOW + " w" + GREEN + "." + RESET, d)
    print(" ", end = "\n")
    while True:
        a = input()
        if a == "w":
            Slow_text(GREEN + "Jesteś w kolejnym miejscu, ciągle jesteś otoczony ścianami z lewej i prawej, użyj" + YELLOW + " w" + GREEN + ", aby poruszyć się dalej..." + RESET, d)
            print(" ", end = "\n")
            break
        else:
            print(RED + "Nie możesz iść w tą stronę!" + RESET, d)
            continue

    while True:
        a = input()
        if a == "w":
            Slow_text(RED + "Napotkałeś na swojej drodze goblina!" + GREEN + " Aby użyć zwykłego ataku wybierz" + YELLOW + " z" + GREEN + ", aby użyć ataku specjalnego wybierz" + BLUE + " x" + RESET, d)
            
            break
        else:
            print(RED + "Nie możesz tak zrobić!" + RESET, d)
            continue

    print(" ", end = "\n")
    print("Posiadasz: " + BLUE + str(mana) + " many" + RESET + " i " + RED + str(hp) + " życia" + RESET + ".")
        
    hp_goblina = Goblin_hp() 
    
    def Tuto():
        
        global atak_oponenta
        Slow_text(GREEN + "Zwykły atak - " + YELLOW + "z" + GREEN + ", specjalny atak -" + BLUE + " x" + RESET, c)
        print(" ", end = "\n")
        global hp_goblina
        while True:
            a = input()

            if a == "z":
                obrazenia = zwykly_atak()
                hp_goblina -= obrazenia 
                Slow_text(GREEN + "Użyłeś zwykłego ataku zadałeś " + RED + str(obrazenia) + GREEN + " obrażeń" + RESET, c)
                print(" ", end="\n")
                Slow_text(RED + "Goblin" + GREEN + " ma teraz " + RED + str(hp_goblina) + GREEN + " hp", c)
                print(" ", end="\n")
                break
            elif a == "x":
                obrazenia = MAGIC()
                hp_goblina -= obrazenia  
                Slow_text(GREEN + ", zadałeś " + RED + str(obrazenia) + GREEN + " obrażeń" + RESET, c)
                print(" ", end="\n")
                Slow_text(RED + "Goblin" + GREEN + " ma teraz " + RED + str(hp_goblina) + GREEN + " hp", c)
                print(" ", end="\n")
                break
            else:
                print(RED + "Nie możesz tak zrobić!" + RESET, c)
                continue
        if hp_goblina <= 0:
            Slow_text(RED + "Brawo! " + GREEN + " Zabiłeś goblina! ", c)
        else:
            Slow_text(RED + "Goblin " + GREEN + "zaatakował!" + RESET, c)
            print(" ", end="\n")
            atak_goblina = Goblin_atak()
            Slow_text(RED + "Goblin" + GREEN + " zadał ci " + RED + str(atak_goblina) + GREEN + " obrażeń" + RESET, c)
            print(" ", end="\n")
            Slow_text(GREEN + "Zostało ci " + RED + str(int(hp) - int(atak_goblina)) + GREEN + " hp." + RESET, c)
            print(" ", end="\n")
            Tuto()

    Tuto()

#------------------------------------------------------------------------------------------------

Slow_text(GREEN + "Czy chcesz przejść tutorial? " + YELLOW + "(t/n)" + RESET, d)
print(" ", end = "\n")
while True:
    a = input().upper()
    if a == "T" or a == "TAK":
        Tuto_full()
        break
    elif a == "N" or a == "NIE":
        print(" ", end = "\n")
        break
    else:
        Slow_text(RED + "Nie ma takiej komendy. " + YELLOW + "(t/n)" + RESET, d)
        print(" ", end = "\n")
        continue

#------------------------------------------------------------------------------------------------
if rasa == "CZŁOWIEK" or rasa == "CZLOWIEK":
     mana, hp = czlowiek()     
elif rasa == "ELF":
     mana, hp = elf()
elif rasa == "MAG":
     mana, hp = mag()
elif rasa == "BARBARZYŃCA" or rasa == "BARBARZYNCA":
     mana, hp = barbarzynca()
elif rasa == "NIZIOŁEK" or rasa == "NIZIOLEK":
     mana, hp = niziolek()
elif rasa == "ORK":
     mana, hp = ork()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print(" ", end = "\n")
Slow_text(YELLOW + "Przeszedłeś tutorial, mana i inne statystyki zostały odnowione" + RESET, d)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def lewo_prawo():
    global x
    print(" ", end = "\n")
    while True:
        Slow_text(GREEN + "możesz iść w prawo lub w lewo używajac klawiszy" + YELLOW + " a" + GREEN + " i" + YELLOW + " d", c)
        print(" ", end = "\n")
        x = input()
        if x == "d":
            
            Slow_text(GREEN + "Poszedłeś w prawo." + RESET, c)
            break
        elif x == "a":
            
            Slow_text(GREEN + "Poszedłeś w lewo." + RESET, c)
            break
        else:
            
            Slow_text(RED + "Nie możesz iść w tą stronę.", c)
            print(" ", end="\n")
            continue


def lewo_prawo_przod():
    global x
    while True:
        Slow_text(GREEN + "możesz iść w prawo w lewo lub prosto używajac klawiszy" + YELLOW + " d" + GREEN + ", " + YELLOW + "a " + GREEN + "i " + YELLOW + "w" + RESET , c)
        print(" ", end = "\n")
        x = input()
        if x == "d":
            print(" ", end = "\n")
            Slow_text(GREEN + "Poszedłeś w prawo." + RESET, c)
            break
        elif x == "a":
            print(" ", end = "\n")
            Slow_text(GREEN + "Poszedłeś w lewo." + RESET, c)
            break
        elif x == "w":
            print(" ", end="\n")
            Slow_text(GREEN + "Poszedłeś przed siebie." + RESET, c)

        else:
            Slow_text(RED + "Nie możesz iść w tą stronę.", c)
            print(" ", end="\n")
            continue

def prosto_prawo():
    global x
    while True:
        Slow_text(GREEN + "mozesz isc w prawo lub prosto używając klawiszy" + YELLOW + " d" + GREEN + " i" + YELLOW + " w" + RESET , c)
        print(" ", end = "\n")
        x = input()
        if x == "d":
            Slow_text(GREEN + "Poszedłeś w prawo." + RESET, c)
            print(" ", end = "\n")
            break
        elif x == "w":
            Slow_text(GREEN + "Poszedłeś prosto." + RESET, c)
            print(" ", end = "\n")
            break
        else:
            print(" ", end = "\n")
            Slow_text(RED + "Nie możesz iść w tą stronę.", c)
            print(" ", end="\n")
            continue



def przod():
     global x
     print(" ", end = "\n")
     while True:
        Slow_text(GREEN + "idź prosto (" + YELLOW + "w" + GREEN + ")" + RESET, c)
        print(" ", end = "\n")
        x = input()
        if x == "w":
            Slow_text(GREEN + "Poszedłeś prosto.", c)
            print(" ", end = "\n")
            break
        else:
            print(" ", end = "\n")
            Slow_text(RED + "Nie możesz iść w tą stronę.", c)
            print(" ", end="\n")
            continue

def prawo():
    global x
    while True:
        Slow_text(GREEN + "idź w prawo (" + YELLOW + "d" + GREEN + ")" + RESET, c)
        print(" ", end = "\n")
        x = input()
        if x == "d":
            Slow_text(GREEN + "Poszedłeś w prawo.", c)
            break
        else:
            print(" ", end = "\n")
            Slow_text(RED + "Nie możesz iść w tą stronę.", c)
            print(" ", end="\n")
            continue

def lewo():
    global x
    while True:
        Slow_text(GREEN + "idź w lewo (" + YELLOW + "a" + GREEN + ")" + RESET, c)
        print(" ", end = "\n")
        x = input()
        if x == "a":
            Slow_text(GREEN + "Poszedłeś w lewo." + RESET, c)
            break
        else:
            print(" ", end = "\n")
            Slow_text(RED + "Nie możesz iść w tą stronę." + RESET,c)
            print(" ", end="\n")
            continue

def potka():
    global mana
    Slow_text(GREEN + "Gratulacje znalazłeś" + BLUE +" potkę" + GREEN + "!" + RESET, d)
    print(" ", end="\n")
    mana += 20
    print("Posiadasz: " + BLUE + str(mana) + " many" + RESET + " i " + RED + str(hp) + " życia" + RESET + ".")






print(" ", end = "\n")
Slow_text(YELLOW + "Jesteś na starcie.", d)

#=============
lewo_prawo()
#=============


while True:
    if x == "a":
        print(" ", end = "\n")
        prawo()
        print(" ", end="\n")
        lewo()
        print(" ", end="\n")
        walka()
        if hp <= 0:
            dead()
            break
        else:
            print(" ", end = "\n")
            prawo()
            print(" ", end="\n")
            potka()
            prawo()
            print(" ", end = "\n")
            walka()
            if hp <= 0:
                dead()
                break
            else:
                print(" ", end = "\n")
                lewo()
                print(" ", end = "\n")
                pokoj12()
                break
    elif x == "d":
        przod()
        walka()
        if hp <= 0:
            dead()
            break
        else:
            print(" ", end="\n")
            lewo()
            przod()
            potka()
            lewo()
            print(" ", end="\n")
            walka()
            if hp <= 0:
                dead()
                break
            else:
                print(" ", end="\n")
                prawo()
                print(" ", end="\n")
                pokoj123()
                break
    else:
        Slow_text(RED + "Nie możesz iść w tą stronę." + RESET,c )
        print(" ", end="\n")
        continue

print(" ", end = "\n")

