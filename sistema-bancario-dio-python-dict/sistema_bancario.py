from datetime import datetime

LIMITE_SAQUES = 10

contas = {}
usuarios = {}
i = 0

def criar_usuario(email, nome, data, cpf, endereco):  
    if not email in usuarios and not cpf in usuarios:
        try:
            usuarios.update({
                f"{email}": {
                    "nome": nome,
                    "data_nascimento": data,
                    "cpf": cpf,
                    "endereco": endereco
                }
            })
        except Exception as e:
            print(f"Erro ao criar o usuário: {str(e)}")
    
        print("Usuário criado com sucesso!")
    
    else:
        print("Erro ao criar o usuário: Usuário já existe ou campos vazios")

def criar_conta(email, agencia, numero, cpf, limite):
    if cpf != usuarios[email]["cpf"]:
        print("Erro ao criar a conta: Usuário não existe")
        
    else:
        contas.update({
            f"{email}": {
                "agencia": agencia,
                "numero": numero,
                "usuario": cpf,
                "saldo": 0,
                "limite": limite,
                "extrato": {
                    "depositos": [],
                    "saques": []
                }
            }
        })
        print("Cadastro finalizado.")

# Keyword only
def saque(email, valor):
    if not email in contas:
        print("Erro ao realizar saque: Conta não existe")
    else:
        limite = contas[email]["limite"]
        numero_saques = len(contas[email]["extrato"]["saques"])
        
        if valor > limite:
            print("Saque não autorizado: Limite excedido.")
        
        elif valor > contas[email]["saldo"]:
            print("Saque não autorizado: Saldo insuficiente.")
        
        elif numero_saques == LIMITE_SAQUES:
            print("Saque não autorizado: Limite de número de saques atingido.")
            
        elif valor < 0:
            print("Saque não autorizado: Valor inválido.")
        
        else:
            contas[email]["saldo"] -= valor
            contas[email]["extrato"]["saques"].append({
                "valor": valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M")
            })
            
        print(f"Saldo atual: {contas[email]['saldo']}")
    
# Positional only
def deposito(email, valor):
    if not email in contas:
        print("Erro ao realizar depósito: Conta não existe")
    else:
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
        
        print(f"Saldo atual: {contas[email]['saldo']}")

def extrato(email):
    if not email in contas:
        print("Erro ao obter extrato: Conta não existe")
    else:
        extrato = contas[email]["extrato"]
        for transacao in extrato["depositos"]:
            print(f"Deposito: {transacao['valor']} - {transacao['data']}")
        
        for transacao in extrato["saques"]:
            print(f"Saque: {transacao['valor']} - {transacao['data']}")

def exibir_contas():
    for conta in contas:
        print(f"""
                Email: {conta}
                    Agência: {contas[conta]["agencia"]}
                    Saldo: {contas[conta]["saldo"]}
                    Limite: {contas[conta]["limite"]}
                    Extrato:
                        {contas[conta]["extrato"]}
                """)
    
    for usuario in usuarios:
        print(f"""
                Email: {usuario}
                    Nome: {usuarios[usuario]["nome"]}
                    Data de nascimento: {usuarios[usuario]["data_nascimento"]}
                    CPF: {usuarios[usuario]["cpf"]}
                    Endereço: {usuarios[usuario]["endereco"]}
                """)