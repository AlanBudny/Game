from random import randint, random;
import time
#----------------------------------------Stats
Imie = input(str("podaj imię swojego bohatera - "))
life = 0
weapon = "drewniany miecz"
bow = "stary łuk"
gold = 0
Hp = 100
Bonus_Hp = 0
Dmg = 0
Exp = 0
Arena = 1
arrows = 0
#-----------------------------------ceny
s_zbroja = "25G"
z_zbroja = "75G"
p_zbroja = "150G"
s_zbroja_cena = 25
z_zbroja_cena = 75
p_zbroja_cena = 150
k_miecz = "40G"
z_miecz = "120G"
p_miecz = "200G"
b_miecz = "300G"
k_miecz_cena = 40
z_miecz_cena = 120
p_miecz_cena = 200
b_miecz_cena = 300
n_luk = "125G"
n_luk_cena = 125

#-----------------------------------atack
def atack(weapon,bow):
    global arrows
    print("1=normalny atak")
    print(f"2=strzał z łuku (masz {arrows} strzał)")
    atak = input()
    if atak == "1":
        if weapon == "drewniany miecz":
            return randint(5,10)
        if weapon == "kamienny miecz":
            return randint(8,13)
        if weapon == "żelazny miecz":
            return randint(12,17)
        if weapon == "platynowy miecz":
            return randint(16,21)
        if weapon == "boski miecz":
            return randint(20,25)
    if atak == "2":
        if arrows > 0:
            arrows -= 1
            if bow == "stary łuk":
                return randint(8,18)
            if bow == "nowy łuk":
                return randint(20,30)
        else:
            print("Nie masz strzał")
            return atack(weapon,bow)
    else:
        print("nie wybrano akcji")
        return atack(weapon,bow)
