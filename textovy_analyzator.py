'''
projekt_1.py = první projekt do Engeto Online Python Akademie
author = Martin Hába
e-mail = mhaba@seznam.cz
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
indexy_textu = [index + 1 for index, hodnota in enumerate(TEXTS)]
pocet_textu = indexy_textu[-1]

INTERPUNKCE = ".,!?;:“”'\""

pocet_slov = 0
pocet_slov_zacinajici_velkym = 0
pocet_slov_pouze_velkymi = 0
pocet_slov_pouze_malymi = 0
pocet_cisel = 0
suma_cisel = 0
delky_slov = {}

#přihlášení se do aplikace
prihlasovaci_udaje = {"bob": "123",
                      "ann": "pass123",
                      "mike":"password123",
                      "liz": "pass123"}

jmeno = input("username:")
heslo = input("password:")

if prihlasovaci_udaje.get(jmeno) == heslo:
    print("-"*40,
          f"Welcome to the app, {jmeno} ", 
          f"We have {pocet_textu} texts to be analyzed", 
          "-"*40,
          sep = "\n")
else: 
    print("unregistered user, terminating the program..")
    exit()

#výběr textu k analýze a jeho případná příprava
vyber_textu = input(f"Enter a number btw. 1 and {pocet_textu} to select:")

if vyber_textu.isnumeric():
    if int(vyber_textu) in indexy_textu:
        vybrany_text = TEXTS[int(vyber_textu)-1].split()
        #slova_textu = {klic:0 for klic in vybrany_text}     
    else:
        print(f"text with number {vyber_textu} does not exist, terminatin the program..")
        exit()
else:
    print("please select only numbers, terminating program..")
    exit()

#vlastní analýza počtu slov
for slovo in vybrany_text:   
    pocet_slov +=1
    delka_slova = len(slovo)  
    # Začínajících velkými písmeny
    if slovo.istitle():
        pocet_slov_zacinajici_velkym +=1            
    # Obsahuje pouze velká písmena (a žádné číslice)
    if slovo.isupper():
        if not any(pismeno.isdigit() for pismeno in slovo):
            pocet_slov_pouze_velkymi +=1
    # Obsahuje pouze malá písmena (a žádné číslice)      
    if slovo.islower():
        if not any(pismeno.isdigit() for pismeno in slovo):
            pocet_slov_pouze_malymi +=1
    # Je číslo a výpočet sumy všech čísel
    if slovo.isnumeric():
        pocet_cisel +=1
        suma_cisel +=int(slovo)
    
    # Očištění délky slov o interpunkční znaménko za slovem
    # nebere v úvahu možnost interpunkce na začátku nebo více znamének
    if not slovo[-1] in INTERPUNKCE:
        delka_slova = len(slovo)
    else:
        delka_slova = len(slovo)-1
    #Četnost délky slov
    if delka_slova in delky_slov:
        delky_slov[delka_slova] +=1 
    else: 
        delky_slov[delka_slova] = 1
               
#tisk výstupu počtů jednotlivých druhů slov
print("-"*40,
      f"There are {pocet_slov} words in the selected text.",
      f"There are {pocet_slov_zacinajici_velkym} titlecase words.", 
      f"There are {pocet_slov_pouze_velkymi} uppercase words.", 
      f"There are {pocet_slov_pouze_malymi} lowercase words.", 
      f"There are {pocet_cisel} numeric strings.", 
      f"The sum of all the numbers {suma_cisel}",
      "-"*40,
      sep = "\n")

#příprava a tisk výstupu četností slov dle délky slov 
#max se bude zobrazovat 30 hvězdiček jako graf, číslo 
pracovni_max = max(delky_slov.values())
if pracovni_max <=30:
    max_cetnost = pracovni_max
else:
    max_cetnost = 30

print("LEN|" + "OCCURENCES".center(max_cetnost + 2) + "|NR.", "-"*40, sep = "\n")

for delka in sorted(delky_slov.keys()):
    # zobrazovat se bude max 30 hvědiček, číslo bude vždy přesné...
    cetnost_slova = delky_slov[delka]
    if cetnost_slova <=30:
        delka_cetnost = cetnost_slova
    else:
        delka_cetnost = 30
    # bude vytvářet zarovnané formátování pokud nebude žádné slovo delší než 99 znaků.
    if delka < 10:
        delka_pro_tisk = f"  {delka}" 
    else:
        delka_pro_tisk = f" {delka}"
    
    print(str(delka_pro_tisk) 
          + "|"
          + "*"*int(delka_cetnost) 
          + " "*(max_cetnost +2 -int(delka_cetnost)) 
          + "|"+ str(cetnost_slova), 
          sep="\n")

