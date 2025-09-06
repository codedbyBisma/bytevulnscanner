from termcolor import colored
def banner():
    print(colored(r"""
   ____        __        __   _      ____                                      
  |  _ \  ___  \ \      / /__| |__  / ___|  ___ __ _ _ __  _ __   ___ _ __ 
  | | | |/ _ \  \ \ /\ / / _ \ '_ \ \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
  | |_| |  __/   \ V  V /  __/ |_) | ___) | (_| (_| | | | | | | |  __/ |   
  |____/ \___|    \_/\_/ \___|_.__/ |____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                                            
    """, "cyan"))
    print(colored("           🚨 ByteVulnScanner 🚨", "red"))
    print(colored("  Developed by Bisma | Python + Nmap + Socket\n", "yellow"))
def menu():
    print(colored("Select an option:", "green"))
    print("[1] Ping Sweep")
    print("[2] Active Host Enumeration")
    print("[3] Port Scanner")
    print("[4] DNS Lookup")
    print("[5] Exit")
import nmap

def port_scan(target):
    scanner = nmap.PortScanner()
    print(colored(f"\n[+] Scanning Target: {target}", "yellow"))
    scanner.scan(target, '1-1024', '-v')
    for host in scanner.all_hosts():
        print(colored(f"\nHost: {host} ({scanner[host].hostname()})", "cyan"))
        print(f"State: {scanner[host].state()}")
        for proto in scanner[host].all_protocols():
            print(colored(f"Protocol: {proto}", "green"))
            lport = scanner[host][proto].keys()
            for port in sorted(lport):
                state = scanner[host][proto][port]['state']
                print(f"Port: {port}\tState: {state}")

if __name__ == "__main__":
    banner()
    while True:
        menu()
        choice = input(colored("Enter your choice: ", "red"))
        
        if choice == "1":
            print(colored("Ping Sweep coming soon...", "blue"))
        elif choice == "2":
            print(colored("Active Host Enumeration...", "blue"))
        elif choice == "3":
            target = input("Enter target IP: ")
            port_scan(target)
        elif choice == "4":
            print(colored("DNS Lookup coming soon...", "blue"))
        elif choice == "5":
            print(colored("Exiting... Stay Safe 🔒", "red"))
            break
        else:
            print(colored("Invalid choice. Try again.", "yellow"))
