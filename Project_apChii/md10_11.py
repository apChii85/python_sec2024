import threading
import time
import signal
import sys

ievaditais = []
# Sreda lock objekts
Ievad_lock = threading.Lock()

# Funkcija, kas lasa klaviatūrass ievadi un glabā to vēsturē
def read_input():
    while True:
        try:
            ievade = input("Ievadi kaut ko un nospied ENTER: ")
            
            # Pievienojam ievadi vēsturei
            with Ievad_lock:
                ievaditais.append(ievade)
            
            # Izdrukājam vēsturi
            print("Ievades vēsture atjaunota:", ievaditais)
        
        except KeyboardInterrupt:
            # iziešana no cikla ja ir ctrl+c
            print("\nCtrl+C nospiests, apturot ievadi...")
            break
        except EOFError:
            # papildus tekstu novākšana
            print("\nProgramma tiek pārtraukta...")
            break

# Funkcija kas ik pa 5sec pieprasa ievades vēsturi
def vesture():
    while True:
        time.sleep(5)  # Gaidām 5 sekundes
        with Ievad_lock:
            # parāda pēdējo vēstures ierakstu, ja tas ir pieejams
            if ievaditais:
                print("Pēdējais ievadītais:", ievaditais[-1])
            else:
                print("Vēl nekas nav ievadīts.")

# Funkcija, kas apstrādā SIGINT signālu
def sigints(sig, frame):
    print("\nProgrammas beigas")
    sys.exit(0) 

# Galvenā funkcija, kas pārvalda pavedienus
def main():
    # Pieslēdzam signal handler, lai apstrādātu Ctrl+C
    signal.signal(signal.SIGINT, sigints)

    # Izveidojam sredus
    Ievad_proc = threading.Thread(target=read_input, daemon=True)
    Ievaditais_proc = threading.Thread(target=vesture, daemon=True)
    # Startējam sredus
    Ievad_proc.start()
    Ievaditais_proc.start()
    # Gaida, līdz sredi pabeidz savu darbu
    try:
        Ievad_proc.join()
        Ievaditais_proc.join()
    except KeyboardInterrupt:
        # Ja nospiests Ctrl+C, mēs varam iziet no galvenā pavediena
        print("\nPārtraukums pieņemts. Programma tiek slēgta...")
        sys.exit(0)

if __name__ == "__main__":
    main()
