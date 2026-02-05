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
RESET = "\033[0m"

# ==========================
# Comando que transforma whoami /priv em JSON
# ==========================
command = r"""
$raw = cmd /c "whoami /priv"

$lines = $raw | Select-Object -Skip 4

$result = @()

foreach ($line in $lines) {
    if ($line.Trim() -eq "") { continue }

    $parts = $line -split "\s{2,}"

    if ($parts.Count -ge 3) {
        $result += [PSCustomObject]@{
            Privilege = $parts[0]
            Description = $parts[1]
            State = $parts[2]
        }
    }
}

$result | ConvertTo-Json
"""

# ==========================
# Pega o output e carrega como JSON
# ==========================
output = run_ps(command)
privs = json.loads(output)

# ==========================
# Listas de privilégios por nível
# ==========================

# 🔴 CRITICAL: privesc MUITO comum / abuso direto
critical_privs = [
    "SeDebugPrivilege",
    "SeImpersonatePrivilege",
    "SeAssignPrimaryTokenPrivilege",
    "SeTcbPrivilege",
    "SeLoadDriverPrivilege",
    "SeBackupPrivilege",
    "SeRestorePrivilege",
    "SeTakeOwnershipPrivilege",
    "SeCreateTokenPrivilege"
]

# 🟡 RED FLAGS: perigosos dependendo do contexto
redflag_privs = [
    "SeSecurityPrivilege",
    "SeSystemEnvironmentPrivilege",
    "SeManageVolumePrivilege",
    "SeIncreaseQuotaPrivilege",
    "SeIncreaseBasePriorityPrivilege",
    "SeRemoteShutdownPrivilege",
    "SeShutdownPrivilege",
    "SeSystemtimePrivilege",
    "SeTimeZonePrivilege",
    "SeMachineAccountPrivilege",
    "SeEnableDelegationPrivilege",
    "SeCreatePagefilePrivilege",
    "SeSystemProfilePrivilege",
    "SeProfileSingleProcessPrivilege",
    "SeIncreaseWorkingSetPrivilege",
    "SeAuditPrivilege"
]

# ==========================
# Verifica cada privilégio e colore
# ==========================
for p in privs:
    priv_name = p["Privilege"]
    state = p["State"]

    state_upper = state.upper()

    # 🔴 CRITICAL (só se estiver Enabled)
    if priv_name in critical_privs:
        print(f"{RED}[CRITICAL] {priv_name} - {state}{RESET}")

    # 🟡 RED FLAG (só se estiver Enabled)
    elif priv_name in redflag_privs:
        print(f"{YELLOW}[RED FLAG] {priv_name} - {state}{RESET}")

    # 🟢 OK
    else:
        print(f"{GREEN}[OK] {priv_name} - {state}{RESET}")
