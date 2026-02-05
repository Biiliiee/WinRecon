import os

RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODULE_DIR = os.path.join(BASE_DIR, "Modules")

def banner():
    os.system("cls")
    print(f"""{CYAN}{BOLD}
██╗    ██╗██╗███╗   ██╗██████╗ ███████╗ ██████╗ ███╗   ██╗
██║    ██║██║████╗  ██║██╔══██╗██╔════╝██╔════╝ ████╗  ██║
██║ █╗ ██║██║██╔██╗ ██║██████╔╝█████╗  ██║      ██╔██╗ ██║
██║███╗██║██║██║╚██╗██║██╔═══╝ ██╔══╝  ██║      ██║╚██╗██║
╚███╔███╔╝██║██║ ╚████║██║     ███████╗╚██████╗ ██║ ╚████║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
{RESET}{YELLOW}{BOLD}         Windows PrivEsc Checker Framework{RESET}
""")

def menu():
    print(f"{GREEN}[1]{RESET} Unquoted Service Paths")
    print(f"{GREEN}[2]{RESET} Checar permissões de Privilégio")
    print(f"{GREEN}[3]{RESET} Windows Basic")
    print(f"{GREEN}[4]{RESET} Sair")

while True:
    banner()
    menu()

    choice = input(f"\n{CYAN}Escolha uma opção >> {RESET}")

    if choice == "1":
        script_path = os.path.join(MODULE_DIR, "unquoted_service_paths.py")
        print(f"\n{YELLOW}[+] Executando Unquoted Service Paths...{RESET}\n")
        os.system(f'python "{script_path}"')
        input(f"\n{CYAN}Pressione ENTER para voltar ao menu...{RESET}")

    elif choice == "2":
        script_path = os.path.join(MODULE_DIR, "permissions.py")
        print(f"\n{YELLOW}[+] Executando verificação de permissões...{RESET}\n")
        os.system(f'python "{script_path}"')
        input(f"\n{CYAN}Pressione ENTER para voltar ao menu...{RESET}")

    elif choice == "3":
        script_path = os.path.join(MODULE_DIR, "Enumeration.py")
        print(f"\n{YELLOW}[+] Executando Enumeração...{RESET}\n")
        os.system(f'python "{script_path}"')
        input(f"\n{CYAN}Pressione ENTER para voltar ao menu...{RESET}")

    elif choice == "4":
        print(f"\n{RED}Saindo...{RESET}")
        break

    else:
        print(f"\n{RED}[!] Opção inválida!{RESET}")
        input(f"{CYAN}Pressione ENTER para tentar novamente...{RESET}")
