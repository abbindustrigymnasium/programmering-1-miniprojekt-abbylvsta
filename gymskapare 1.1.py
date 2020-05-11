import math 
import random

anv={"Vide": [
        {
            "Ålder": 13,
            "Vikt": 46,
            "Längd": 1.60
        }
    ],
     "Ylva": [
        {
            "Ålder": 17,
            "Vikt": 51,
            "Längd": 1.57
        }
    ],
}

Vem= input("Vänligen ange ditt namn > ").capitalize()

Que= input("Vill du veta din viktinformation? > ").capitalize()
if Que == ("Ja"): # Om ja så räknar den ut ditt BMI
    weigh= anv[Vem][0]
    a= int(weigh["Vikt"])

    lenght= anv[Vem][0]
    b= float(lenght["Längd"])
    
    BMI= float(a/b**2)
    BMI= str(round(BMI, 2))
    print("Ditt BMI är " + BMI )
else:
    print("Okej")


antalP= int(input("Hur många pass vill du träna " + str(Vem) + "? > "))

antalM= int(input("Hur många minuter vill du träna? > "))


antalÖ= float(antalM/2) #räknar med att varje övning tar 2 minuter att genomföra

Övningar = {"Bröst": ["bänkpress", "hantelpress", "kryssdrag", "pec deck", "hantelflyes", "lutande bänkpress", "bröstpress", "armhävningar"],
            "Mage": ["kabelcrunch", "hängande benlyft", "benlyft", "kabelrotationer", "magrullaren", "cyckelcrunch", "alternerande hälnuddningar", "crunches"],
            "Ben": ["knäböj", "frontböj", "rumänska marklyft", "utfallssteg", "höftlyft", "benpress", "bensträck", "legcurls"]
            }
i= 0
r= 1

print("\nBröst \nMage \nBen")


while i< antalP: #räknar hur många pass den ska göra och vad man vill träna varje pass
    text="\nVad vill du träna pass " + str(r) + "? Välj från listan ovan. > "
    Aträna= input(text).capitalize()
    print("\nDina övningar för pass " + str(r) + ":")
    r += 1
    i += 1
    c=0
    def övning():
        previous_value = None
        while True:
            value = random.choice(Övningar[Aträna])
            if value != previous_value:
                yield value
                previous_value = value
    ö= övning()
    for c in range(int(antalÖ)):
        print(next(ö))
        c += 1
        
        