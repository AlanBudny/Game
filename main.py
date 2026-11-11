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
#------------------Składniki Artefaktów
elficka_tkanina = 0
goblini_samorodek_zlota = 0
krasnoludzki_stop_metali = 0
#------------------Artefakty
elficka_bransoletka_madrosci = ""
elficka_bransoletka_madrosci_stat = 1
naszyjnik_sily = ""
naszyjnik_sily_stat = 1
pierscien_wytrzymalosci = ""
pierscien_wytrzymalosci_stat = 1
#------------------eliksiry
heal_potion = 0
burn_potion = 0
weakness_potion = 0
strength_potion = 0
heal_potion_stat = 15
burn_potion_stat = 4
weakness_potion_stat = 0.6
strength_potion_stat = 1.5
burn_effect = 0
strength_effect = 0
weakness_effect = 0
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
def attack():
    print("1 - Normalny atak")
    print(f"2 - Strzał z łuku (masz {arrows} strzał)")
    print("3 - Użyj eliksiru")
    w_atak = input()
    if w_atak == "1":
        sword_attack()
    elif w_atak == "2":
        bow_attack()
    elif w_atak == "3":
        potion_use()
    else:
        print("Podałeś złą liczbę")
        attack()
def sword_attack():
    global weapon,damage, strength_effect, strength_potion_stat, naszyjnik_sily_stat
    print("1=normalny atak")
    if weapon == "drewniany miecz":
        damage = randint(5,10)
    if weapon == "kamienny miecz":
        damage = randint(8,13)
    if weapon == "żelazny miecz":
        damage = randint(12,17)
    if weapon == "platynowy miecz":
        damage = randint(16,21)
    if weapon == "boski miecz":
        damage = randint(20,25)
    damage = int(damage*naszyjnik_sily_stat)
    if strength_effect > 0:
        strength_effect -= 1
        print("Twój atak został wzmocniony przez miksturę siły")
        damage = int(damage*strength_potion_stat)
    return damage
def bow_attack():
    global arrows, bow, damage, strength_effect, strength_potion_stat, naszyjnik_sily_stat
    if arrows > 0:
        arrows -= 1
        if bow == "stary łuk":
            damage = randint(8,18)
        if bow == "nowy łuk":
            damage = randint(20,30)
        damage = int(damage*naszyjnik_sily_stat)
        if strength_effect > 0:
            strength_effect -= 1
            print("Twój atak został wzmocniony przez miksturę siły")
            damage = int(damage*strength_potion_stat)
        return damage
    else:
        print("Nie masz strzał")
        return attack()
def potion_attack():
    global heal_potion, heal_potion_stat, burn_potion, strength_potion, weakness_potion, life, burn_effect, strength_effect, weakness_effect
    print("Której mikstury chcesz użyć:")
    print(f"1 - Mikstura Życia x{heal_potion}")
    print(f"2 - Mikstura Płomieni x{burn_potion}")
    print(f"3 - Mikstura Siły x{strength_potion}")
    print(f"4 - Mikstura Osłabienia x{weakness_potion}")
    print(f"5 - Powrót")
    elixir = input()
    if elixir == "1":
        if heal_potion > 0:
            heal_potion -= 1
            life += heal_potion_stat
            print(f"Zyskujesz {heal_potion_stat} punktów zdrowia")
        else:
            print("Nie masz żadnych mikstur zdrowia")
            potion_attack()
    elif elixir == "2":
        if burn_potion > 0:
            burn_potion -= 1
            burn_effect += 3
            print(f"Podpalasz przeciwnika na {burn_effect} tury")
        else:
            print("Nie masz żadnych mikstur płomienia")
            potion_attack()
    elif elixir == "3":
        if strength_potion > 0:
            strength_potion -= 1
            strength_effect = 2
            print(f"Wzmacniasz się na {strength_effect} tury")
        else:
            print("Nie masz żadnych mikstur siły")
            potion_attack()
    elif elixir == "4":
        if weakness_potion > 0:
            weakness_potion -= 1
            weakness_effect = 2
            print(f"Osłabiasz przeciwnika na {weakness_effect} tury")
        else:
            print("Nie masz żadnych mikstur osłabienia")
            potion_attack()
    elif elixir == "5":
        attack()
    else:
        print("Podałeś złą liczbę")
        potion_attack()
def potion_use():
    potion_attack()
    print("1 - Normalny atak")
    print(f"2 - Strzał z łuku (masz {arrows} strzał)")
    w_atak2 = input()
    if w_atak2 == "1":
        sword_attack()
    elif w_atak2 == "2":
        bow_attack()
    else:
        potion_use()

#---------------------------------Karczma
def karczma():
    global gold
    print(r"                                                                                                 ")
    print(r"                          _._                                                                    ")
    print(r"                        {>=-=<}                                           _______________        ")
    print(r"                        (  .  )                                          /              /|       ")
    print(r"        ||              :`>=<`:                                         '         |_|  / |       ")
    print(r"       :``:          .'' '-.-' ''.         ||                          ' ||           /  |       ")
    print(r"_______|[]|__________|___________|________/><\_______,.,_____________,' :``||  |_|   /   |       ")
    print(r"|_|    |__|                               \__/       ) (                |=:``:      /    |       ")
    print(r"    :-:    (_)     :--:        ||                   (___)               |_|==|     /     |       ")
    print(r"    |_|            |__|       (__)                                        |__|    /      |       ")
    print(r"_________________________________________________________________________________/|      |       ")
    print(r"| |\ \    / /| |\ \    / /| |\ \    / /| |\ \    / /| |\ \    / /| |\ \    / /| | |     /        ")
    print(r"| | \ \  / / | | \ \  / / | | \ \  / / | | \ \  / / | | \ \  / / | | \ \  / / | | |    /         ")
    print(r"| |  \ \/ /  | |  \ \/ /  | |  \ \/ /  | |  \ \/ /  | |  \ \/ /  | |  \ \/ /  | | |   /          ")
    print(r"| |   \ \/   | |   \ \/   | |   \ \/   | |   \ \/   | |   \ \/   | |   \ \/   | | |  /           ")
    print(r"| |   ^  \   | |   ^  \   | |   ^  \   | |   ^  \   | |   ^  \   | |   ^  \   | | | /            ")
    print(r"| |  / /\ \  | |  / /\ \  | |  / /\ \  | |  / /\ \  | |  / /\ \  | |  / /\ \  | | |/             ")
    print(r"| | / /  \ \ | | / /  \ \ | | / /  \ \ | | / /  \ \ | | / /  \ \ | | / /  \ \ | | /              ")
    print(r"| |/ /    \ \| |/ /    \ \| |/ /    \ \| |/ /    \ \| |/ /    \ \| |/ /    \ \| |/               ")
    print(r" ````````````````````````````````````````````````````````````````````````````````                ")
    print("Witaj w Karczmie")
    print("Po co przychodzisz?:\n1-Napić się(3G)\n2-Zagrać w Kubki(10G)\n3-Wyjdż z Karczmy")
    wybor = int(input())
    if wybor == 1:
        if gold >= 3:
            print(r"                                        ")
            print(r"          __ ---- __                    ")
            print(r"        |`-- ____ --`|                  ")
            print(r"        |': . __ . :'=::.               ")
            print(r"        | |  :  :  | | ::               ")
            print(r"        | |  |  |  | | ::               ")
            print(r"        | |  |  |  | =::'               ")
            print(r"        | '  :  :  ' |                  ")
            print(r"        ' -- ____ -- '                  ")
            print(r"                                        ")
            print("Wypijasz Piwo")
            gold -= 3
            time.sleep(0.8)
        else:
            print("Nie stać cię")
            time.sleep(0.5)
        karczma()
    elif wybor == 2:
        if gold >= 10:
            print("Podążaj za kulką. Jeśli ją znajdziesz zyskasz 10 monet, w przeciwnym wypadku stracisz 10 monet")
            time.sleep(1.5)
            kubeczki()
        else:
            print("Nie stać cię")
            time.sleep(0.8)
            karczma()
    elif wybor == 3:
        sklep_i_arena()
    else:
        print("Podałeś złą liczbę")
        time.sleep(0.5)
