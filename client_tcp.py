import socket
import json

HOST = "127.0.0.1"
PORT = 65432

primoNumero = int(input("Inserisci il primo numero: "))
secondoNumero = int(input("Inserisci il secondo numero: "))
operazione = input("Inserisci l'operazione (+, -, *, /): ")

richiesta = {
    "primoNumero": primoNumero,
    "secondoNumero": secondoNumero,
    "operazione": operazione
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    messaggio = json.dumps(richiesta)
    sock.sendall(messaggio.encode())

    risposta = sock.recv(1024).decode()
    risultato = json.loads(risposta)["risultato"]

    print(f"Risultato: {risultato}")