#---------------------------------Arena
def arena():
#    0-nazwa, 1-życie, 2-obrażenia, 3-gold, 4-EXP
    global gold,weapon,bow,life,Imie,Exp,Hp,Dmg,Bonus_Hp,Arena,arrows
    if Arena == 1:
        locked = "Zablokowane"
    if Arena > 1:
        locked = " "
    liczba_pokonanych_przeciwnikow = 0
    print("Gdzie chcesz się udać:\n1-Dziki Las\n2-Zniszczone Przedmieścia ""\033[1m" + f"{locked}" + "\033[0m""\n3-powrót")
    miejsce = input()
    if miejsce == "3":
        sklep_i_arena()
    if miejsce == "1":
        life = Hp + Bonus_Hp
        y = 5
        while life >= 1:
            print(r"                                                                                /\           ")
            print(r"                                                                               /  \          ")
            print(r"                 /\                                                           , `` ,         ")
            print(r"                /;'\                                                         <.-  -.>        ")
            print(r"               / ,:,\                                                        , `  ` ,        ")
            print(r"             .'. ',. '.                                                     <.- '' -.>       ")
            print(r"           .'  '. ' ;  '.                                                   , ` __ ` ,       ")
            print(r"      ,.-' .-'_-''''-_'-. '-.,                                            <.- ' ,, ' -.>     ")
            print(r"     <,.-'_-': . : .  ,'-_'-.,>                                            , ` _,,_ ` ,      ")
            print(r"  _-' ;  ; __,.-'  '-.,__ ,   ;'-_                /\                     <.- ' ,  , ' -.>    ")
            print(r"<_,..-- ''_-': . : .  ,'-'' --..,_>              /.'\                     , ` _,..,_ ` ,     ")
            print(r"      _-' ; :  ' __ ''  ,. '-_                 .',__;'.                 <.- ' ,    , ' -.>   ")
            print(r"  _-' ;  ; __,.-'  '-.,__ ,   ;'-_           <.-',--,'-.>                , ` _,....,_ ` ,    ")
            print(r"<_,..-- ''_-': . : .  ,'-'' --..,_>            .':__''.                <.- ' ,      , ' -.>  ")
            print(r"      _-' ; :  ' __ ''  ,. '-_               <.-',--,'-.>               , ` _,..--..,_ ` ,   ")
            print(r"  _-' ;  ; __,.-'/|'-.,__ ,   ;'-_             .'.__.'.               <.- ' ,        , ' -.> ")
            print(r"<_,..-- ''    ||/ }\ ||   '' --..,_>     __,.<.-'|\||'-.>   |  |       , ` _,..----..,_ ` ,  ")
            print(r"___,..-- ''`' ||\{;/\)| ' -..__,.,_,.-''  __,.._ ''.|-.,__,.|\/|,    <.- '   |      |   ' -.>")
            print(r"              '-.,.,.-' .,.;:.;.,      ,-{  [)  \                '' -- .,___,'-.,,.-',__     ")
            print(r"    .,;';,.                           /__  /_|_ _)    ,.;';.                             ''-.")
            print("Wędrujesz dalej w głąb lasu")
            time.sleep(1.5)
            dwarf = ["Krasnoludem",30,10,10,15] #Arena 1
            goblin = ["Goblinem",20,12,10,10] #Arena 1
            ogre = ["Ogrem",45,6,15,20]       #Arena 1    
            list_Opponents = [dwarf,goblin,ogre]
            x = randint(0, 3)                  
            while x == y:
                x = randint(0, 3)             
            y = x
            if x == 3:
                zdarzenie = randint(1, 3)      
                if zdarzenie == 1:
                    mimic()
                if zdarzenie == 2:
                    master()
                if zdarzenie == 3:
                    bandit()
            if x < 3:
                Opponent = list_Opponents[x]
                print("-"*40)
                while Opponent[1] > 0:
                    if x == 0:
                        print(r"                  ,dM                                                                              ")
                        print(r"                 dMMP                                                                              ")
                        print(r"                dMMM'                                                                              ")
                        print(r"                \MM/                                                                               ")
                        print(r"                dMMm.                                                                              ")
                        print(r"               dMMP'_\---.                                                                         ")
                        print(r"              _| _  p ;88;`.                                                                       ")
                        print(r"            ,db; p >  ;8P|  `.                                                                     ")
                        print(r"           (``T8b,__,'dP |   |                                                 ,-- .               ")
                        print(r"           |   `Y8b..dP  ;_  |                                        ,       /|\   :              ")
                        print(r"           |    |`T88P_ /  `\;                                 \.,_,,-'\      | |   ;              ")
                        print(r"           :_.-~|d8P'`Y/    /                                   \   (\` `    ,_;  :_,              ")
                        print(r"            \_   TP    ;   7`\.                                  \  /\\     /;    /  )             ")
                        print(r" ,,__        >   `._  /'  /   `\_                                 \( ,\\ _;' \      //             ")
                        print(r" `._ ''''~~~~------|`\;' ;     ,'                                  `  \><)_,';,.'  / (             ")
                        print(r"    '''~~~-----~~~'\__[|;' _.-'  `\.                                   \ )._ ___,.'  \             ")
                        print(r"            ;--..._     .-'-._     ;                                         ;       :             ")
                        print(r"           /      /`~~.'   ,'`\_ ,/.                                         [===O===]             ")
                        print(r"          ;_    /'        /    ,/                                           /~~~/|~~~|             ")
                        print(r"          | `~-l         ;    /                                            /.  / | _ |             ")
                        print(r"__________`\    ;_______/\.._|____________________________________________{ }'{__{  }'  ______________")
                        print(r"            \    \      \     \.                                           ]--|   ]  [             ")
                        print(r"            /`---';      `----'                                          (_)_ ;   |--|             ")
                        print(r"           (     /                                                              (_)_;/             ")
                        print(r"            `---'                                                                                  ")
                    if x == 1:
                        print(r"                  ,dM                                                                ")
                        print(r"                 dMMP                                                                ")
                        print(r"                dMMM'                                                                ")
                        print(r"                \MM/                                                                 ")
                        print(r"                dMMm.                                                    ,.--./|     ")
                        print(r"               dMMP'_\---.                                             /'    /||     ")
                        print(r"              _| _  p ;88;`.                                         _(|)   (_}/     ")
                        print(r"            ,db; p >  ;8P|  `.                                   ,.*'  _     * )     ")
                        print(r"           (``T8b,__,'dP |   |                                    `'`,`',_   _/      ")
                        print(r"           |   `Y8b..dP  ;_  |                                  /|  {|   I,_,I       ")
                        print(r"           |    |`T88P_ /  `\;                                 { |  {|  /     '-     ")
                        print(r"           :_.-~|d8P'`Y/    /                                  {;|  {| {     (  ;    ")
                        print(r"            \_   TP    ;   7`\.                                {;|  ()=;    (    |   ")
                        print(r" ,,__        >   `._  /'  /   `\_                              {;|   ___..-'`   /    ")
                        print(r" `._ ''''~~~~------|`\;' ;     ,'                              (>)||_____...--''     ")
                        print(r"    '''~~~-----~~~'\__[|;' _.-'  `\.                            '       }      |     ")
                        print(r"            ;--..._     .-'-._     ;                                    `''--''`     ")
                        print(r"           /      /`~~.'   ,'`\_ ,/.                                    `''--''`     ")
                        print(r"          ;_    /'        /    ,/                                       /////|||     ")
                        print(r"          | `~-l         ;    /                                        /////||||     ")
                        print(r"__________`\    ;_______/\.._|________________________________________{|||{_{||{______________________")
                        print(r"            \    \      \     \.                                      |\/\|  \|\\    ")
                        print(r"            /`---';      `----'                                       |   |   \__\   ")
                        print(r"           (     /                                                    |_-_| c'.__,}  ")
                        print(r"            `---'                                                  C'.___,}          ") 
                    if x ==2:
                        print(r"                  ,dM                                                 ")
                        print(r"                 dMMP                                                 ")
                        print(r"                dMMM'                                                             (\    /)")
                        print(r"                \MM/                                                              |_)//(_|")
                        print(r"                dMMm.                                                             |4\_/4)(")
                        print(r"               dMMP'_\---.                                                       '( (_  -)D")
                        print(r"              _| _  p ;88;`.                                                       ) _)  /\,__")
                        print(r"            ,db; p >  ;8P|  `.                                                   _,\_._,/ /   `)")
                        print(r"           (``T8b,__,'dP |   |                                      \.,_,,      ( _   ~ .   ,   \)")
                        print(r"           |   `Y8b..dP  ;_  |                                       \   (\      \(   \/  _)(    )")
                        print(r"           |    |`T88P_ /  `\;                                        \   \\      )). _______>-. `*")
                        print(r"           :_.-~|d8P'`Y/    /                                          \  /\\    _'( /   /\  '\  _)")
                        print(r"            \_   TP    ;   7`\.                                         \( ,\\.-'  '/    \/    \/")
                        print(r" ,,__        >   `._  /'  /   `\_                                        '  \><)_'.)|/\/\/\/\/\|")
                        print(r" `._ ''''~~~~------|`\;' ;     ,'                                             \) ,( |\/\/\/\/\/|")
                        print(r"    '''~~~-----~~~'\__[|;' _.-'  `\.                                          ' ((  \    /\    /")
                        print(r"            ;--..._     .-'-._     ;                                           ((((  \___\/___/)")
                        print(r"           /      /`~~.'   ,'`\_ ,/.                                           ((,) /   ((()   )")
                        print(r"          ;_    /'        /    ,/                                                '..-,  (()('   /")
                        print(r"          | `~-l         ;    /                                                   _//.   ((() .'")
                        print(r"__________`\    ;_______/\.._|________________________________________________ //,/'____ ((( ', ______")
                        print(r"            \    \      \     \.                                                           ((  )")
                        print(r"            /`---';      `----'                                                             / /")
                        print(r"           (     /                                                                        _/,/'")
                        print(r"            `---'                                                                       /,/,'")
                    print(f"Walczysz z {Opponent[0]}")
                    print(f"Przeciwnik ma {Opponent[1]} Hp i zadaje ci {Opponent[2]} obrażeń")
                    life = life - Opponent[2]
                    time.sleep(0.5)
                    if life <= 0:
                        break
                    print(f"Zostało ci {life} Hp")
                    atak = atack(weapon,bow)+Dmg
                    Opponent[1] = Opponent[1] - atak
                    print(f"Zadałeś {atak} obrażeń")
                    time.sleep(1)
                    if Opponent[1] <= 0:
                        print("-"*40)
                        print('Zabiłeś przeciwnika')
                        time.sleep(1.5)
                        gold = gold+Opponent[3]
                        liczba_pokonanych_przeciwnikow = liczba_pokonanych_przeciwnikow+1
                        Exp = Exp+Opponent[4]
                if liczba_pokonanych_przeciwnikow > 7:
                    print("Przeszedłeś przez Dziki Las")
                    Arena = 2
                    locked = " "
                    sklep_i_arena()
        print(r"            .--.      ")
        print(r"         ,'      ',   ")
        print(r"        ;    ||    ;  ")
        print(r"        |  ==[]==  |  ")
        print(r"        |    ||    |  ")
        print(r"        |    ||    |  ")
        print(r"        |    ||    |  ")
        print(r"        |__________|  ")
        print(r"       /.':,.,'.~,:/  ")
        print(r"      /;';,.~.,',;/   ")
        print(r"     /;:~,.:,.:~;/    ")
        print(r"    /:;'.:';~::./     ")
        print(r"   /;:,~.:';.';/      ")
        print(r"   `''''''''''`       ")
        print("zginąłeś")
        print("pokonałeś",liczba_pokonanych_przeciwnikow,"przeciwników")
        time.sleep(1)
        liczba_pokonanych_przeciwnikow = 0
        sklep_i_arena()
    if miejsce == "2":
        if Arena == 1:
            print("Nie odblokowałeś jeszcze tej krainy")
            arena()
        if Arena == 2:
            life = Hp + Bonus_Hp
            while life >= 1:
                knight = ["Mrocznym Rycerzem",60,16,30,40]      #Arena 2
                giant = ["Olbrzymem",80,12,35,45]               #Arena 2
                elf = ["Mrocznym Elfem",50,18,30,40]            #Arena 2
                list_Opponents = [knight,giant,elf]
                x = randint(0,2)
                Opponent = list_Opponents[x]
                print("-"*40)
                while Opponent[1] > 0:
                    print(f"{Imie} walczy teraz z {Opponent[0]}")
                    print(f"Przeciwnik ma {Opponent[1]} Hp i zadaje ci {Opponent[2]} obrażeń")
                    life = life - Opponent[2]
                    if life <= 0:
                        break
                    print(f"Zostało ci {life} Hp")
                    atak = atack(weapon,bow)+Dmg
                    Opponent[1] = Opponent[1] - atak
                    print(f"Zadałeś {atak} obrażeń")
                    if Opponent[1] <= 0:
                        print("-"*40)
                        print('Zabiłeś przeciwnika')
                        gold = gold+Opponent[3]
                        liczba_pokonanych_przeciwnikow = liczba_pokonanych_przeciwnikow+1
                        Exp = Exp+Opponent[4]
                if liczba_pokonanych_przeciwnikow > 7:
                    print("Przeszedłeś przez Zniszczone Przedmieścia")
                    sklep_i_arena()
            print("zginąłeś")
            print("pokonałeś",liczba_pokonanych_przeciwnikow,"przeciwników")
            liczba_pokonanych_przeciwnikow = 0
            sklep_i_arena()
    else:
        print("Podałeś zła liczbę")
        arena()