#---------------------------------Arena
def arena():
#    0-nazwa, 1-życie, 2-obrażenia, 3-gold, 4-EXP
    global pierscien_wytrzymalosci_stat,elficka_bransoletka_madrosci_stat,gold,weapon,bow,life,Imie,Exp,Hp,Dmg,Bonus_Hp,Arena,arrows, burn_effect, strength_effect, weakness_effect, elficka_tkanina, goblini_samorodek_zlota, krasnoludzki_stop_metali
    if Arena < 2:
        locked = "Zablokowane"
    if Arena >= 2:
        locked = " "
    liczba_pokonanych_przeciwnikow = 0
    y = -1
    print("Gdzie chcesz się udać:\n1-Dziki Las\n2-Zniszczone Przedmieścia ""\033[1m" + f"\033[31m{locked}\033[0m" + "\033[0m""\n3-powrót")
    miejsce = input()
    if miejsce == "3":
        sklep_i_arena()
    elif miejsce == "1":
        picked_arena = 1
    elif miejsce == "2":
        if Arena >= 2:
            picked_arena = 2
        else:
            print("Nie odblokowałeś jeszcze tej krainy")
            arena()
    else:
        print("Podałeś złą liczbę")
        arena()
    life = int((Hp + Bonus_Hp)*pierscien_wytrzymalosci_stat)
    while life >= 1:
        if picked_arena == 1:
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
            print(r"      _-' ; :  ' __ ''  ,. '-_                 .',__;'.                 <.- ' , '' , ' -.>   ")
            print(r"  _-' ;  ; __,.-'  '-.,__ ,   ;'-_           <.-',--,'-.>                , ` _,....,_ ` ,    ")
            print(r"<_,..-- ''_-': . : .  ,'-'' --..,_>            .':__''.                <.- ' , '  ' , ' -.>  ")
            print(r"      _-' ; :  ' __ ''  ,. '-_               <.-',--,'-.>               , ` _,..--..,_ ` ,   ")
            print(r"  _-' ;  ; __,.-'/|'-.,__ ,   ;'-_             .'.__.'.               <.- ' , '    ' , ' -.> ")
            print(r"<_,..-- ''    ||/ }\ ||   '' --..,_>     __,.<.-'|\||'-.>   |  |       , ` _,..----..,_ ` ,  ")
            print(r"___,..-- ''`' ||\{;/\)| ' -..__,.,_,.-''  __,.._ ''.|-.,__,.|\/|,    <.- '   |      |   ' -.>")
            print(r"              '-.,.,.-' .,.;:.;.,      ,-{  [)  \                '' -- .,___,'-.,,.-',__     ")
            print(r"    .,;';,.                           /__  /_|_ _)    ,.;';.                             ''-.")
            print("Wędrujesz dalej w głąb lasu")
            dwarf = ["Krasnoludem",45,6,15,20] #Arena 1
            goblin = ["Goblinem",30,10,10,15] #Arena 1
            elf = ["Elfem",20,12,10,10]       #Arena 1    
            list_Opponents = [dwarf,goblin,elf]
        elif picked_arena == 2:
            print("Wędrujesz dalej mijając zniszczone budynki")
            knight = ["Mrocznym Rycerzem",50,18,30,40]      #Arena 2
            giant = ["Olbrzymem",80,12,35,45]               #Arena 2  
            ogre = ["Ogrem",60,16,30,40]          #Arena 2
            list_Opponents = [knight,giant,ogre]
        time.sleep(1.5)
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
                if picked_arena == 1:
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
                    if x == 2:
                        print(r"                  ,dM                                      ")
                        print(r"                 dMMP                                      ")
                        print(r"                dMMM'                                      ")
                        print(r"                \MM/                                       ")
                        print(r"                dMMm.                                              ,1              __        ")
                        print(r"               dMMP'_\---.                                        //\            _,.  \      ")
                        print(r"              _| _  p ;88;`.                                     //  \           /   \ \     ")
                        print(r"            ,db; p >  ;8P|  `.                                  //    \         _|    ) |'`) ")
                        print(r"           (``T8b,__,'dP |   |                                 //      \  ,.- ' _\ _ /  |-'  ")
                        print(r"           |   `Y8b..dP  ;_  |                             <--((-------<<)_ = '      |  |    ")
                        print(r"           |    |`T88P_ /  `\;                                (><)_==______]_____/   |  |    ")
                        print(r"           :_.-~|d8P'`Y/    /                                   \\    /          \    \/     ")
                        print(r"            \_   TP    ;   7`\.                                  \\  /           /______\    ")
                        print(r" ,,__        >   `._  /'  /   `\_                                 \\/            |\/\/\/|    ") 
                        print(r" `._ ''''~~~~------|`\;' ;     ,'                                  `1         _.' \/\/\/\|   ")
                        print(r"    '''~~~-----~~~'\__[|;' _.-'  `\.                                      ,-'`   _'`/\` `    ")
                        print(r"            ;--..._     .-'-._     ;                                     (   ,-''    |  |    ")
                        print(r"           /      /`~~.'   ,'`\_ ,/.                                     |  |        |  |    ")
                        print(r"          ;_    /'        /    ,/                                        /  |        (  |    ")
                        print(r"          | `~-l         ;    /                                        <__,.._       |  |    ")
                        print(r"__________`\    ;_______/\.._|_______________________________________,-{  [)  \______/  |_____________")
                        print(r"            \    \      \     \.                                    /__  /_|_ _)  < . _.;    ")
                        print(r"            /`---';      `----'                                                              ")
                        print(r"           (     /                                                                           ")
                        print(r"            `---'                                                                            ")
                if picked_arena == 2: 
                    if x == 2:
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
                recieved_damage = Opponent[2]
                if weakness_effect > 0:
                    weakness_effect -= 1
                    recieved_damage = int(recieved_damage * weakness_potion_stat)
                    print("Przeciwnik jest osłabiony")
                print(f"Przeciwnik ma {Opponent[1]} Hp i zadaje ci {recieved_damage} obrażeń")
                life = life - recieved_damage
                time.sleep(0.5)
                if life <= 0:
                    break
                print(f"Zostało ci {life} Hp")
                attack()
                atak = damage+Dmg
                Opponent[1] = Opponent[1] - atak
                print(f"Zadałeś {atak} obrażeń")
                time.sleep(0.5)
                if burn_effect > 0:
                    burn_effect -= 1
                    Opponent[1] -= burn_potion_stat
                    print(f"Przeciwnik traci {burn_potion_stat} punktów zdrowia od ognia")
                time.sleep(0.5)
                if Opponent[1] <= 0:
                    print("-"*40)
                    print('Zabiłeś przeciwnika')
                    burn_effect = 0
                    weakness_effect = 0
                    gold = gold+Opponent[3]
                    liczba_pokonanych_przeciwnikow = liczba_pokonanych_przeciwnikow+1
                    Exp = Exp+int((Opponent[4])*elficka_bransoletka_madrosci_stat)
                    print(f"Zdobywasz {Opponent[3]} monet i {int((Opponent[4])*elficka_bransoletka_madrosci_stat)} punktów doświadczenia")
                    loot_chance = randint(1,2)
                    if loot_chance == 1:
                        drop_ammount = randint(1,2)
                        if Opponent[0] == "Krasnoludem":
                            krasnoludzki_stop_metali += drop_ammount
                            print(f"Oraz zdobywasz x{drop_ammount} krasnoludzkiego stopu metali")
                        if Opponent[0] == "Elfem":
                            elficka_tkanina += drop_ammount
                            print(f"Oraz zdobywasz x{drop_ammount} elfickiej tkaniny")
                        if Opponent[0] == "Goblinem":
                            goblini_samorodek_zlota += drop_ammount
                            print(f"Oraz zdobywasz x{drop_ammount} gobliniego samorodka złota")
                    time.sleep(2)
            if liczba_pokonanych_przeciwnikow > 7 and picked_arena == 1:
                print("Przeszedłeś przez Dziki Las")
                Arena = max(2, Arena)
                sklep_i_arena()
            if liczba_pokonanych_przeciwnikow > 7 and picked_arena == 2:
                print("Przeszedłeś przez Zniszczone Przedmieścia")
                Arena = max(3, Arena)
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
    strength_effect = 0
    print("zginąłeś")
    print("pokonałeś",liczba_pokonanych_przeciwnikow,"przeciwników")
    time.sleep(1)
    sklep_i_arena()
