LIMITE_SAQUES = 10

contas = {}
usuarios = {}
i = 0

def criar_usuario(email, nome, cpf):
    try:
        usuarios.update({
            f"{email}": {
                "nome": nome,
                "cpf": cpf
            }
        })
    except:
        return "Erro ao criar o usuário."
    
    print("Usuário criado com sucesso!")
    return criar_conta(email=email)

def criar_conta(email):
    try:
        agencia = int(input(f"Informe a agencia do usuario ({email}): "))
    except:
        return "Fornecer apenas numeros!"
    
    usuarios[email]["agencia"] = agencia
    contas.update({
        f"{email}": {
            "agencia": agencia,
            "saldo": 0
        }
    })
    return "Cadastro finalizado."

while i == 0:
    try:
        email = str(input("Informe o email do usuario: "))
        nome = str(input("Informe o nome do usuario: "))
        cpf = int(input("Informe o CPF do usuario (somente numeros): "))
        i += 1
            
    except:
        print("Dados inválidos!\n")
        i = 0


criar_usuario(email=email, nome=nome, cpf=cpf)  

for usuario, dados in usuarios.items():
    print(usuario, dados)
    
for conta, dados in contas.items():
    print(conta, dados)