#---------------------------------Sklep
def sklep_i_arena():
    print("-"*40)
    global arrows,gold,weapon,bow,life,Imie,Exp,Hp,Dmg,Bonus_Hp,Arena,s_zbroja,z_zbroja,p_zbroja,s_zbroja_cena,z_zbroja_cena,p_zbroja_cena,k_miecz,z_miecz,p_miecz,b_miecz,k_miecz_cena,z_miecz_cena,p_miecz_cena,b_miecz_cena,n_luk,n_luk_cena
    while Exp >= 100:
        print("zdobyłeś poziom")
        print("na co chcesz przeznaczyć punkt doświadczenia:\n1-obrażenia(+1)\n2-zdrowie(+3)")
        poziom = input()
        if poziom == "1":
            Dmg = Dmg+1
            print("-"*40)
        elif poziom == "2":
            Bonus_Hp = Bonus_Hp+3
            print("-"*40)
        else:
            print("-"*40)
            print("źle podana liczba")
            sklep_i_arena()
        Exp = Exp-100
    print("Gdzie chcesz iść:\n1-Kowal\n2-Zbrojmistrz\n3-Łucznik\n4-Podróż\n5-Ekwipunek i Statystyki")
    print("masz",gold,"golda ")
    czynnosc = input()
    if czynnosc == "1":
        print("-"*40)
        print(r"        ,<'.                            ")
        print(r"       ;  '.' .                         ")
        print(r"        *.  ',-'.                       ")
        print(r"        ;;' ;:.'                        ")
        print(r"       ;;                 _             ")
        print(r"      ;;           ,-.=' ,;'            ")
        print(r"     ;;        ,-'      ;;'             ")
        print(r"     '    ,-'      ,-' ,'               ")
        print(r"         |`'._,.-' ,-'                  ")
        print(r"          `';.;,-'  (.                  ")
        print(r"         ,='  |     .-'|                ")
        print(r"        |'.  ,' .-' .-'                 ")
        print(r"         '.':-' .-'                     ")
        print(r"           '.-'                         ")
        print("Witaj u Kowala")
        print("Który miecz chcesz kupić")
        print(f"1-kamienny miecz(8-13)-{k_miecz}\n2-żelazny miecz(12-17)-{z_miecz}\n3-platynowy miecz(16-21)-{p_miecz}\n4-boski miecz(20-25)-{b_miecz}\n5-powrót")
        wybor = input()
        if wybor == "1":
            if gold >= k_miecz_cena:
                gold = gold - k_miecz_cena
                k_miecz_cena = 0
                k_miecz = "Wyposaż"
                weapon = "kamienny miecz"
                print("Wyposażyłeś kamienny miecz")
                sklep_i_arena()
            else:
                print("nie stać cię")
                sklep_i_arena()
        if wybor == "2":
            if gold >= z_miecz_cena:
                gold = gold - z_miecz_cena
                z_miecz_cena = 0
                z_miecz = "Wyposaż"
                weapon = "żelazny miecz"
                print("Wyposażyłeś żelazny miecz")
                sklep_i_arena()
            else:
                print("nie stać cię")
                sklep_i_arena()
        if wybor == "3":
            if gold >= p_miecz_cena:
                gold = gold - p_miecz_cena
                p_miecz_cena = 0
                p_miecz = "Wyposaż"
                weapon = "platynowy miecz"
                print("Wyposażyłeś platynowy miecz")
                sklep_i_arena()
            else:
                print("nie stać cię")
                sklep_i_arena()
        if wybor == "4":
            if gold >= b_miecz_cena:
                gold = gold - b_miecz_cena
                b_miecz_cena = 0
                b_miecz = "Wyposaż"
                weapon = "boski miecz"
                print("Wyposażyłeś boski miecz")
                sklep_i_arena()
            else:
                sklep_i_arena()
        if wybor == "5":
            sklep_i_arena()
        else:
            print("Podałeś złą liczbę")
            sklep_i_arena()
    if czynnosc == "3":
        print("-"*40)
        print("Co chcesz kupić")
        print(r"                                        ")
        print(r"                  ,,                    ")
        print(r"                  ;;                    ")
        print(r"                 .--.                   ")
        print(r"              .'  __  '.                ")
        print(r"            .  .'    '.  .              ")
        print(r"           .  :  .''.  :  .             ")
        print(r"           : :  : () :  : :             ")
        print(r"           '  :  `..`  :  '             ")
        print(r"            '  '.    .'  '              ")
        print(r"             '.   ''   .'               ")
        print(r"              ,;' -- ';,                ")
        print(r"              ;'  ||  ';                ")
        print(r"_____________,;___||___;,_______________")
        print(r"             ;'   ''   ';               ")
        print(r"            ,;          ;,              ")
        print(r"                                        ")
        print(f"1-strzały 1-3G\n2-nowy łuk(20-30)-{n_luk}\n3-powrót")
        wybor1 = input()
        if wybor1 == "1":
            print("-"*40)
            print("Ile strzał chcesz kupić")
            ile = int(input())
            if gold >= 3*ile:
                print(f"kupiłeś {ile} strzał za {3*ile}G")
                gold -= 3*ile
                arrows = arrows + ile
                sklep_i_arena()
            else:
                print("nie stać cię")
                sklep_i_arena()
        if wybor1 == "2":
            if gold >= n_luk_cena:
                gold = gold - n_luk_cena
                n_luk_cena = 0
                n_luk = "Wyposaż"
                bow = "nowy łuk"
                print("Wyposażyłeś nowy łuk")
                sklep_i_arena()
            else:
                print("nie stać cię")
                sklep_i_arena()
        if wybor1 == "3":
            sklep_i_arena()
        else:
            print("Podałeś złą liczbę")
            sklep_i_arena()
    if czynnosc == "2":
        print("-"*40)
        print(r"         _                 _            ")
        print(r"     .,' ,' (` ' '' ' `) ', ',.         ")
        print(r"    : '.__'.  `' -- '`  .'__.' :        ")
        print(r"   ;`;-'  :      ..      :  '-;`;       ")
        print(r"    '      '-.   ::   .-'      '        ")
        print(r"           :     ..     :               ")
        print(r"            '-.  ::  .-'                ")
        print(r"            :    ..    :                ")
        print(r"            ,'-. .. .-',                ")
        print(r"           /`'.      .'`\               ")
        print(r"         .'  .'  ..  '.  '.             ")
        print(r"                                        ")
        print(f"Którą zbroje chcesz kupić:\n1-skórzana zbroja(125HP)-{s_zbroja}\n2-żelazna zbroja(150HP)-{z_zbroja}\n3-platynowa zbroja(200HP)-{p_zbroja}\n4-powrót")
        wybor2 = input()
        if wybor2 == "1":
            if gold >= s_zbroja_cena:
                gold = gold - s_zbroja_cena
                s_zbroja_cena = 0
                s_zbroja = "Wyposaż"
                Hp = 125
                print("Wyposażyłeś skórzaną zbroję")
                sklep_i_arena()
            else:
                print("nie stać cię")
                sklep_i_arena()
        if wybor2 == "2":
            if gold >= z_zbroja_cena:
                gold = gold - z_zbroja_cena
                z_zbroja_cena = 0
                z_zbroja = "Wyposaż"
                Hp = 150
                print("Wyposażyłeś żelazną zbroję")
                sklep_i_arena()
            else:
                print("nie stać cię")
                sklep_i_arena()
        if wybor2 == "3":
            if gold >= p_zbroja_cena:
                gold = gold - p_zbroja_cena
                p_zbroja_cena = 0
                p_zbroja = "Wyposaż"
                Hp = 200
                print("Wyposażyłeś platynową zbroję")
                sklep_i_arena()
            else:
                print("nie stać cię")
                sklep_i_arena()
        if wybor2 == 4:
            sklep_i_arena()
        else:
            print("Podałeś złą liczbę")
            sklep_i_arena()
    if czynnosc == "4":
        print("-"*40)
        arena()
    if czynnosc == "5":
        print("-"*40)
        print(r"        ,- _                  ")
        print(r"       :    ,- _              ")
        print(r"       /`[;:    ,-,           ")
        print(r"      |    ;`[;:   : ,;.      ")
        print(r"      |   :    /'-'\'' :,     ")
        print(r"      |   :   |     |  :;     ")
        print(r"       \  :   |     |  ||     ")
        print(r"      ( '-,:  |     |  ;;     ")
        print(r"        '-( -.,\.'./; .;'     ")
        print(r"            '-(`( )`)''       ")
        print(r"                `'`           ")
        print(f"Wyposażony ekwipunek:\n{weapon}\n{bow}\n{arrows} strzał")
        if Hp == 100:
            print("brak zbroi")
        if Hp == 125:
            print("skórzana zbroja")
        if Hp == 150:
            print("żelazna zbroja")
        if Hp == 200:
            print("platynowa zbroja")
        print(f"{Hp+Bonus_Hp} Punktów zdrowia")
        print(f"{Dmg} Bonusowych obrażeń")
        time.sleep(1)
        sklep_i_arena()
    else:
        print("Podałeś złą liczbę")
        sklep_i_arena()
