import sys			
english = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", "when", "make", "can", "like", "time", "no", "just", "him", "know", "take", "person", "into", "year", "your", "good", "some", "could", "them", "see", "other", "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use", "two", "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"]			
german = ["der", "und", "sein", "in", "ein", "zu", "haben", "ich", "werden", "sie", "von", "nicht", "mit", "es", "sich", "auch", "auf", "für", "an", "er", "so", "dass", "können", "dies", "als", "ihr", "ja", "wie", "bei", "oder", "wir", "aber", "dann", "man", "da", "sein", "noch", "nach", "was", "also", "aus", "all", "wenn", "nur", "müssen", "sagen", "um", "über", "machen", "kein", "Jahr", "du", "mein", "schon", "vor", "durch", "geben", "mehr", "andere", "viel", "kommen", "jetzt", "sollen", "mir", "wollen", "ganz", "mich", "immer", "gehen", "sehr", "hier", "doch", "bis", "groß", "wieder", "Mal", "zwei", "gut", "wissen", "neu", "sehen", "lassen", "uns", "weil", "unter", "denn", "stehen", "jede", "Beispiel", "Zeit", "erste", "ihm", "ihn", "wo", "lang", "eigentlich", "damit", "selbst", "unser", "oben"]

spanish = ["el", "de", "que", "y", "a", "en", "un", "ser", "se", "no", "haber", "por", "con", "su", "para", "como", "estar", "tener", "le", "lo", "lo", "todo", "pero", "más", "hacer", "o", "poder", "decir", "este", "ir", "otro", "ese", "la", "si", "me", "ya", "ver", "porque", "dar", "cuando", "él", "muy", "sin", "vez", "mucho", "saber", "qué", "sobre", "mi", "alguno", "mismo", "yo", "también", "hasta", "año", "dos", "querer", "entre", "así", "primero", "desde", "grande", "eso", "ni", "nos", "llegar", "pasar", "tiempo", "ella", "sí", "día", "uno", "bien", "poco", "deber", "entonces", "poner", "cosa", "tanto", "hombre", "parecer", "nuestro", "tan", "donde", "ahora", "parte", "después", "vida", "quedar", "siempre", "creer", "hablar", "llevar", "dejar", "nada", "cada", "seguir", "menos", "nuevo", "encontrar"]

french = ["le", "de", "un", "à", "être", "et", "en", "avoir", "que", "pour", "dans", "ce", "il", "qui", "ne", "sur", "se", "pas", "plus", "pouvoir", "par", "je", "avec", "tout", "faire", "son", "mettre", "autre", "on", "mais", "nous", "comme", "ou", "si", "leur", "y", "dire", "elle", "devoir", "avant", "deux", "même", "prendre", "aussi", "celui", "donner", "bien", "où", "fois", "vous", "encore", "nouveau", "aller", "cela", "entre", "premier", "vouloir", "déjà", "grand", "mon", "me", "moins", "aucun", "lui", "temps", "très", "savoir", "falloir", "voir", "quelque", "sans", "raison", "notre", "dont", "non", "an", "monde", "jour", "monsieur", "demander", "alors", "après", "trouver", "personne", "rendre", "part", "dernier", "venir", "pendant", "passer", "peu", "lequel", "suite", "bon", "comprendre", "depuis", "point", "ainsi", "heure", "rester"]

arr = []
ecount = 0
gcount = 0
scount = 0
fcount = 0
for line in sys.stdin:
    words = line.split()
    for word in words:
        if(word in english):
            ecount += 1
        if(word in german):
            gcount += 1
        if(word in spanish):
            scount += 1
        if(word in french):
            fcount += 1
maxv = max(ecount, gcount, scount, fcount)
if ecount == maxv:
    print "English"
elif fcount == maxv:
    print "French"
elif gcount == maxv:
    print "German"
elif scount == maxv:
    print "Spanish"