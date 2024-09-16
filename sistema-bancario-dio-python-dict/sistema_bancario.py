from datetime import datetime

LIMITE_SAQUES = 10

contas = {}
usuarios = {}
i = 0

def criar_usuario(email, nome, cpf):  
    if email not in usuarios and cpf not in usuarios:
        try:
            usuarios.update({
                f"{email}": {
                    "nome": nome,
                    "cpf": cpf
                }
            })
        except Exception as e:
            print(f"Erro ao criar o usuário: {str(e)}")
    
        print("Usuário criado com sucesso!")
    
    else:
        print("Erro ao criar o usuário: Usuário já existe ou campos vazios")

def criar_conta(email):
    try:
        agencia = int(input(f"Informe a agencia do usuario ({email}): "))
        limite = float(input(f"Informe o limite da conta ({email}): "))
    except:
        print("Fornecer apenas numeros!")
    
    contas.update({
        f"{email}": {
            "agencia": agencia,
            "saldo": 0,
            "limite": limite,
            "extrato": {
                "depositos": [],
                "saques": []
            }
        }
    })
    print("Cadastro finalizado.")

def saque(email, valor):
    limite = contas[email]["limite"]
    saldo = contas[email]["saldo"]
    numero_saques = len(contas[email]["extrato"]["saques"])
    
    if valor > limite:
        print("Saque não autorizado: Limite excedido.")
    
    elif valor > saldo:
        print( "Saque não autorizado: Saldo insuficiente.")
    
    elif numero_saques == LIMITE_SAQUES:
        print("Saque não autorizado: Limite de número de saques atingido.")
    
    else:
        contas[email]["saldo"] -= valor
        contas[email]["extrato"]["saques"].append({
            "valor": valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M")
        })
        
    print(f"Saldo atual: {saldo}")
    
def deposito(email, valor):
    saldo = contas[email]["saldo"]
    
    # Se não for float nem int
    if not isinstance(valor, (float, int)):
        print("Deposito não autorizado: Valor inválido.")
    
    elif valor < 0:
        print("Deposito não autorizado: Valor negativo.")

    else:
        contas[email]["saldo"] += valor
        contas[email]["extrato"]["depositos"].append({
            "valor": valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M")
        })
    
    print(f"Saldo atual: {saldo}")

def extrato(email):
    extrato = contas[email]["extrato"]
    for transacao in extrato["depositos"]:
        print(f"Deposito: {transacao['valor']} - {transacao['data']}")
    
    for transacao in extrato["saques"]:
        print(f"Saque: {transacao['valor']} - {transacao['data']}")


# SIMULAÇÃO DE USO
# case "nc" (nova conta):
while i == 0:
    try:
        email = str(input("Informe o email do usuario: "))
        nome = str(input("Informe o nome do usuario: "))
        cpf = int(input("Informe o CPF do usuario (somente numeros): "))
        i += 1
            
    except:
        print("Dados inválidos!\n")
        i = 0

# Keyword only, pois informa variável=valor
criar_usuario(email=email, nome=nome, cpf=cpf)
criar_usuario(email=email, nome=nome, cpf=cpf)

for usuario, dados in usuarios.items():
    print(usuario, dados)
    
for conta, dados in contas.items():
    print(conta, dados)