#-----------------------------------losowe zdarzenia
def mimic():
    global gold,life,arrows
    print(r'')
    print(r'                  ,-_"==._                                            ')
    print(r'                ,","      `"==._                                      ')
    print(r'              ,","              `"==._                                ')
    print(r'              ._`"=._               ,-""=__                           ')
    print(r'              |o`"=._`"=._        ," ,""   "",                        ')
    print(r'              | ;`-.o`"=._`"=._ ," ,"     __.-";                      ')
    print(r'              |o;    `"-.o`"=._`"=; _.--" __.-o;                      ')
    print(r'______________| ;     (#) `-.o `"=|`_.--"_o.-; ;______________________')
    print(r'              |o;._    "      `".o|o_.--"    ;o;                      ')
    print(r'               "=._o--._        ; | ;        ; ;                      ')
    print(r'                    "=._o--._   ;o|o;     _._;o;                      ')
    print(r'                         "=._o._; | ;_.--"o.--"                       ')
    print(r'                              "=.o|o_.--""                            ')
    print(r'')
    print("Napotkałeś na swojej drodze skrzynię\n1-Otwierasz ją ciekawy co jest w środku\n2-Omijasz ją bojąc się pułapki")
    mimik = input()
    if mimik == "1":
        szansa = randint(1,3)
        if szansa == 3:
            print(r'')
            print(r'                   .=""_;=.                                           ')
            print(r'               ,-"_,=""     `"=.                                      ')
            print(r'               "=._o`"-._        `"=.                                 ')
            print(r'                   `"|/_o`"=._      _`"=._                            ')
            print(r'                  _.--" :=._o  "=._."_.-=" "=.                        ')
            print(r'              ._"           _|/"=/_,-._       ".,                     ')
            print(r'              |o`"=.|\  _.-"__"-.  -._"-._    ; ;                     ')
            print(r'              | ;`-.o` / ,-"  "-      "-._"-._ /                      ')
            print(r'              |o;    `"\/o`"=.|\         _=.--o;                      ')
            print(r'______________| ;     (#) `-.o `"=. _.--"_o.-; ;______________________')
            print(r'              |o;._    "      `".o|o_.--"    ;o;                      ')
            print(r'               "=._o--._        ; | ;        ; ;                      ')
            print(r'                    "=._o--._   ;o|o;     _._;o;                      ')
            print(r'                         "=._o._; | ;_.--"o.--"                       ')
            print(r'                              "=.o|o_.--""                            ')
            print(r'')
            print("Skrzynia okazała się być mimikiem\nTracisz 15 punktów zdrowia")
            life -= 15
            time.sleep(2)
        else:
            loot = randint(1,3)
            print(r'')
            print(r'                   .=""_;=.                                           ')
            print(r'               ,-"_,=""     `"=.                                      ')
            print(r'               "=._o`"-._        `"=.                                 ')
            print(r'                   `"=._o`"=._      _`"=._                            ')
            print(r'                        :=._o "=._."_.-=" "=.                         ')
            print(r'              ._"  ,. .` ` `` ,  `"-._"-._   ".,                      ')
            print(r'              |o`"=._` , "` `; .". ,  "-._"-._; ;                     ')
            print(r'              | ;`-.o`"=._; ." ` "`.".` . "-._ /                      ')
            print(r'              |o;    `"-.o`"=._``  "` " ,__.--o;                      ')
            print(r'______________| ;     (#) `-.o `"=.`_.--"_o.-; ;______________________')
            print(r'              |o;._    "      `".o|o_.--"    ;o;                      ')
            print(r'               "=._o--._        ; | ;        ; ;                      ')
            print(r'                    "=._o--._   ;o|o;     _._;o;                      ')
            print(r'                         "=._o._; | ;_.--"o.--"                       ')
            print(r'                              "=.o|o_.--""                            ')
            print(r'')
            if loot == 3:
                gold_chest = randint(5,10)
                arrows_chest = randint(3,4)
                arrows += arrows_chest
                gold += gold_chest
                print(f"Otwierasz skrzynię i znajdujesz w niej {gold_chest} monet i {arrows_chest} strzały")
                time.sleep(2)
            else:
                gold_chest = randint(10,15)
                gold += gold_chest
                print(f"Otwierasz skrzynię i znajdujesz w niej {gold_chest} monet")
                time.sleep(2)
    elif mimik == "2":
        print("Poszedłeś dalej omijając skrzynię")
        time.sleep(1)
    else:
        print("Podałeś złą liczbę")
        mimic()
