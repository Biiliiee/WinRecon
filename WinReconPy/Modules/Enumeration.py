import subprocess
import json

# ==========================
# Função para rodar PowerShell
# ==========================
def run_ps(command):
    result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", command],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )
    return (result.stdout or "").strip()

# ==========================
# Cores ANSI
# ==========================
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ==========================
# Script PowerShell (gera JSON)
# ==========================
command = r"""
$usersNoPass = (Get-LocalUser | Where-Object { $_.PasswordRequired -eq $false }).Count
$groupsCount = (Get-LocalGroup).Count
$openPorts = (Get-NetTCPConnection -State Listen).Count

$result = [PSCustomObject]@{
    UsersWithoutPassword = $usersNoPass
    GroupsCount = $groupsCount
    OpenPortsListening = $openPorts
}

$result | ConvertTo-Json
"""

# ==========================
# Executa e carrega JSON
# ==========================
output = run_ps(command)
data = json.loads(output)

users_no_pass = data["UsersWithoutPassword"]
groups_count = data["GroupsCount"]
open_ports = data["OpenPortsListening"]

# ==========================
# Print formatado + cores
# ==========================
print(f"{CYAN}==============================")
print("   WINDOWS BASIC AUDIT")
print(f"=============================={RESET}\n")

# Usuários sem senha
if users_no_pass > 0:
    print(f"{RED}[ALERTA]{RESET} Existem {RED}{users_no_pass}{RESET} usuários sem senha.")
else:
    print(f"{GREEN}[OK]{RESET} Nenhum usuário sem senha encontrado.")

# Grupos locais
print(f"{CYAN}[INFO]{RESET} Existem {YELLOW}{groups_count}{RESET} grupos locais no sistema.")

# Portas abertas
if open_ports > 50:
    print(f"{YELLOW}[RED FLAG]{RESET} Existem {YELLOW}{open_ports}{RESET} portas em estado LISTEN.")
else:
    print(f"{GREEN}[OK]{RESET} Existem {GREEN}{open_ports}{RESET} portas em estado LISTEN.")

print()
