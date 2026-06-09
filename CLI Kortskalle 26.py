from random import randint
import os
import time

def skrivTekst(tekst, delay=0.03):
    for bokstav in tekst:
        print(bokstav, end="", flush=True)
        time.sleep(delay)
    print()

def skrivInput(tekst, delay=0.03):
    for bokstav in tekst:
        print(bokstav, end="", flush=True)
        time.sleep(delay)

    return input()

#-----------------------------------------------------------TITTEL
print(
    "-------------------------------\n"
    "       * KORTSKALLE *\n"
    "-------------------------------\n"
)

#-----------------------------------------------------------SPILLEREGLER
def spilleregler():
    regler = skrivInput(
        "Ønsker du å lese spillereglene?\n"
        " - "
    ).lower()
    time.sleep(0.5)
    print()
    while regler != "nei":
        if regler == "ja":
            skrivTekst(
                "Ok! Her er reglene:\n"
            )
            print(
                "-------------------------------"
            )
            skrivTekst(
                "MÅLSETNING:\n"
                "Gjett både din egen karakter OG ditt eget sted før andre gjør det samme.\n"
                "\n"
                "OPPSETT:\n"
                "• Hver spiller tildeles en karakter og et sted\n"
                "• Kun de ANDRE spillerne får vite hva du fikk\n"
                "• Du kjenner ikke din egen karakter eller ditt eget sted\n"
                "\n"
                "SPILLGANG:\n"
                "Spillerne går på tur en om gangen. Hver tur får du:\n"
                "  1. Et tilfeldig hint-format (mer info kommer)\n"
                "  2. Valget om du vil gjette eller gå videre\n"
                "\n"
                "DE 4 HINT-FORMATENE:\n"
                "\n"
                "① ALLE GIR HINT\n"
                "   Alle dine medspillere gir ETT hint hver. Du velger selv\n"
                "   om hintene skal handle om din KARAKTER eller ditt STED.\n"
                "\n"
                "② RAPID FIRE (30 sekunder)\n"
                "   Du stiller så mange JA/NEI-spørsmål som mulig på 30 sekunder.\n"
                "   Du må si på forhånd om det skal handle om din KARAKTER eller ditt STED.\n"
                "   Eksempler: 'Er jeg en politiker?', 'Er jeg i Europa?'\n"
                "\n"
                "③ NYHETSOVERSKRIFT\n"
                "   Dine medspillere lager hver sin setning som kunne vært en\n"
                "   nyhetsoverskrift om din KARAKTER eller om ditt STED.\n"
                "   Du velger selv hvilken av dem det skal handle om.\n"
                "\n"
                "④ BOKSTAVHINT\n"
                "   Dine medspillere oppgir en bokstav du selv velger.\n"
                "   Du kan be om hvilken som helst bokstav, for eksempel første eller siste bokstav.\n"
                "   Du bestemmer om det skal være fra KARAKTER eller STED.\n"
                "\n"
                "Medspillerne har lov til å bruke internet for å svare på oppgavene."
                "\n"
                "GJETTING:\n"
                "På slutten av din tur kan du si 'svar' for å gjette.\n"
                "Du må gjette BÅDE karakteren din OG stedet ditt riktig.\n"
                "Hvis du gjetter feil, kan du allikevel fortsette å spille.\n"
                "\n"
                "VINNERE:\n"
                "Når en spiller har gjettet riktig, spilles resten av runden så alle spillerne får sin tur.\n"
                "På denne siste turen, får man valget mellom å gjette eller gi turen videre.\n"
                "Når runden er ferdig, har alle som gjettet riktig vunnet spillet!"
            )
            break
        regler = skrivInput(
            "Ugyldig svar. Skriv 'ja' eller 'nei'.\n"
            "Ønsker du å lese spillereglene?\n"
            " - "
        ).lower()
        time.sleep(0.5)
    print()
