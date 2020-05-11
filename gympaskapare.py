
  

Övningar = {"Bröst": ["bänkpress", "hantelpress", "kryssdrag", "pec deck", "hantelflyes", "lutande bänkpress", "bröstpress", "armhävningar"],
            "Mage": ["kabelcrunch", "hängande benlyft", "benlyft", "kabelrotationer", "magrullaren", "cyckelcrunch", "alternerande hälnuddningar", "crunches"],
            "Ben": ["knäböj", "frontböj", "rumänska marklyft", "utfallssteg", "höftlyft", "benpress", "bensträck", "legcurls"]
            }


antalP= int(input("Hur många pass vill du träna? > "))

antalM= int(input("Hur många minuter vill du träna? > "))
import math
antalÖ= float(antalM/2) #räknar med att varje övning tar 2 minuter att genomföra
print(round(antalÖ))  #vill ej printa sedan, antal övningar

i= 0
r= 1


print("\nBröst \nMage \nBen")
import random
while i< antalP:
    text="\nVad vill du träna pass " + str(r) + "? Välj från listan ovan. > "
    Aträna= input(text).capitalize()
    r += 1
    i += 1
    c=0
    while c< antalÖ:
      #print(Aträna in Övningar)
      gympass= (random.choice(Övningar[Aträna]))  
      print(gympass) #printar en random magövning
      c += 1
      