import time
import random
from colorama import Fore, Back, Style, init

init(autoreset=True)

def print_slowly(text, color=Fore.WHITE, delay=0.02):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(random.uniform(delay/2, delay*1.5))
    print()  # Newline at the end

def hacker_terminal():
    # ASCII Art
    skull = """
     ______
    < INIT >
     ------
            \\   ^__^
             \\  (oo)\\_______
                (__)\\       )\\/\\
                    ||----w |
                    ||     ||
    """
    print(Fore.MAGENTA + skull)
    time.sleep(1)

    print_slowly("[*] Booting up brute force kernel...", Fore.CYAN)
    time.sleep(0.5)
    print_slowly("[*] Establishing link to server...", Fore.CYAN)
    time.sleep(0.5)

    for _ in range(random.randint(3, 7)):
        ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        print_slowly(f"[*] Probing {ip}...", Fore.YELLOW)
        time.sleep(0.5)
        if random.choice([True, False]):
            print_slowly("[!] Access denied!", Fore.RED)
        else:
            print_slowly("[+] Connection established!", Fore.GREEN)
        time.sleep(0.5)

    print_slowly("[*] Breaching firewalls...", Fore.CYAN)
    firewalls = ["Norton", "McAfee", "Bitdefender", "Kaspersky", "Windows Defender"]
    for fw in firewalls:
        time.sleep(0.5)
        if random.choice([True, False]):
            print_slowly(f"[!] {fw} firewall breached!", Fore.GREEN)
        else:
            print_slowly(f"[x] Failed to breach {fw}!", Fore.RED)

    print_slowly("[*] Extracting data files...", Fore.CYAN)
    time.sleep(1)
    for _ in range(random.randint(2, 5)):
        data_file = f"file_{random.randint(1000, 9999)}.txt"
        print_slowly(f"[+] Extracted: {data_file}", Fore.BLUE)
        time.sleep(0.5)

    print_slowly("[*] Uploading payload to target system...", Fore.CYAN)
    time.sleep(1)
    print_slowly("[+] Payload upload complete!", Fore.GREEN)
    time.sleep(0.5)

    print_slowly("[*] Establishing backdoor for future access...", Fore.CYAN)
    time.sleep(1)
    print_slowly("[*] Registering encryption keys...", Fore.CYAN)
    time.sleep(1)
    print_slowly("[+] Backdoor established!", Fore.GREEN)
    time.sleep(0.5)

    print_slowly("[*] Deleting log files...", Fore.CYAN)
    time.sleep(0.5)
    print_slowly("[*] Killing connection...", Fore.CYAN)
    time.sleep(0.5)
    print_slowly("[*] Brute force protocol offline.", Fore.CYAN)

if __name__ == "__main__":
    hacker_terminal()