spilleregler()
skrivTekst("Du/dere vil også få muligheten til å lese reglene før spillet starter.")
print("-------------------------------")
time.sleep(1)
print()

#-----------------------------------------------------------SPILLERE
skrivTekst("Velg antall spillere: (Anbefalt: ~3-7)")
while True:
    try:
        antallSpillere = int(skrivInput(" - "))
        if antallSpillere > 1 and antallSpillere <= 30:
            break
        print()
        if antallSpillere < 2:
            skrivTekst("Man kan ikke spille med mindre enn 2 spillere.")
        elif antallSpillere > 50:
            skrivTekst(f"Det blir litt vel mye med {antallSpillere} spillere, kanskje?")
    except ValueError:
        skrivTekst(
            "\n"
            "Du må skrive inn et tall."
        )
    skrivTekst("Vennligst velg på nytt:")
print()
time.sleep(0.5)

spillere = {}

for i in range(antallSpillere):
    navn = skrivInput(f"Spiller {i+1}'s navn: ")
    spillere[navn] = {
        "karakter": None,
        "sted": None
    }
time.sleep(1)

print("\n-------------------------------\n")

#-----------------------------------------------------------KARAKTER- OG STED-VALG
autoKarakterer = [
    # --- POLITIKERE (25 stk) ---
    "Jens Stoltenberg", "Erna Solberg", "Gro Harlem Brundtland", "Donald Trump", "Barack Obama", 
    "Joe Biden", "Winston Churchill", "Nelson Mandela", "Angela Merkel", "Vladimir Putin", 
    "Einar Gerhardsen", "Kåre Willoch", "Margaret Thatcher", "John F. Kennedy", "Abraham Lincoln", 
    "George Washington", "Emmanuel Macron", "Justin Trudeau", "Kim Jong-un", "Bill Clinton", 
    "Ronald Reagan", "Jonas Gahr Støre", "Trygve Slagsvold Vedum", "Sylvi Listhaug", "Adolf Hitler",


    # --- HISTORISKE PERSONER (25 stk) ---
    "Albert Einstein", "Leonardo da Vinci", "Fridtjof Nansen", "Roald Amundsen", "Cleopatra", 
    "Julius Cæsar", "William Shakespeare", "Mozart", "Beethoven", "Napoleon", 
    "Jeanne d'Arc", "Marie Curie", "Isaac Newton", "Christopher Columbus", "Charles Darwin", 
    "Alexander den store", "Mahatma Gandhi", "Martin Luther King Jr.", "Henrik Ibsen", "Edvard Munch", 
    "Anne Frank", "Marco Polo", "Harald Hårfagre", "Olav den hellige", "Dronning Victoria",

    # --- TEGNESERIE-KARAKTERER (25 stk) ---
    "Donald Duck", "Mikke Mus", "Pappa Smurf", "Skrue McDuck", "Langbein", 
    "Homer Simpson", "Bart Simpson", "Svampebob Firkant", "Pondus", "Asterix", 
    "Obelix", "Tintin", "Lucky Luke", "Fantomet", "Batman", 
    "Superman", "Spiderman", "Super Mario", "Pikachu", "Nemi", 
    "Tommy og Tigern", "Snoopy", "Pusur", "Skipper'n", "Ole Brumm",

    # --- ANDRE UTVALGTE PERSONER/FIGURER (25 stk) ---
    "Jesus", "Julenissen", "Pippi Langstrømpe", "Harry Potter", "Sherlock Holmes", 
    "James Bond", "Michael Jackson", "Elvis Presley", "Askeladden", "Bukkene Bruse", 
    "Rødhette", "Askepott", "Shrek", "Tarzan", "Robin Hood", 
    "Grev Dracula", "Frankenstein", "Luke Skywalker", "Darth Vader", "Kaptein Sabeltann", 
    "Marilyn Monroe", "Beyoncé", "Taylor Swift", "Alan Walker", "Kygo"
]

