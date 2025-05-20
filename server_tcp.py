import socket
import json

IP = "127.0.0.1"
PORTA = 65432
DIM_BUFFER = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((IP, PORTA))
    sock_server.listen()
    print(f"Server in ascolto su {IP}:{PORTA}...")

    while True:
        connessione, indirizzo = sock_server.accept()
        with connessione as client:
            print(f"Connessione stabilita con {indirizzo}")
            dati = client.recv(DIM_BUFFER)

            if not dati:
                continue

            dati = dati.decode()
            richiesta = json.loads(dati)

            primoNumero = richiesta["primoNumero"]
            secondoNumero = richiesta["secondoNumero"]
            operazione = richiesta["operazione"]

            risultato = None
            if operazione == "+":
                risultato = primoNumero + secondoNumero
            elif operazione == "-":
                risultato = primoNumero - secondoNumero
            elif operazione == "*":
                risultato = primoNumero * secondoNumero
            elif operazione == "/":
                if secondoNumero != 0:
                    risultato = primoNumero / secondoNumero
                else:
                    risultato = "Errore: divisione per zero"
            else:
                risultato = "Errore: operazione non valida"

            risposta = json.dumps({"risultato": risultato})
            client.sendall(risposta.encode())
