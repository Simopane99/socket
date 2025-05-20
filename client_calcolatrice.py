import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        primo = float(input("Inserisci il primo numero: "))
        op = input("Inserisci l'operazione (+, -, *, /): ")
        secondo = float(input("Inserisci il secondo numero: "))

        richiesta = {
            "primoNumero": primo,
            "operazione": op,
            "secondoNumero": secondo
        }

        messaggio = json.dumps(richiesta)
        s.sendto(messaggio.encode(), (SERVER_IP, SERVER_PORT))

        risposta, _ = s.recvfrom(BUFFER_SIZE)
        risposta = json.loads(risposta.decode())

        if "risultato" in risposta:
            print(f"Risultato: {risposta['risultato']}")
        else:
            print(f"Errore: {risposta['errore']}")
    except Exception as e:
        print("Errore di input:", e)
    
    cont = input("Vuoi continuare? (s/n): ")
    if cont.lower() != 's':
        break

s.close()