#---------------------------------Alchemik
def alchemik():
    global gold, heal_potion, heal_potion_stat, burn_potion, strength_potion, weakness_potion, burn_potion_stat, strength_potion_stat, weakness_potion_stat
    print(r"                   '                ")
    print(r"             '  O        ,          ")
    print(r"          .          o  ,.          ")
    print(r"                  '    //           ")
    print(r"          _ .O -.-- - //. _         ")
    print(r"      _:- . _        ''_ . -:_      ")
    print(r"     '--'      ` '' `      '--'     ")
    print(r"       '                    '       ")
    print(r"        :                  :        ")
    print(r"         '.  .        .  .'         ")
    print(r"           ':'.. __ ..':'           ")
    print(r"___________::____::____::___________")
    print(r"         o:.'    ''    '.:o         ")
    print(r"                                    ")
    print("Witaj u Alchemika")
    print("Która mikstura cię interesuje:\n1-Mikstura Życia\n2-Mikstura Płomienia\n3-Mikstura Siły\n4-Mikstura Osłabienia\n5-Powrót")
    alchem = input()
    if alchem == "1":
        print(r"                          ")
        print(r"         C:::Ↄ             ")
        print(r"          | |              ")
        print(r"          | |              ")
        print(r"         .' '.             ")
        print(r"      .'..___..'.          ")
        print(r"     :--..___..--:         ")
        print(r"      '._______.'          ")
        print(r"                          ")
        print("     Mikstura Życia")
        print(f"Zyskujesz {heal_potion_stat} punktów zdrowia")
        print("       Koszt: 10G")
        print("1 - Kupno")
        print("2 - Powrót")
        shop_alchem = input()
        if shop_alchem == "1":
            if gold >= 10:
                gold -= 10
                heal_potion += 1
                print("Zakupiłeś Miksturę Życia")
                print("-"*40)
            else:
                print("Nie stać cię")
                print("-"*40)
            alchemik()
        else:
            print("-"*40)
            alchemik()
    elif alchem == "2":
        print(r"                                ")
        print(r"                 C:Ↄ              ")
        print(r"                 : :              ")
        print(r"                /   \             ")
        print(r"               /     \            ")
        print(r"              /-.___.-\           ")
        print(r"              \-.___.-/           ")
        print(r"               \_____/            ")
        print(r"                                 ")
        print("          Mikstura Płomienia")
        print(f"Przeciwnik traci {burn_potion_stat} punktów zdrowia przez 3 tury")
        print("              Koszt: 8G")
        print("1 - Kupno")
        print("2 - Powrót")
        shop_alchem = input()
        if shop_alchem == "1":
            if gold >= 8:
                gold -= 8
                burn_potion += 1
                print("Zakupiłeś Miksturę Płomieni")
                print("-"*40)
            else:
                print("Nie stać cię")
                print("-"*40)
            alchemik()
        else:
            print("-"*40)
            alchemik()
    elif alchem == "3":
        print(r"                               ")
        print(r"              C:Ↄ              ")
        print(r"              | |              ")
        print(r"            ..' '..            ")
        print(r"           |_______|           ")
        print(r"           |_______|           ")
        print(r"           |       |           ")
        print(r"           :_______:           ")
        print(r"                               ")
        print("         Mikstura Siły")
        strength = (strength_potion_stat - 1)*100
        print(f"Zyskujesz o {strength}% wzmocnioną siłę")
        print("           Koszt: 12G")
        print("1 - Kupno")
        print("2 - Powrót")
        shop_heal = input()
        if shop_heal == "1":
            if gold >= 12:
                gold -= 12
                strength_potion += 1
                print("Zakupiłeś Miksturę Siły")
                print("-"*40)
            else:
                print("Nie stać cię")
                print("-"*40)
            alchemik()
        else:
            print("-"*40)
            alchemik()
    elif alchem == "4":
        print(r"                                 ")
        print(r"                C:Ↄ              ")
        print(r"                : :              ")
        print(r"               .' '.             ")
        print(r"               |   |             ")
        print(r"               |._.|             ")
        print(r"               |._.|             ")
        print(r"               |   |             ")
        print(r"               '._.'             ")
        print(r"                                 ")
        print("        Mikstura Osłabienia")
        weak = (1 - weakness_potion_stat)*100
        print(f"Ataki przeciwnika są osłabione o {weak}%")
        print("            Koszt: 12G")
        print("1 - Kupno")
        print("2 - Powrót")
        shop_heal = input()
        if shop_heal == "1":
            if gold >= 12:
                gold -= 12
                weakness_potion += 1
                print("Zakupiłeś Miksturę Osłabienia")
                print("-"*40)
            else:
                print("Nie stać cię")
                print("-"*40)
            alchemik()
        else:
            print("-"*40)
            alchemik()
    else:
        sklep_i_arena()
#---------------------------------Artefakty
def artefacts():
    global gold, krasnoludzki_stop_metali, goblini_samorodek_zlota, elficka_tkanina, elficka_bransoletka_madrosci, elficka_bransoletka_madrosci_stat, naszyjnik_sily, naszyjnik_sily_stat, pierscien_wytrzymalosci, pierscien_wytrzymalosci_stat
    print("Witaj u Rzemieślnika")
    print("Który artefakt cię interesuje:")
    print(f"1-Elficka Bransoletka Mądrości \033[32m {elficka_bransoletka_madrosci} \033[0m")
    print(f"2-Naszyjnik Siły \033[32m {naszyjnik_sily} \033[0m")
    print(f"3-Pierścień Wytrzymałości \033[32m {pierscien_wytrzymalosci} \033[0m")
    print("4-Powrót")
    artefacts_choice = input()
    if artefacts_choice == "1":
        print("                Elficka Bransoletka Mądrości")
        print("Zwiększa otrzymywane punkty doświadczenia z przeciwników o 50%")
        print(f"Cena:\n{krasnoludzki_stop_metali}/3 Krasnoludzkiego Stopu Metali\n{elficka_tkanina}/5 Elfickiej Tkaniny\n{gold}/30 monet")
        print("1-Kupno\n2-Powrót")
        decision = input()
        if decision == "1" and elficka_bransoletka_madrosci == "":
            if krasnoludzki_stop_metali >= 3 and elficka_tkanina >= 5 and gold >= 30:
                krasnoludzki_stop_metali -= 3
                elficka_tkanina -= 5
                gold -= 30
                elficka_bransoletka_madrosci = "Wyposażone"
                elficka_bransoletka_madrosci_stat = 1.5
                print("Kupiłeś Elficką Bransoletkę Mądrości")
                sklep_i_arena()
            else:
                print("Nie masz wszystkich składników")
                artefacts()
        elif decision == "1" and elficka_bransoletka_madrosci == "Wyposażone":
            print("Posiadasz już ten przedmiot")
            artefacts()
        else:
            artefacts()
    elif artefacts_choice == "2":
        print("                      Naszyjnik Siły")
        print("Zwieksza zadawane przez ciebie niemagiczne obrażenia o 25%")
        print(f"Cena:\n{krasnoludzki_stop_metali}/2 Krasnoludzkiego Stopu Metali\n{goblini_samorodek_zlota}/6 Goblinich Samorodków Złota\n{gold}/40 monet")
        print("1-Kupno\n2-Powrót")
        decision = input()
        if decision == "1" and naszyjnik_sily == "":
            if krasnoludzki_stop_metali >= 2 and goblini_samorodek_zlota >= 6 and gold >= 40:
                krasnoludzki_stop_metali -= 2
                goblini_samorodek_zlota -= 6
                gold -= 40
                naszyjnik_sily = "Wyposażone"
                naszyjnik_sily_stat = 1.25
                print("Kupiłeś Naszyjnik Siły")
                sklep_i_arena()
            else:
                print("Nie masz wszystkich składników")
                artefacts()
        elif decision == "1" and naszyjnik_sily == "Wyposażone":
            print("Posiadasz już ten przedmiot")
            artefacts()
        else:
            artefacts()
    elif artefacts_choice == "3":
        print("      Pierścień Wytrzymałości")
        print("Zwieksza twoje punkty zdrowia o 25%")
        print(f"Cena:\n{krasnoludzki_stop_metali}/8 Krasnoludzkiego Stopu Metali\n{gold}/50 monet")
        print("1-Kupno\n2-Powrót")
        decision = input()
        if decision == "1" and pierscien_wytrzymalosci == "":
            if krasnoludzki_stop_metali >= 8 and gold >= 50:
                krasnoludzki_stop_metali -= 8
                gold -= 50
                pierscien_wytrzymalosci = "Wyposażone"
                pierscien_wytrzymalosci_stat = 1.25
                print("Kupiłeś Pierścień Wytrzymałości")
                sklep_i_arena()
            else:
                print("Nie masz wszystkich składników")
                artefacts()
        elif decision == "1" and pierscien_wytrzymalosci == "Wyposażone":
            print("Posiadasz już ten przedmiot")
            artefacts()
        else:
            artefacts()
    else:
        sklep_i_arena()