def master():
    global gold,Imie,Exp,Dmg,Bonus_Hp
    print(r"                                  ")
    print(r"                  , - .           ")
    print(r"               ,'   .' `          ")
    print(r"              :     :             ")
    print(r"            _:       :_           ")
    print(r"         .' :         : '.        ")
    print(r"         '.  '-._ _.-'  .'        ")
    print(r"           (` --...-- `)          ")
    print(r"            ;,,  |  ,,;           ")
    print(r'            ;, ""-""` ;           ')
    print(r"             ; ;  ' `;            ")
    print(r"         _,..;`  ';  ;..,_        ")
    print(r"       ;''    ; ':  ;  ; ;'.      ")
    print(r'      :       ; , " ; /  | |:     ')
    print(r"      :      __;' ';''  / / :     ")
    print(r"      :--''` _. ;,;.-''  /  :     ")
    print(r"                                  ")
    print(f"Napotykasz na swojej drodze mędrca. Ofiaruje ci on swoją wiedzę za cenę 10 monet (Masz {gold} monet)\n1-Przyjmujesz ofertę\n2-Odrzucasz ofertę i idziesz dalej")
    medrec = input()
    if medrec == "1":
        if gold < 10:
            print("Nie stać cię było na nauki mędrca. Idziesz dalej")
            time.sleep(1.5)
        if gold >= 10:
            nauka = randint(1,3)
            gold -= 10
            if nauka == 1:
                Dmg += 1
                print("Nauczyłeś się nowych metod walki (Zyskujesz +1 do bonusowych obrażeń)")
                time.sleep(2.5)
            if nauka == 2:
                Bonus_Hp += 3
                print("Nauczyłeś się co robić gdy jesteś ranny (Zyskujesz +3 bonusowych punktów zdrowia)")
                time.sleep(2.5)
            if nauka == 3:
                Exp += 75
                print("Mędrzec opowiada ci swoją historię (Zyskujesz +75 punktów doświadczenia)")
                time.sleep(2.5)
    elif medrec == "2":
        print("Odrzuciłeś ofertę i idziesz dalej")
        time.sleep(1.5)
    else:
        print("Podałeś zła liczbę")
        master()
