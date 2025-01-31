#Domanda 1
for tentativo in range(3):
    print("Qual è la capitale dell'Italia?")
    risposta = input()
    if risposta.strip().lower() == "roma":
        print("Esatto!")
        break
    else:
        print("Risposta errata!")
else:
    print("Hai esaurito i tentativi! La risposta corretta era 'Roma'.")
    
#Domanda 2
for tentativo in range(3):
    print("Dove si trova Berlino?")
    risposta = input()
    if risposta.strip().lower() == "germania":
        print("Esatto!")
        break
    else:
        print("Risposta errata!")
else:
    print("Hai esaurito i tentativi! La risposta corretta era 'Germania'.")
#Domanda 3
for tentativo in range(3):
    print("Barcellona è la capitale della Spagna? (Sì/No)")
    risposta = input()
    if risposta.strip().lower() == "no":
        print("Esatto!")
        break
    else:
        print("Risposta errata! Tentativi rimasti:")
else:
    print("Hai esaurito i tentativi! La risposta corretta era 'No'.")