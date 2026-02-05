import subprocess
import json
import os

def run_ps(command):
    result = subprocess.run(
        ["powershell", "-NoProfile", "-Command", command],
        capture_output=True,
        text=True
    )
    return (result.stdout + result.stderr).strip()  # inclui stderr pra pegar mensagens de erro

command = r"""
Get-CimInstance Win32_Service |
Select Name, PathName |
ConvertTo-Json
"""

output = run_ps(command)
services = json.loads(output)

if isinstance(services, dict):
    services = [services]

RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

dangerous_perms = ["SERVICE_CHANGE_CONFIG", "WRITE_DAC", "WRITE_OWNER"]

for svc in services:
    name = svc["Name"]
    path = svc["PathName"]

    if path and ".exe" in path.lower():

        path_clean = path.strip()
        exe_path = path_clean.lower().split(".exe")[0] + ".exe"

        if " " in exe_path and not path_clean.startswith('"'):
            print(f"{RED}[!]{RESET} {YELLOW}Vulnerável Possível:{RESET} {name}")
            print(f"{YELLOW}Path:{RESET} {path}\n")

            folder = input("Digite o caminho para checar permissões e uma possível vulnerabilidade: ")

            command = f'icacls "{folder}"'
            output = run_ps(command)
            print(output)