def bandit():
    global gold,weapon,bow,life,Imie,Exp,Hp,Dmg,Bonus_Hp,Arena,arrows
    print(r"                                     ")
    print(r"              :'._.':                ")
    print(r"           ,-:       :-,             ")
    print(r"         :  :         :  :           ")
    print(r"          '. '-._ _.-' .'            ")
    print(r"           ( '-._ _.-' )             ")
    print(r"           *:,_  I  _,:*             ")
    print(r"            \  `'-'`  /              ")
    print(r"             '.     .'               ")
    print(r"              | ';' |                ")
    print(r"        ..---' '-.-' '---..          ")
    print(r"      /  | | \              \        ")
    print(r"     |   \  \  ''--.,__      |       ")
    print(r"     |    \  '-.,_      ''--.|       ")
    print("Napotykasz na swojej drodze bandytę, który rząda od ciebie pieniędzy")
    print("-"*40)
    rob = 8
    if gold > 0:
        if rob <= gold:
            rob = 8
        elif rob > gold:
            rob = gold
        print(f"Co robisz:\n1-Oddajesz mu {rob} monet\n2-Postanawiasz z nim walczyć\n3-Próbujesz uciec")
        decyzja = input()
        if decyzja == "1":
            gold -= rob
            print(f"Bandyta zabiera ci {rob} monet")
            time.sleep(1.5)
        elif decyzja == "2":
            print("Stajesz do walki z bandytą")
            time.sleep(0.6)
            bandit_fight()
        elif decyzja == "3":
            ucieczka = randint(1,3)
            if ucieczka == 3:
                print("Udało ci się uciec nie oddając żadnych pieniędzy")
                time.sleep(2)
            else:
                print("Zostałeś ugodzony sztyletem, ale za nim bandytą zdążył zadać drugi cios udało ci się uciec\nTracisz 20 punktów zdrowia")
                time.sleep(2.5)
                life -=20
        else:
            print("Podałeś złą liczbę")
            bandit()
    elif gold == 0:
        print("Nie masz żadnych pieniędzy do oddania więc musisz z nim walczyć")
        time.sleep(0.8)
        bandit_fight()
def bandit_fight():
    global gold,weapon,bow,life,Imie,Exp,Hp,Dmg,Arena,arrows
    if Arena == 1:
        Opponent = ["Bandytą", 35, 12, 15, 20]
    if Arena == 2:
        Opponent = ["Bandytą", 65, 20, 25, 30]
    while life >= 1:
        print(f"Walczysz z {Opponent[0]}")
        print(f"Przeciwnik ma {Opponent[1]} Hp i zadaje ci {Opponent[2]} obrażeń")
        life = life - Opponent[2]
        time.sleep(0.5)
        if life <= 0:
            break
        print(f"Zostało ci {life} Hp")
        atak = atack(weapon,bow)+Dmg
        Opponent[1] = Opponent[1] - atak
        print(f"Zadałeś {atak} obrażeń")
        time.sleep(0.6)
        if Opponent[1] <= 0:
            print("-"*40)
            print('Zabiłeś bandytę')
            time.sleep(0.8)
            gold = gold+Opponent[3]
            Exp = Exp+Opponent[4]
            break
sklep_i_arena()