#---------------------------------Sklep
def sklep_i_arena():
    print("-"*40)
    global pierscien_wytrzymalosci_stat,arrows,gold,weapon,bow,life,Imie,Exp,Hp,Dmg,Bonus_Hp,Arena,s_zbroja,z_zbroja,p_zbroja,s_zbroja_cena,z_zbroja_cena,p_zbroja_cena,k_miecz,z_miecz,p_miecz,b_miecz,k_miecz_cena,z_miecz_cena,p_miecz_cena,b_miecz_cena,n_luk,n_luk_cena, elficka_tkanina, goblini_samorodek_zlota, krasnoludzki_stop_metali
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
    print("Gdzie chcesz iść:\n1-Kowal\n2-Zbrojmistrz\n3-Łucznik\n4-Alchemik\n5-Artefakty\n6-Karczma\n7-Podróż\n8-Ekwipunek i Statystyki")
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
        print(r"     ;;        ,-'     ';;'             ")
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
        alchemik()
    if czynnosc == "5":
        artefacts()
    if czynnosc == "6":
        karczma()
    if czynnosc == "7":
        print("-"*40)
        arena()
    if czynnosc == "8":
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
        print(f"\033[32mWyposażony ekwipunek:\n{weapon}\n{bow}\n{arrows} strzał\033[0m")
        print(f"Mikstura Życia x{heal_potion}\nMikstura Płomieni x{burn_potion}\nMikstura Siły x{strength_potion}\nMikstura Osłabienia x{weakness_potion}")
        print(f"\033[32mSkładniki:\nKrasnoludzki stop metali x{krasnoludzki_stop_metali}\nElficka tkanina x{elficka_tkanina}\nGoblini samorodek złota x{goblini_samorodek_zlota}\033[0m")
        if Hp == 100:
            print("brak zbroi")
        if Hp == 125:
            print("skórzana zbroja")
        if Hp == 150:
            print("żelazna zbroja")
        if Hp == 200:
            print("platynowa zbroja")
        print(f"{int((Hp+Bonus_Hp)*pierscien_wytrzymalosci_stat)} Punktów zdrowia")
        print(f"{Dmg} Bonusowych obrażeń")
        time.sleep(1)
        sklep_i_arena()
    else:
        print("Podałeś złą liczbę")
        sklep_i_arena()
#-----------------------------------losowe zdarzenia
def mimic():
    global gold,life,arrows, heal_potion, strength_potion, weakness_potion, burn_potion
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
                print(f"Otwierasz skrzynię i znajdujesz w niej {gold_chest} monet\nOraz {arrows_chest} strzały")
                time.sleep(2)
            elif loot == 2:
                gold_chest = randint(10,15)
                gold += gold_chest
                print(f"Otwierasz skrzynię i znajdujesz w niej {gold_chest} monet")
                time.sleep(2)
            elif loot == 1:
                gold_chest = randint(5,10)
                gold += gold_chest
                print(f"Otwierasz skrzynię i znajdujesz w niej {gold_chest} monet")
                mixture = randint(1,4)
                if mixture == 1:
                    heal_potion += 1
                    print("Oraz Miksturę Życia")
                elif mixture == 2:
                    burn_potion += 1
                    print("Oraz Miksturę Płomienia")
                elif mixture == 3:
                    strength_potion += 1
                    print("Oraz Miksturę Siły")
                else:
                    weakness_potion += 1
                    print("Oraz Miksturę Osłabienia")
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
        print("Co robisz:\n1-Postanawiasz z nim walczyć\n2-Próbujesz uciec")
        decyzja = input()
        if decyzja == "1":
            print("Stajesz do walki z bandytą")
            time.sleep(0.6)
            bandit_fight()
        elif decyzja == "2":
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
def bandit_fight():
    global gold,weapon,bow,life,Imie,Exp,Hp,Dmg,Arena,arrows, burn_effect, strength_effect, weakness_effect
    Opponent = ["Bandytą", 35, 12, 15, 20]
    while life >= 1:
        print(f"Walczysz z {Opponent[0]}")
        recieved_damage = Opponent[2]
        if weakness_effect > 0:
            weakness_effect -= 1
            recieved_damage = int(recieved_damage * weakness_potion_stat)
            print("Przeciwnik jest osłabiony")
        print(f"Przeciwnik ma {Opponent[1]} Hp i zadaje ci {recieved_damage} obrażeń")
        life = life - recieved_damage
        time.sleep(0.5)
        if life <= 0:
            break
        print(f"Zostało ci {life} Hp")
        attack()
        atak = damage+Dmg
        Opponent[1] = Opponent[1] - atak
        print(f"Zadałeś {atak} obrażeń")
        time.sleep(0.5)
        if burn_effect > 0:
            burn_effect -= 1
            Opponent[1] -= burn_potion_stat
            print(f"Przeciwnik traci {burn_potion_stat} punktów zdrowia od ognia")
        time.sleep(0.5)
        if Opponent[1] <= 0:
            print("-"*40)
            burn_effect = 0
            weakness_effect = 0
            print('Zabiłeś bandytę')
            time.sleep(0.8)
            gold = gold+Opponent[3]
            Exp = Exp+Opponent[4]
            break