autoSteder = [
    # 15 velkjente land
    "Norge", "Sverige", "Danmark", "Finland", "USA", 
    "Frankrike", "Spania", "Italia", "Tyskland", "Hellas", 
    "Japan", "Kina", "Australia", "Brasil", "Egypt",

    # 15 velkjente byer
    "London", "Paris", "New York", "Tokyo", "Roma", 
    "Sydney", "Kairo", "Rio de Janeiro", "Barcelona", "Berlin", 
    "København", "Stockholm", "Los Angeles", "Bangkok", "Amsterdam",

    # 5 store byer i Norge
    "Oslo", "Bergen", "Trondheim", "Stavanger", "Kristiansand",

    # 15 velkjente fiktive steder
    "Hogwarts", "Narnia", "Andeby", "Bikinibunnen", 
    "Atlantis", "Mummidalen", "Zootropolis", "Kardemommeby",
    "Hundremeterskogen", "Drømmeland", "Gotham City", "Krypton",
    "Wakanda", "Blåfjell", "Flåklypa",

    # 10 typer offentlige bygg
    "Sykehuset", "Skolen", "Biblioteket", "Rådhuset", "Politistasjonen", 
    "Brannstasjonen", "Museet", "Kinoen", "Teateret", "Kirken",

    # 10 romtyper (steder i huset)
    "Kjøkkenet", "Stuen", "Baderommet", "Soverommet", "Gangen", 
    "Kjelleren", "Loftet", "Garasjen", "Kontoret", "Vaskerommet",

    # 15 velkjente geografiske områder/severdigheter
    "Eiffeltårnet", "Frihetsgudinnen", "Den kinesiske mur", "Pyramidene", "Grand Canyon", 
    "Niagara", "Nordpolen", "Antarktis", "Sahara", "Hawaii", 
    "Atlanterhavet", "Stillehavet", "Middelhavet", "Mount Everest", "Amazonas",

    # 10 planeter og objekter i solsystemet
    "Merkur", "Venus", "Jorden", "Mars", "Jupiter", 
    "Saturn", "Uranus", "Neptun", "Månen", "Sola"

    # 5 lokasjoner/regioner/severdigheter til slutt (generelle/kjente som passer spillet)
    "Himmelen", "Tangen", "Flekkerøy", "Colorline", "Bali"
]

karakterOgStedvalg = skrivInput(
    "Hvordan vil dere velge karakterer og steder? (Skriv tall):\n"
    "\n"
    "1. Egendefinert (Dere har full kontroll, f.eks muntlig eller skriftlig bestemmelse)\n"
    "2. Tilfeldig egendefinert (Dere lager lister selv, og programmet velger tilfeldig fra disse)\n"
    "3. Tilfeldig forhåndsdefinert (Programmet har ferdige lister, og velger tilfeldig fra disse)\n"
    " - "
).lower()
time.sleep(0.5)

while karakterOgStedvalg != "1" and karakterOgStedvalg != "2" and karakterOgStedvalg != "3":
    karakterOgStedvalg = skrivInput(
        "Beklager, svaret er ugyldig. Husk å skrive et tall fra 1 til 3.\n"
        "Vennligst velg på nytt:\n"
        " - "
    ).lower()
    print()

if karakterOgStedvalg == "1":
    skrivInput("Trykk 'enter' når dere har valgt karakterer og steder.")

elif karakterOgStedvalg == "2":
    karakterliste = []
    skrivTekst("Skriv inn karakterer, en om gangen. Trykk 'enter' når du er ferdig.")
    while True:
        karakter = skrivInput(f"Karakter {len(karakterliste) + 1}: ").lower()
        if not karakter == "":
            karakterliste.append(karakter)
        elif len(karakterliste) < 1:
            time.sleep(0.5)
            skrivTekst("Du må skrive inn minst 1 karakter.")
        else:
            break
    time.sleep(0.5)
    print()
    stedliste = []
    skrivTekst("Skriv inn steder, en om gangen. Trykk 'enter' når du er ferdig.")
    while True:
        sted = skrivInput(f"Sted {len(stedliste) + 1}: ").lower()
        if not sted == "":
            stedliste.append(sted)
        elif len(stedliste) < 1:
            time.sleep(0.5)
            skrivTekst("Du må skrive inn minst 1 sted.")
        else:
            break

