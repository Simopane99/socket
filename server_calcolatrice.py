import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((SERVER_IP, SERVER_PORT))

print("Server calcolatrice in attesa...")

while True:
    # Ricevo i dati
    data, addr = s.recvfrom(BUFFER_SIZE)
    if not data:
        break

    data = data.decode()
    data = json.loads(data)

    primoNumero = data["primoNumero"]
    operazione = data["operazione"]
    secondoNumero = data["secondoNumero"]

    try:
        if operazione == "+":
            risultato = primoNumero + secondoNumero
        elif operazione == "-":
            risultato = primoNumero - secondoNumero
        elif operazione == "*":
            risultato = primoNumero * secondoNumero
        elif operazione == "/":
            risultato = primoNumero / secondoNumero
        else:
            raise ValueError("Operazione non valida")

        risposta = json.dumps({"risultato": risultato})
    except Exception as e:
        risposta = json.dumps({"errore": str(e)})

    s.sendto(risposta.encode(), addr)
