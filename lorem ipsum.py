import random


WORDS=['cvičení', 'ložisko', 'vidět', 'práce', 'stane', 'se', 'to', 'jsou', 'že', 'jo', 'pro', 'nám', 'mu', 'když', 'služby', 'až', 'na', 'nesnáším', 'bude', 'založen', 'jako', 'kdyby', 'nebo', 'kdokoliv', 'vybrat', 'proto', 'ne', 'on', 'nenávidí', 'čas', 'hledal', 'nejhodnější', 'snadný', 'ani', 'nic', 'urychlený', 'život', 'opravdu', 'sám', 'pokud', 'mysl', 'přijít', 'být', 'chován', 'vůle', 'cesta', 'narozený', 'prostě', 'a', 'následovat', 'ale', 'z', 'potěšení', 'krát', 'pravdy', 'racionální', 'předpokládat', 'přihodit', 'náš', 'prosím', 'něco', 'let', 'poskytnout', 'současnost', 'dárek', 'věc', 'potřeby', 'bere', 'pochopit', 'vskutku', 'můžeme', 'musíš', 'žalobci', 'odkud', 'moudře', 's', 'potěšením', 'hrubý', 'chvály', 'vyřešeno', 'milovat', 'kde', 'nějak', 'často', 'obviňovat', 'volný', 'uvolnit', 'sebe', 'řekl', 'odmítnutí', 'oni', 'nevědí', 'bolesti', 'nicméně', 'překáží', 'malý', 'hlavní', 'odmítnout', 'slepý', 'žádný', 'celý', 'vybraný', 'vedeme', 'bolest', 'úzkost', 'nich', 'zármutek', 'protože', 'problémy', 'velký', 'rozdíl', 'každý', 'triky', 'příjemný', 'ona', 'který', 'jak', 'tělo', 'jemnost', 'opustit', 'těžce', 'pracující', 'výsledek', 'tento', 'chtíč', 'obvinit', 'věci', 'chyba', 'méně', 'jeho', 'nikdo', 'prchá', 'služale', 'v', 'kritizován', 'nikdy', 'nech', 'ho', 'utéct', 'vynálezce', 'blahoslavený', 'odražen', 'odmítl', 'co', 'vysvětlím', 'otevřel', 'bych', 'následek', 'drsnější', 'výhody', 'volba', 'odpuzuje', 'přijdu', 'architekt', 'je', 'flexibilita', 'jim', 'ostatní', 'držený', 'zničen', 'dále', 'dělat', 'většina', 'zkažený', 'elita', 'přesně', 'tak', 'incident']
sections=[]
paragraphs=[]

for _ in range(int(input("počet odstavců: "))):
    paragraph = ""
    for _ in range(random.randint(2,5)):

        sentence="" 

        for _ in range(random.randint(1,5)):
            sections.append(" ".join(random.sample(WORDS,random.randint(3,12))))

        sentence = ", ".join(sections).capitalize() + random.choice([".","?"])
        paragraph += sentence + " "
    paragraphs.append(paragraph[:-1])

output="\n".join(paragraphs)


file = open("document.rtf","w")
file.write(output)
file.close()