elif karakterOgStedvalg == "3":
    karakterliste = autoKarakterer
    stedliste = autoSteder

time.sleep(1)

print("\n-------------------------------\n")

#-----------------------------------------------------------KARAKTER- OG STED-FORDELING
if karakterOgStedvalg == "1":
    pass
else:
    skrivTekst(
        "Nå skal det fordeles! For hver spillers karakter- og sted-utdeling, skal kun de andre spillerne se karakteren og stedet som deles ut.\n"
        "(EKSEMPEL: Det er 3 spillere. Spiller 1 skal få karakter og sted. Kun spiller 2 og 3 får lov til å se hva det er.)\n"
        "Trykk 'enter' for å vise karakter og sted, trykk 'enter' igjen for å gjemme dem, og så videre til neste spiller.\n"
    )
    for navn in spillere:
        karakter = karakterliste[randint(0, len(karakterliste) - 1)]
        sted = stedliste[randint(0, len(stedliste) - 1)]
        skrivInput(f"Trykk 'enter' for å vise {navn}'s karakter og sted.")
        spillere[navn] = {
            "karakter": karakter,
            "sted": sted
        }
        skrivTekst(
            f"* {navn} sin karakter er: {karakter}\n"
            f"* {navn} sitt sted er: {sted}"
        )
        time.sleep(1)
        skrivInput(
            "\n"
            "Trykk 'enter' for å gjemme karakter og sted også gå videre."
        )
        for y in range(100):
            print()
    skrivTekst(
        "Alle karakterer og steder er fordelt nå!\n"
    )
    print("-------------------------------\n")
time.sleep(1)

#-----------------------------------------------------------SPILLEREGLER

skrivTekst("Da er det klart for å starte spillet! Dere har muligheten til å lese reglene igjen før dere starter.")
spilleregler()

#-----------------------------------------------------------SPILLRUNDER
skrivInput("Trykk 'enter' når dere er klare til å starte spillet.")

rundetall=0
playing = True
vinnere = []