def kubeczki():
    global gold
    delay = 0.25
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
    print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
    print(r"_____|                  |____|                  |____|                  |_____")
    print(r"     |                  |    |                  |    |                  |     ")
    print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
    print(r"                                                                              ")
    time.sleep(delay)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
    print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
    print(r"     |                  |    |                  |    |                  |     ")
    print(r"_____|                  |____|                  |____|                  |_____")
    print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
    print(r"                                      ''                                      ")
    print(r"                                                                              ")

    time.sleep(delay)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
    print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
    print(r"     |                  |    |                  |    |                  |     ")
    print(r"     |                  |    |                  |    |                  |     ")
    print(r"_____'_-- .. ____ .. --_'____'_-- .. ____ .. --_'____'_-- .. ____ .. --_'_____")
    print(r"                                     '--'                                     ")
    print(r"                                                                              ")
    print(r"                                                                              ")
    time.sleep(delay)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
    print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
    print(r"     |                  |    |                  |    |                  |     ")
    print(r"     |                  |    |                  |    |                  |     ")
    print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
    print(r"____________________________________(    )____________________________________")
    print(r"                                     '--'                                     ")
    print(r"                                                                              ")
    print(r"                                                                              ")
    time.sleep(delay)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
    print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
    print(r"     |                  |    |                  |    |                  |     ")
    print(r"     |                  |    |                  |    |                  |     ")
    print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
    print(r"                                     .--.                                     ")
    print(r"____________________________________(    )____________________________________")
    print(r"                                     '--'                                     ")
    print(r"                                                                              ")
    print(r"                                                                              ")
    time.sleep(delay*4)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
    print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
    print(r"     |                  |    |                  |    |                  |     ")
    print(r"     |                  |    |                  |    |                  |     ")
    print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
    print(r"____________________________________(    )____________________________________")
    print(r"                                     '--'                                     ")
    print(r"                                                                              ")
    print(r"                                                                              ")
    time.sleep(delay)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
    print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
    print(r"     |                  |    |                  |    |                  |     ")
    print(r"     |                  |    |                  |    |                  |     ")
    print(r"_____'_-- .. ____ .. --_'____'_-- .. ____ .. --_'____'_-- .. ____ .. --_'_____")
    print(r"                                     '--'                                     ")
    print(r"                                                                              ")
    print(r"                                                                              ")
    time.sleep(delay)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
    print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
    print(r"     |                  |    |                  |    |                  |     ")
    print(r"_____|                  |____|                  |____|                  |_____")
    print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
    print(r"                                      ''                                      ")
    print(r"                                                                              ")
    time.sleep(delay)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
    print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
    print(r"_____|                  |____|                  |____|                  |_____")
    print(r"     |                  |    |                  |    |                  |     ")
    print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
    print(r"                                                                              ")
    pozycja = 2
    czasruchu = 0.015
    for i in range(randint(20,30)):
        pierwszy_kubek = randint(1,3)
        drugi_kubek = randint(1,3)
        while drugi_kubek == pierwszy_kubek:
            drugi_kubek = randint(1,3)
        if (pierwszy_kubek == 2 and drugi_kubek == 1) or (pierwszy_kubek == 1 and drugi_kubek == 2):
            if pozycja == 2:
                pozycja = 1
            elif pozycja == 1:
                pozycja = 2
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                _. . -- . ._                                 ")
            print(r"                             .'-. .  __  . .-'.          _. . -- . ._         ")
            print(r"          _. . -- . ._       :                :       .'-. .  __  . .-'.      ")
            print(r"       .'-. .  __  . .-'.    :                :       :                :      ")
            print(r"       :                :    |                |       :                :      ")
            print(r"       :                :    |                |       |                |      ")
            print(r"       |                |   .' - .. ____ .. - '.      |                |      ")
            print(r"       |                |   |                  |     .' - .. ____ .. - '.     ")
            print(r"______.' - .. ____ .. - '.__|                  |_____|                  |_____")
            print(r"      |                  |  ' -- .. ____ .. -- '     |                  |     ")
            print(r"      |                  |                           ' -- .. ____ .. -- '     ")
            print(r"      ' -- .. ____ .. -- '                                                    ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                               _. . -- . ._                                   ")
            print(r"                            .'-. .  __  . .-'.           _. . -- . ._         ")
            print(r"           _. . -- . ._     :                :        .'-. .  __  . .-'.      ")
            print(r"        .'-. .  __  . .-'.  :                :        :                :      ")
            print(r"        :                :  |                |        :                :      ")
            print(r"        :                :  |                |        |                |      ")
            print(r"        |                | .' - .. ____ .. - '.       |                |      ")
            print(r"        |                | |                  |      .' - .. ____ .. - '.     ")
            print(r"_______.' - .. ____ .. - '.|                  |______|                  |_____")
            print(r"       |                  |' -- .. ____ .. -- '      |                  |     ")
            print(r"       |                  |                          ' -- .. ____ .. -- '     ")
            print(r"       ' -- .. ____ .. -- '                                                   ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                             _. . -- . ._                                     ")
            print(r"                          .'-. .  __  . .-'.             _. . -- . ._         ")
            print(r"             _. . -- . ._ :                :          .'-. .  __  . .-'.      ")
            print(r"          .'-. .  __  . .-'.               :          :                :      ")
            print(r"          :                :               |          :                :      ")
            print(r"          :                :               |          |                |      ")
            print(r"          |                |- .. ____ .. - '.         |                |      ")
            print(r"          |                |                |        .' - .. ____ .. - '.     ")
            print(r"_________.' - .. ____ .. - '.               |________|                  |_____")
            print(r"         |                  | .. ____ .. -- '        |                  |     ")
            print(r"         |                  |                        ' -- .. ____ .. -- '     ")
            print(r"         ' -- .. ____ .. -- '                                                 ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                           _. . -- . ._                                       ")
            print(r"                        .'-. .  __  . .-'.               _. . -- . ._         ")
            print(r"               _. . -- .'.               :            .'-. .  __  . .-'.      ")
            print(r"            .'-. .  __  . .-'.           :            :                :      ")
            print(r"            :                :           |            :                :      ")
            print(r"            :                :           |            |                |      ")
            print(r"            |                | ____ .. - '.           |                |      ")
            print(r"            |                |            |          .' - .. ____ .. - '.     ")
            print(r"___________.' - .. ____ .. - '.           |__________|                  |_____")
            print(r"           |                  |____ .. -- '          |                  |     ")
            print(r"           |                  |                      ' -- .. ____ .. -- '     ")
            print(r"           ' -- .. ____ .. -- '                                               ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                         _. . -- . ._                                         ")
            print(r"                      .'-. .  __  . .-'.                 _. . -- . ._         ")
            print(r"                 _. . :- . .           :              .'-. .  __  . .-'.      ")
            print(r"              .'-. .  __  . .-'.       :              :                :      ")
            print(r"              :                :       |              :                :      ")
            print(r"              :                :       |              |                |      ")
            print(r"              |                |_ .. - '.             |                |      ")
            print(r"              |                |        |            .' - .. ____ .. - '.     ")
            print(r"_____________.' - .. ____ .. - '.       |____________|                  |_____")
            print(r"             |                  | .. -- '            |                  |     ")
            print(r"             |                  |                    ' -- .. ____ .. -- '     ")
            print(r"             ' -- .. ____ .. -- '                                             ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                       _. . -- . ._                                          ")
            print(r"                    .'-. .  __  . .-'.                   _. . -- . ._         ")
            print(r"                   _: . -- . .       :                .'-. .  __  . .-'.      ")
            print(r"                .'-. .  __  . .-'.   :                :                :      ")
            print(r"                :                :   |                :                :      ")
            print(r"                :                :   |                |                |      ")
            print(r"                |                | - '.               |                |      ")
            print(r"                |                |    |              .' - .. ____ .. - '.     ")
            print(r"_______________.' - .. ____ .. - '.   |______________|                  |_____")
            print(r"               |                  |-- '              |                  |     ")
            print(r"               |                  |                  ' -- .. ____ .. -- '     ")
            print(r"               ' -- .. ____ .. -- '                                             ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                     _. . -- . ._                                             ")
            print(r"                  .'-. .  __  . .-'.                     _. . -- . ._         ")
            print(r"                  :  _  . -- . .   :                  .'-. .  __  . .-'.      ")
            print(r"                  .'-. .  __  . .-'.                  :                :      ")
            print(r"                  :                :                  :                :      ")
            print(r"                  :                :                  |                |      ")
            print(r"                 .|                |.                 |                |      ")
            print(r"                 ||                ||                .' - .. ____ .. - '.     ")
            print(r"_________________:' - .. ____ .. - ':________________|                  |_____")
            print(r"                 |                  |                |                  |     ")
            print(r"                 |                  |                ' -- .. ____ .. -- '     ")
            print(r"                 ' -- .. ____ .. -- '                                         ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                   _. . -- . ._                                               ")
            print(r"                .'-. .  __  . .-'.                       _. . -- . ._         ")
            print(r"                :      _. . -- . :_                   .'-. .  __  . .-'.      ")
            print(r"                :   .'-. .  __  . .-'.                :                :      ")
            print(r"                |   :                :                :                :      ")
            print(r"                |   :                :                |                |      ")
            print(r"               .' - |                |                |                |      ")
            print(r"               |    |                |               .' - .. ____ .. - '.     ")
            print(r"_______________|   .' - .. ____ .. - '.______________|                  |_____")
            print(r"               ' --|                  |              |                  |     ")
            print(r"                   |                  |              ' -- .. ____ .. -- '     ")
            print(r"                   ' -- .. ____ .. -- '                                       ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                 _. . -- . ._                                                 ")
            print(r"              .'-. .  __  . .-'.                         _. . -- . ._         ")
            print(r"              :          _. . -- . ._                 .'-. .  __  . .-'.      ")
            print(r"              :       .'-. .  __  . .-'.              :                :      ")
            print(r"              |       :                :              :                :      ")
            print(r"              |       :                :              |                |      ")
            print(r"             .' - .. _|                |              |                |      ")
            print(r"             |        |                |             .' - .. ____ .. - '.     ")
            print(r"_____________|       .' - .. ____ .. - '.____________|                  |_____")
            print(r"             ' -- .. |                  |            |                  |     ")
            print(r"                     |                  |            ' -- .. ____ .. -- '     ")
            print(r"                     ' -- .. ____ .. -- '                                     ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"               _. . -- . ._                                                   ")
            print(r"            .'-. .  __  . .-'.                           _. . -- . ._         ")
            print(r"            :              _.'. -- . ._               .'-. .  __  . .-'.      ")
            print(r"            :           .'-. .  __  . .-'.            :                :      ")
            print(r"            |           :                :            :                :      ")
            print(r"            |           :                :            |                |      ")
            print(r"           .' - .. ____ |                |            |                |      ")
            print(r"           |            |                |           .' - .. ____ .. - '.     ")
            print(r"___________|           .' - .. ____ .. - '.__________|                  |_____")
            print(r"           ' -- .. ____|                  |          |                  |     ")
            print(r"                       |                  |          ' -- .. ____ .. -- '     ")
            print(r"                       ' -- .. ____ .. -- '                                   ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"             _. . -- . ._                                                     ")
            print(r"          .'-. .  __  . .-'.                             _. . -- . ._         ")
            print(r"          :                : _. . -- . ._             .'-. .  __  . .-'.      ")
            print(r"          :               .'-. .  __  . .-'.          :                :      ")
            print(r"          |               :                :          :                :      ")
            print(r"          |               :                :          |                |      ")
            print(r"         .' - .. ____ .. -|                |          |                |      ")
            print(r"         |                |                |         .' - .. ____ .. - '.     ")
            print(r"_________|               .' - .. ____ .. - '.________|                  |_____")
            print(r"         ' -- .. ____ .. |                  |        |                  |     ")
            print(r"                         |                  |        ' -- .. ____ .. -- '     ")
            print(r"                         ' -- .. ____ .. -- '                                 ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"           _. . -- . ._                                                       ")
            print(r"        .'-. .  __  . .-'.                               _. . -- . ._         ")
            print(r"        :                :     _. . -- . ._           .'-. .  __  . .-'.      ")
            print(r"        :                :  .'-. .  __  . .-'.        :                :      ")
            print(r"        |                |  :                :        :                :      ")
            print(r"        |                |  :                :        |                |      ")
            print(r"       .' - .. ____ .. - '. |                |        |                |      ")
            print(r"       |                  | |                |       .' - .. ____ .. - '.     ")
            print(r"_______|                  |.' - .. ____ .. - '.______|                  |_____")
            print(r"       ' -- .. ____ .. -- '|                  |      |                  |     ")
            print(r"                           |                  |      ' -- .. ____ .. -- '     ")
            print(r"                           ' -- .. ____ .. -- '                               ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
            print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
            print(r"      :                :      :                :      :                :      ")
            print(r"      :                :      :                :      :                :      ")
            print(r"      |                |      |                |      |                |      ")
            print(r"      |                |      |                |      |                |      ")
            print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
            print(r"_____|                  |____|                  |____|                  |_____")
            print(r"     |                  |    |                  |    |                  |     ")
            print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
            print(r"                                                                              ")
        if (pierwszy_kubek == 2 and drugi_kubek == 3) or (pierwszy_kubek == 3 and drugi_kubek == 2):
            if pozycja == 2:
                pozycja = 3
            elif pozycja == 3:
                pozycja = 2
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                                        _. . -- . ._          ")
            print(r"         _. . -- . ._                                .'-. .  __  . .-'.       ")
            print(r"      .'-. .  __  . .-'.          _. . -- . ._       :                :       ")
            print(r"      :                :       .'-. .  __  . .-'.    :                :       ")
            print(r"      :                :       :                :    |                |       ")
            print(r"      |                |       :                :    |                |       ")
            print(r"      |                |       |                |   .' - .. ____ .. - '.      ")
            print(r"     .' - .. ____ .. - '.      |                |   |                  |      ")
            print(r"_____|                  |_____.' - .. ____ .. - '.__|                  |______")
            print(r"     |                  |     |                  |  ' -- .. ____ .. -- '      ")
            print(r"     ' -- .. ____ .. -- '     |                  |                            ")
            print(r"                              ' -- .. ____ .. -- '                            ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                                       _. . -- . ._           ")
            print(r"         _. . -- . ._                               .'-. .  __  . .-'.        ")
            print(r"      .'-. .  __  . .-'.           _. . -- . ._     :                :        ")
            print(r"      :                :        .'-. .  __  . .-'.  :                :        ")
            print(r"      :                :        :                :  |                |        ")
            print(r"      |                |        :                :  |                |        ")
            print(r"      |                |        |                | .' - .. ____ .. - '.       ")
            print(r"     .' - .. ____ .. - '.       |                | |                  |       ")
            print(r"_____|                  |______.' - .. ____ .. - '.|                  |_______")
            print(r"     |                  |      |                  |' -- .. ____ .. -- '       ")
            print(r"     ' -- .. ____ .. -- '      |                  |                           ")
            print(r"                               ' -- .. ____ .. -- '                           ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                                     _. . -- . ._             ")
            print(r"         _. . -- . ._                             .'-. .  __  . .-'.          ")
            print(r"      .'-. .  __  . .-'.             _. . -- . ._ :                :          ")
            print(r"      :                :          .'-. .  __  . .-'.               :          ")
            print(r"      :                :          :                :               |          ")
            print(r"      |                |          :                :               |          ")
            print(r"      |                |          |                |- .. ____ .. - '.         ")
            print(r"     .' - .. ____ .. - '.         |                |                |         ")
            print(r"_____|                  |________.' - .. ____ .. - '.               |_________")
            print(r"     |                  |        |                  | .. ____ .. -- '         ")
            print(r"     ' -- .. ____ .. -- '        |                  |                         ")
            print(r"                                 ' -- .. ____ .. -- '                         ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                                   _. . -- . ._               ")
            print(r"         _. . -- . ._                           .'-. .  __  . .-'.            ")
            print(r"      .'-. .  __  . .-'.               _. . -- .'._              :            ")
            print(r"      :                :            .'-. .  __  . .-'.           :            ")
            print(r"      :                :            :                :           |            ")
            print(r"      |                |            :                :           |            ")
            print(r"      |                |            |                | ____ .. - '.           ")
            print(r"     .' - .. ____ .. - '.           |                |            |           ")
            print(r"_____|                  |__________.' - .. ____ .. - '.           |___________")
            print(r"     |                  |          |                  |____ .. -- '           ")
            print(r"     ' -- .. ____ .. -- '          |                  |                       ")
            print(r"                                   ' -- .. ____ .. -- '                       ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                                  _. . -- . ._                ")
            print(r"         _. . -- . ._                          .'-. .  __  . .-'.             ")
            print(r"      .'-. .  __  . .-'.                  _. . '- . ._          :             ")
            print(r"      :                :               .'-. .  __  . .-'.       :             ")
            print(r"      :                :               :                :       |             ")
            print(r"      |                |               :                :       |             ")
            print(r"      |                |               |                |_ .. - '.            ")
            print(r"     .' - .. ____ .. - '.              |                |        |            ")
            print(r"_____|                  |_____________.' - .. ____ .. - '.       |____________")
            print(r"     |                  |             |                  | .. -- '            ")
            print(r"     ' -- .. ____ .. -- '             |                  |                    ")
            print(r"                                      ' -- .. ____ .. -- '                    ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                                _. . -- . ._                  ")
            print(r"         _. . -- . ._                        .'-. .  __  . .-'.               ")
            print(r"      .'-. .  __  . .-'.                    _: . -- . . _     :               ")
            print(r"      :                :                 .'-. .  __  . .-'.   :               ")
            print(r"      :                :                 :                :   |               ")
            print(r"      |                |                 :                :   |               ")
            print(r"      |                |                 |                | - '.              ")
            print(r"     .' - .. ____ .. - '.                |                |    |              ")
            print(r"_____|                  |_______________.' - .. ____ .. - '.   |______________")
            print(r"     |                  |               |                  |-- '              ")
            print(r"     ' -- .. ____ .. -- '               |                  |                  ")
            print(r"                                        ' -- .. ____ .. -- '                  ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                              _. . -- . ._                    ")
            print(r"         _. . -- . ._                      .'-. .  __  . .-'.                 ")
            print(r"      .'-. .  __  . .-'.                   :  _  . -- . .   :                 ")
            print(r"      :                :                   .'-. .  __  . .-'.                 ")
            print(r"      :                :                   :                :                 ")
            print(r"      |                |                   :                :                 ")
            print(r"      |                |                  .|                |.                ")
            print(r"     .' - .. ____ .. - '.                 ||                ||                ")
            print(r"_____|                  |_________________:' - .. ____ .. - ':________________")
            print(r"     |                  |                 |                  |                ")
            print(r"     ' -- .. ____ .. -- '                 |                  |                ")
            print(r"                                          ' -- .. ____ .. -- '                ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                            _. . -- . ._                     ")
            print(r"         _. . -- . ._                    .'-. .  __  . .-'.                   ")
            print(r"      .'-. .  __  . .-'.                 :      _. . -- . :_                  ")
            print(r"      :                :                 :   .'-. .  __  . .-'.               ")
            print(r"      :                :                 |   :                :               ")
            print(r"      |                |                 |   :                :               ")
            print(r"      |                |                .' - |                |               ")
            print(r"     .' - .. ____ .. - '.               |    |                |               ")
            print(r"_____|                  |_______________|   .' - .. ____ .. - '.______________")
            print(r"     |                  |               ' --|                  |              ")
            print(r"     ' -- .. ____ .. -- '                   |                  |              ")
            print(r"                                            ' -- .. ____ .. -- '              ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                          _. . -- . ._                        ")
            print(r"         _. . -- . ._                  .'-. .  __  . .-'.                     ")
            print(r"      .'-. .  __  . .-'.               :          _. . -' . ._                ")
            print(r"      :                :               :       .'-. .  __  . .-'.             ")
            print(r"      :                :               |       :                :             ")
            print(r"      |                |               |       :                :             ")
            print(r"      |                |              .' - .. _|                |             ")
            print(r"     .' - .. ____ .. - '.             |        |                |             ")
            print(r"_____|                  |_____________|       .' - .. ____ .. - '.____________")
            print(r"     |                  |             ' -- .. |                  |            ")
            print(r"     ' -- .. ____ .. -- '                     |                  |            ")
            print(r"                                              ' -- .. ____ .. -- '            ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                        _. . -- . ._                          ")
            print(r"         _. . -- . ._                .'-. .  __  . .-'.                       ")
            print(r"      .'-. .  __  . .-'.             :              _.'. -- . ._              ")
            print(r"      :                :             :           .'-. .  __  . .-'.           ")
            print(r"      :                :             |           :                :           ")
            print(r"      |                |             |           :                :           ")
            print(r"      |                |            .' - .. ____ |                |           ")
            print(r"     .' - .. ____ .. - '.           |            |                |           ")
            print(r"_____|                  |___________|           .' - .. ____ .. - '.__________")
            print(r"     |                  |           ' -- .. ____|                  |          ")
            print(r"     ' -- .. ____ .. -- '                       |                  |          ")
            print(r"                                                ' -- .. ____ .. -- '          ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                      _. . -- . ._                            ")
            print(r"         _. . -- . ._              .'-. .  __  . .-'.                         ")
            print(r"      .'-. .  __  . .-'.           :                : _. . -- . ._            ")
            print(r"      :                :           :               .'-. .  __  . .-'.         ")
            print(r"      :                :           |               :                :         ")
            print(r"      |                |           |               :                :         ")
            print(r"      |                |          .' - .. ____ .. -|                |         ")
            print(r"     .' - .. ____ .. - '.         |                |                |         ")
            print(r"_____|                  |_________|               .' - .. ____ .. - '.________")
            print(r"     |                  |         ' -- .. ____ .. |                  |        ")
            print(r"     ' -- .. ____ .. -- '                         |                  |        ")
            print(r"                                                  ' -- .. ____ .. -- '        ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                    _. . -- . ._                              ")
            print(r"         _. . -- . ._            .'-. .  __  . .-'.                           ")
            print(r"      .'-. .  __  . .-'.         :                :     _. . -- . ._          ")
            print(r"      :                :         :                :  .'-. .  __  . .-'.       ")
            print(r"      :                :         |                |  :                :       ")
            print(r"      |                |         |                |  :                :       ")
            print(r"      |                |        .' - .. ____ .. - '. |                |       ")
            print(r"     .' - .. ____ .. - '.       |                  | |                |       ")
            print(r"_____|                  |_______|                  |.' - .. ____ .. - '.______")
            print(r"     |                  |       ' -- .. ____ .. -- '|                  |      ")
            print(r"     ' -- .. ____ .. -- '                           |                  |      ")
            print(r"                                                    ' -- .. ____ .. -- '      ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
            print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
            print(r"      :                :      :                :      :                :      ")
            print(r"      :                :      :                :      :                :      ")
            print(r"      |                |      |                |      |                |      ")
            print(r"      |                |      |                |      |                |      ")
            print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
            print(r"_____|                  |____|                  |____|                  |_____")
            print(r"     |                  |    |                  |    |                  |     ")
            print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
            print(r"                                                                              ")
        if (pierwszy_kubek == 1 and drugi_kubek == 3) or (pierwszy_kubek == 3 and drugi_kubek == 1):
            if pozycja == 1:
                pozycja = 3
            elif pozycja == 3:
                pozycja = 1
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                                        _. . -- . ._          ")
            print(r"                                 _. . -- . ._        .'-. .  __  . .-'.       ")
            print(r"          _. . -- . ._        .'-. .  __  . .-'.     :                :       ")
            print(r"       .'-. .  __  . .-'.     :                :     :                :       ")
            print(r"       :                :     :                :     |                |       ")
            print(r"       :                :     |                |     |                |       ")
            print(r"       |                |     |                |    .' - .. ____ .. - '.      ")
            print(r"       |                |    .' - .. ____ .. - '.   |                  |      ")
            print(r"______.' - .. ____ .. - '.___|                  |___|                  |______")
            print(r"      |                  |   |                  |   ' -- .. ____ .. -- '      ")
            print(r"      |                  |   ' -- .. ____ .. -- '                             ")
            print(r"      ' -- .. ____ .. -- '                                                    ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                                     _. . -- . ._             ")
            print(r"                                 _. . -- . ._     .'-. .  __  . .-'.          ")
            print(r"             _. . -- . ._     .'-. .  __  . .-'.  :                :          ")
            print(r"          .'-. .  __  . .-'.  :                :  :                :          ")
            print(r"          :                :  :                :  |                |          ")
            print(r"          :                :  |                |  |                |          ")
            print(r"          |                |  |                | .' - .. ____ .. - '.         ")
            print(r"          |                | .' - .. ____ .. - '.|                  |         ")
            print(r"_________.' - .. ____ .. - '.|                  ||                  |_________")
            print(r"         |                  ||                  |' -- .. ____ .. -- '         ")
            print(r"         |                  |' -- .. ____ .. -- '                             ")
            print(r"         ' -- .. ____ .. -- '                                                 ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                                  _. . -- . ._                ")
            print(r"                                 _. . -- . ._  .'-. .  __  . .-'.             ")
            print(r"                _. . -- . ._  .'-. .  __  . .-'.                :             ")
            print(r"             .'-. .  __  . .-':                :                :             ")
            print(r"             :                :                :                |             ")
            print(r"             :                :                |                |             ")
            print(r"             |                |                | - .. ____ .. - '.            ")
            print(r"             |                | - .. ____ .. - '.                |            ")
            print(r"____________.' - .. ____ .. - '.                |                |____________")
            print(r"            |                  |                |- .. ____ .. -- '            ")
            print(r"            |                  |- .. ____ .. -- '                             ")
            print(r"            ' -- .. ____ .. -- '                                              ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                               _. . -- . ._                   ")
            print(r"                                 _. . -- . ._'-. .  __  . .-'.                ")
            print(r"                   _. . -- . ._'-. .  __  . .-'.             :                ")
            print(r"                .'-. .  __  . .-':             :             :                ")
            print(r"                :                :             :             |                ")
            print(r"                :                :             |             |                ")
            print(r"                |                |             |.. ____ .. - '.               ")
            print(r"                |                |.. ____ .. - '.             |               ")
            print(r"_______________.' - .. ____ .. - '.             |             |_______________")
            print(r"               |                  |             |. ____ .. -- '               ")
            print(r"               |                  |. ____ .. -- '                             ")
            print(r"               ' -- .. ____ .. -- '                                           ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                            _. . -- . ._                      ")
            print(r"                                 _. . -- .'._ .  __  . .-'.                   ")
            print(r"                      _. . -- .'._ .  __  . .-'.          :                   ")
            print(r"                   .'-. .  __  . .-':          :          :                   ")
            print(r"                   :                :          :          |                   ")
            print(r"                   :                :          |          |                   ")
            print(r"                   |                |          |____ .. - '.                  ")
            print(r"                   |                |____ .. - '.          |                  ")
            print(r"__________________.' - .. ____ .. - '.          |          |__________________")
            print(r"                  |                  |          |___ .. -- '                  ")
            print(r"                  |                  |___ .. -- '                             ")
            print(r"                  ' -- .. ____ .. -- '                                        ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                         _. . -- . ._                         ")
            print(r"                                 _. . --'. ._ __  . .-'.                      ")
            print(r"                         _. . --'. ._ __  . .-'.       :                      ")
            print(r"                      .'-. .  __  . .-':       :       :                      ")
            print(r"                      :                :       :       |                      ")
            print(r"                      :                :       |       |                      ")
            print(r"                      |                |       |_ .. - '.                     ")
            print(r"                      |                |_ .. - '.       |                     ")
            print(r"_____________________.' - .. ____ .. - '.       |       |_____________________")
            print(r"                     |                  |       | .. -- '                     ")
            print(r"                     |                  | .. -- '                             ")
            print(r"                     ' -- .. ____ .. -- '                                     ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                      _. . -- . ._                            ")
            print(r"                                 _. .'-- . ._  . .-'.                         ")
            print(r"                            _. .'-- . ._  . .-'.    :                         ")
            print(r"                         .'-. .  __  . .-':    :    :                         ")
            print(r"                         :                :    :    |                         ")
            print(r"                         :                :    |    |                         ")
            print(r"                         |                |    |. - '.                        ")
            print(r"                         |                |. - '.    |                        ")
            print(r"________________________.' - .. ____ .. - '.    |    |________________________")
            print(r"                        |                  |    | -- '                        ")
            print(r"                        |                  | -- '                             ")
            print(r"                        ' -- .. ____ .. -- '                                  ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                   _. . -- . ._                               ")
            print(r"                                 _' . -- . ._ .-'.                            ")
            print(r"                               _' . -- . ._ .-'. :                            ")
            print(r"                            .'-. .  __  . .-': : :                            ")
            print(r"                            :                : : |                            ")
            print(r"                            :                : | |                            ")
            print(r"                            |                | | '.                           ")
            print(r"                            |                | '. |                           ")
            print(r"___________________________.' - .. ____ .. - '. | |___________________________")
            print(r"                           |                  | | '                           ")
            print(r"                           |                  | '                             ")
            print(r"                           ' -- .. ____ .. -- '                               ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                                _. . -- . ._                                  ")
            print(r"                             .'-._. . -- . ._'.                               ")
            print(r"                             :.'-._. . -- . ._'.                              ")
            print(r"                             ::.'-. .  __  . .-':                             ")
            print(r"                             |::                :                             ")
            print(r"                             ||:                :                             ")
            print(r"                            .'||                |                             ")
            print(r"                            |.'|                |                             ")
            print(r"____________________________||.' - .. ____ .. - '.____________________________")
            print(r"                            '||                  |                            ")
            print(r"                             '|                  |                            ")
            print(r"                              ' -- .. ____ .. -- '                            ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                            _. . -- . ._                                      ")
            print(r"                         .'-. .  _. . --'. ._                                 ")
            print(r"                         :    .'-. .  _. . --'. ._                            ")
            print(r"                         :    :    .'-. .  __  . .-':                         ")
            print(r"                         |    :    :                :                         ")
            print(r"                         |    |    :                :                         ")
            print(r"                        .' - .|    |                |                         ")
            print(r"                        |    .' - .|                |                         ")
            print(r"________________________|    |    .' - .. ____ .. - '.________________________")
            print(r"                        ' -- |    |                  |                        ")
            print(r"                             ' -- |                  |                        ")
            print(r"                                  ' -- .. ____ .. -- '                        ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                         _. . -- . ._                                         ")
            print(r"                      .'-. .  __ _. .'-- . ._                                 ")
            print(r"                      :       .'-. .  __ _. .'-- . ._                         ")
            print(r"                      :       :       .'-. .  __  . .-':                      ")
            print(r"                      |       :       :                :                      ")
            print(r"                      |       |       :                :                      ")
            print(r"                     .' - .. _|       |                |                      ")
            print(r"                     |       .' - .. _|                |                      ")
            print(r"_____________________|       |       .' - .. ____ .. - '._____________________")
            print(r"                     ' -- .. |       |                  |                     ")
            print(r"                             ' -- .. |                  |                     ")
            print(r"                                     ' -- .. ____ .. -- '                     ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                      _. . -- . ._                                            ")
            print(r"                   .'-. .  __  . _' . -- . ._                                 ")
            print(r"                   :          .'-. .  __  . _' . -- . ._                      ")
            print(r"                   :          :          .'-. .  __  . .-':                   ")
            print(r"                   |          :          :                :                   ")
            print(r"                   |          |          :                :                   ")
            print(r"                  .' - .. ____|          |                |                   ")
            print(r"                  |          .' - .. ____|                |                   ")
            print(r"__________________|          |          .' - .. ____ .. - '.__________________")
            print(r"                  ' -- .. ___|          |                  |                  ")
            print(r"                             ' -- .. ___|                  |                  ")
            print(r"                                        ' -- .. ____ .. -- '                  ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                   _. . -- . ._                                               ")
            print(r"                .'-. .  __  . .-'_. . -- . ._                                 ")
            print(r"                :             .'-. .  __  . .-'_. . -- . ._                   ")
            print(r"                :             :             .'-. .  __  . .-':                ")
            print(r"                |             :             :                :                ")
            print(r"                |             |             :                :                ")
            print(r"               .' - .. ____ ..|             |                |                ")
            print(r"               |             .' - .. ____ ..|                |                ")
            print(r"_______________|             |             .' - .. ____ .. - '._______________")
            print(r"               ' -- .. ____ .|             |                  |               ")
            print(r"                             ' -- .. ____ .|                  |               ")
            print(r"                                           ' -- .. ____ .. -- '               ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"                _. . -- . ._                                                  ")
            print(r"             .'-. .  __  . .-'.  _. . -- . ._                                 ")
            print(r"             :                .'-. .  __  . .-'.  _. . -- . ._                ")
            print(r"             :                :                .'-. .  __  . .-':             ")
            print(r"             |                :                :                :             ")
            print(r"             |                |                :                :             ")
            print(r"            .' - .. ____ .. - |                |                |             ")
            print(r"            |                .' - .. ____ .. - |                |             ")
            print(r"____________|                |                .' - .. ____ .. - '.____________")
            print(r"            ' -- .. ____ .. -|                |                  |            ")
            print(r"                             ' -- .. ____ .. -|                  |            ")
            print(r"                                              ' -- .. ____ .. -- '            ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"             _. . -- . ._                                                     ")
            print(r"          .'-. .  __  . .-'.     _. . -- . ._                                 ")
            print(r"          :                :  .'-. .  __  . .-'.     _. . -- . ._             ")
            print(r"          :                :  :                :  .'-. .  __  . .-':          ")
            print(r"          |                |  :                :  :                :          ")
            print(r"          |                |  |                |  :                :          ")
            print(r"         .' - .. ____ .. - '. |                |  |                |          ")
            print(r"         |                  |.' - .. ____ .. - '. |                |          ")
            print(r"_________|                  ||                  |.' - .. ____ .. - '._________")
            print(r"         ' -- .. ____ .. -- '|                  ||                  |         ")
            print(r"                             ' -- .. ____ .. -- '|                  |         ")
            print(r"                                                 ' -- .. ____ .. -- '         ")
            time.sleep(czasruchu)
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
            print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
            print(r"      :                :      :                :      :                :      ")
            print(r"      :                :      :                :      :                :      ")
            print(r"      |                |      |                |      |                |      ")
            print(r"      |                |      |                |      |                |      ")
            print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
            print(r"_____|                  |____|                  |____|                  |_____")
            print(r"     |                  |    |                  |    |                  |     ")
            print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
            print(r"                                                                              ")
    gdzie = int(input("W którym kubku jest kulka(1-3): "))
    while gdzie < 1 or gdzie > 3:
        print("Musisz wybrać liczbę pomiędzy 1-3")
        gdzie = int(input("W którym kubku jest kulka(1-3): "))
    time.sleep(delay)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
    print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      :                :      :                :      :                :      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"      |                |      |                |      |                |      ")
    print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
    print(r"_____|                  |____|                  |____|                  |_____")
    print(r"     |                  |    |                  |    |                  |     ")
    print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
    print(r"                                                                              ")
    if pozycja == 2:
        time.sleep(delay)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
        print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"_____|                  |____|                  |____|                  |_____")
        print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
        print(r"                                      ''                                      ")
        print(r"                                                                              ")

        time.sleep(delay)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
        print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"_____'_-- .. ____ .. --_'____'_-- .. ____ .. --_'____'_-- .. ____ .. --_'_____")
        print(r"                                     '--'                                     ")
        print(r"                                                                              ")
        print(r"                                                                              ")
        time.sleep(delay)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
        print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
        print(r"____________________________________(    )____________________________________")
        print(r"                                     '--'                                     ")
        print(r"                                                                              ")
        print(r"                                                                              ")
        time.sleep(delay)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
        print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
        print(r"                                     .--.                                     ")
        print(r"____________________________________(    )____________________________________")
        print(r"                                     '--'                                     ")
        print(r"                                                                              ")
        print(r"                                                                              ")
        time.sleep(delay*4)
    if pozycja == 1:
        time.sleep(delay)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
        print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"_____|                  |____|                  |____|                  |_____")
        print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
        print(r"              ''                                                            ")
        print(r"                                                                              ")

        time.sleep(delay)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
        print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"_____'_-- .. ____ .. --_'____'_-- .. ____ .. --_'____'_-- .. ____ .. --_'_____")
        print(r"             '--'                                                             ")
        print(r"                                                                              ")
        print(r"                                                                              ")
        time.sleep(delay)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
        print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
        print(r"____________(    )____________________________________________________________")
        print(r"             '--'                                                             ")
        print(r"                                                                              ")
        print(r"                                                                              ")
        time.sleep(delay)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
        print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
        print(r"             .--.                                                             ")
        print(r"____________(    )____________________________________________________________")
        print(r"             '--'                                                             ")
        print(r"                                                                              ")
        print(r"                                                                              ")
        time.sleep(delay*4)
    if pozycja == 3:
        time.sleep(delay)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
        print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"_____|                  |____|                  |____|                  |_____")
        print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
        print(r"              ''                                                              ")
        print(r"                                                                              ")

        time.sleep(delay)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
        print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"_____'_-- .. ____ .. --_'____'_-- .. ____ .. --_'____'_-- .. ____ .. --_'_____")
        print(r"                                                             '--'             ")
        print(r"                                                                              ")
        print(r"                                                                              ")
        time.sleep(delay)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
        print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
        print(r"____________________________________________________________(    )____________")
        print(r"                                                             '--'             ")
        print(r"                                                                              ")
        print(r"                                                                              ")
        time.sleep(delay)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(r"         _. . -- . ._            _. . -- . ._            _. . -- . ._         ")
        print(r"      .'-. .  __  . .-'.      .'-. .  __  . .-'.      .'-. .  __  . .-'.      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      :                :      :                :      :                :      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"      |                |      |                |      |                |      ")
        print(r"     .' - .. ____ .. - '.    .' - .. ____ .. - '.    .' - .. ____ .. - '.     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"     |                  |    |                  |    |                  |     ")
        print(r"     ' -- .. ____ .. -- '    ' -- .. ____ .. -- '    ' -- .. ____ .. -- '     ")
        print(r"                                                             .--.             ")
        print(r"____________________________________________________________(    )____________")
        print(r"                                                             '--'             ")
        print(r"                                                                              ")
        print(r"                                                                              ")
        time.sleep(delay*4)
    if gdzie == pozycja:
        print("BRAWO! Znalazłeś kulkę")
        print("Zyskujesz 10 monet")
        time.sleep(0.8)
        gold += 10
    else:
        print("Niestety nie udało ci się znaleźć kulki")
        print("Tracisz 10 monet")
        time.sleep(0.8)
        gold -= 10
    karczma()
sklep_i_arena()
