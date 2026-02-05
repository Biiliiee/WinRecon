# WinReconPy

WinReconPy é uma ferramenta modular em **Python** para realizar **reconhecimento e auditoria básica de segurança em sistemas Windows**, focada em identificar possíveis vetores de **Privilege Escalation (PrivEsc)**.

O projeto funciona através de um menu interativo que executa módulos separados dentro da pasta `Modules/`.

---

## Funcionalidades

### [1] Unquoted Service Paths
Verifica serviços do Windows que podem estar vulneráveis ao problema de **Unquoted Service Path**, onde caminhos com espaços sem aspas podem permitir execução de binários maliciosos.

- Enumera serviços via `Win32_Service`
- Detecta possíveis caminhos vulneráveis
- Permite checar permissões com `icacls`

---

### [2] Checar permissões de Privilégio
Analisa os privilégios do usuário atual usando:

- `whoami /priv`

O script classifica os privilégios como:

- **CRITICAL**
- **RED FLAG**
- **OK**

Isso ajuda a identificar permissões frequentemente exploradas em escalonamento de privilégios (ex: `SeImpersonatePrivilege`, `SeDebugPrivilege`, etc).

---

### [3] Windows Basic Audit
Executa uma auditoria rápida no sistema e retorna estatísticas importantes:

- Quantidade de usuários sem senha
- Quantidade de grupos locais
- Quantidade de portas TCP em estado **LISTEN**

---

## Estrutura do Projeto

WinReconPy/
│
├── winrecon.py
└── Modules/
├── Enumeration.py
├── permissions.py
└── unquoted_service_paths.py


---

## Requisitos

- Windows 10/11
- Python 3.x
- PowerShell habilitado

⚠️ Algumas verificações podem exigir execução como **Administrador** dependendo do ambiente.

---

## Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/<seu-usuario>/WinReconPy.git
Entre na pasta do projeto:

cd WinReconPy
Execute o script principal:

python winrecon.py