flereRunder = playing
while playing == True:
    for navn in spillere:
        rundetall = rundetall + 1
        print(
            "\n"
            f"-------------------------------({rundetall})\n"
        )
        skrivTekst(
            f"Det er {navn} sin tur."
            "\n"
        )
        if playing == True:
            Type = randint(1, 4)
            if Type == 1:
                skrivTekst(
                    "Alle medspillere må gi et hint hver!\n"
                    "Du velger om medspillerne skal\n"
                    "gi hint om person eller sted."
                )
            elif Type == 2:
                skrivInput(
                    "Du har 30 sekunder på deg til å stille\n"
                    "så mange ja/nei-spørsmål som mulig!\n"
                    "Alle spørsmålene må være om\n"
                    "enten person eller sted.\n"
                    "Start tiden? ('Enter'): ")
                tid = 30
                for x in range (30):
                    print(tid)
                    time.sleep(1)
                    tid = tid - 1
                skrivTekst("Tiden er ute!")
            elif Type == 3:
                skrivTekst(
                    "Medspillerne skal lage en nyhetsoverskrift!\n"
                    "De skal lage en setning som kunne vært\n"
                    "tittelen på en nyhetssak om denne personen/stedet.\n"
                    "Du velger selv om det skal handle om\n"
                    "enten person eller sted."
                )
            else:
                skrivTekst(
                    "Medspillerne skal oppgi en bokstav!\n"
                    "Du velger selv hvilken bokstav du vil ha,\n"
                    "for eksempel første eller siste bokstav.\n"
                    "Du velger om medspillerne skal\n"
                    "gi hint om person eller sted."
                )
            turInput = skrivInput(
                "\n"
                "Neste tur? (For å gjette hvem og hvor du er, skriv 'svar'): "
            )
        if turInput.lower() == "svar":
            if karakterOgStedvalg == "2" or karakterOgStedvalg == "3":
                karakterGjett = skrivInput("Gjett karakteren din: ")
                if karakterGjett.lower() == spillere[navn]["karakter"].lower():
                    skrivTekst(f"Riktig, Du var {spillere[navn]['karakter']}!")
                else:
                    skrivTekst(
                        f"Feil karakter!"
                    )
                stedGjett = skrivInput("Gjett stedet ditt: ")
                if stedGjett.lower() == spillere[navn]["sted"].lower():
                    skrivTekst(f"Riktig, {spillere[navn]['sted']} er hvor du var!")
                else:
                    skrivTekst(
                        f"Feil sted!"
                    )
                
                if karakterGjett.lower() == spillere[navn]["karakter"].lower() and stedGjett.lower() == spillere[navn]["sted"].lower():
                    playing = False
                    vinnere.append(navn)
                    skrivTekst(
                        f"Gratulerer, du gjettet både karakteren og stedet ditt riktig, og har vunnet spillet!"
                    )
                else:
                    if playing == True:
                        skrivTekst(
                            f"Fordi du ikke gjettet både karakteren og stedet ditt riktig, må du fortsette spillet. Du kan gjette igjen senere!"
                        )
                    else:
                        skrivTekst(
                            f"Fordi du ikke gjettet både karakteren og stedet ditt riktig, er du ute av spillet..."
                        )
            else:
                gjettetRiktig = skrivInput(
                    "Gjett karakteren din for dine medspillere.\n"
                    "Deretter stedet ditt, og få dem til å svare på begge.\n"
                    "Gjettet du både riktig karakter og riktig sted?\n"
                    " - "
                ).lower()
                if gjettetRiktig == "ja":
                        playing = False
                        vinnere.append(navn)
                        skrivTekst(
                            f"Gratulerer, fordi du gjettet både karakteren og stedet ditt riktig, har du nå vunnet spillet!"
                        )
                elif gjettetRiktig == "nei":
                    if playing == True:
                        skrivTekst(
                            f"Det var synd... men du kan prøve igjen neste runde!"
                        )
                    else:
                        skrivTekst(
                            f"Det var synd. Siden noen har klart å gjette riktig, er du nå ute av spillet."
                        )
                while gjettetRiktig != "ja" and gjettetRiktig != "nei":
                    if gjettetRiktig == "ja":
                        playing = False
                        vinnere.append(navn)
                        skrivTekst(
                            f"Gratulerer, fordi du gjettet både karakteren og stedet ditt riktig, har du nå vunnet spillet!"
                        )
                    elif gjettetRiktig == "nei":
                        skrivTekst(
                            f"Det var synd... men du kan prøve igjen neste runde!"
                        )
                    gjettetRiktig = skrivInput(
                        "Ugyldig svar. Skriv 'ja' eller 'nei'.\n"
                        "Gjett karakteren din for dine medspillere.\n"
                        "Deretter stedet ditt, og få dem til å svare på begge.\n"
                        "Gjettet du både riktig karakter og riktig sted?\n"
                        " - "
                    ).lower()
if len(vinnere) > 1:
    vinnerPrint = ", ".join(vinnere[:-1]) + f" og {vinnere[-1]}"
elif vinnere:
    vinnerPrint = vinnere[0]
else:
    vinnerPrint = "none"

print("Spillet er nå over, takk for at dere spilte!\n"
        f"Vinnerne er {vinnerPrint}!!")