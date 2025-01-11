import socket
import requests

def get_local_ip():
    """
    Funkcija, kas atrod lokālo IP adresi.
    """
    try:
        # Izveido savienojumu un iegūst lokālo IP
        local_ip = socket.gethostbyname(socket.gethostname())
        return local_ip
    except Exception as e:
        return f"Kļūda, nosakot lokālo IP: {e}"

def get_public_ip():
    """
    Funkcija, kas atrod publisko IP adresi, izmantojot ārēju API.
    """
    try:
        # Pieprasījums uz API, lai noskaidrotu publisko IP
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        public_ip = response.json()["ip"]
        return public_ip
    except Exception as e:
        return f"Kļūda, nosakot publisko IP: {e}"

# Galvenā programma
if __name__ == "__main__":
    print("IP adrešu noteikšana:")
    print("-" * 30)

    # Iegūst un izvada lokālo IP adresi
    local_ip = get_local_ip()
    print(f"Lokālā IP adrese: {local_ip}")

    # Iegūst un izvada publisko IP adresi
    public_ip = get_public_ip()
    print(f"Publiskā IP adrese: {public_ip}")