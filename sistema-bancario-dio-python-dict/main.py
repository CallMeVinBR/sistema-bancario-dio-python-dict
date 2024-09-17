import sistema_bancario as main
from datetime import datetime

numero_conta = 1

print("SISTEMA BANCARIO".center(30, "="))
interface = """
    [s]. Sacar
    [d]. Depositar
    [e]. Exibir extrato
    
    [nu] Novo usuário
    [nc] Nova conta
    [lu] Listar usuários

    [q]. Sair
    
> """

while True:
    opcao = input(interface)
    
    if opcao.lower() == "nu":
        try:
            email = input("Insira o email: ")
            nome = input("Insira o nome: ")
            data = input("Insira a data de nascimento: ")
            cpf = int(input("Insira o CPF (somente números): "))
            logradouro = input("Insira seu logradouro: ")
            numero = input("Insira o numero do endereço: ")
            bairro = input("Insira o bairro: ")
            cidade = input("Insira a cidade ou sigla: ")
            estado = input("Insira o estado: ")
            endereco = f"{logradouro}, {numero} - {bairro} - {cidade} {estado}"
            data_formato = datetime.strptime(data, "%d/%m/%Y").date()
        
        except:
            print("Dados inválidos!")
        
        main.criar_usuario(email, nome, data_formato, cpf, endereco)
    
    elif opcao.lower() == "nc":
        try:
            email = input("Insira o email: ")
            agencia = input("Insira a agência: ")
            cpf = int(input("Insira o CPF: "))
            limite = float(input("Insira o limite: "))
        except:
            print("Dados inválidos!")
        
        main.criar_conta(email, agencia, numero_conta, cpf, limite)
        numero_conta += 1
    
    elif opcao.lower() == "lu":
        main.exibir_contas()
        
    elif opcao.lower() == "s":
        try:
            email = input("Insira o email: ")
            valor = float(input("Insira o valor do saque: "))
        except:
            print("Dados inválidos!")
            
        main.saque(email=email, valor=valor)
    
    elif opcao.lower() == "d":
        try:
            email = input("Insira o email: ")
            valor = float(input("Insira o valor do depósito: "))
        except:
            print("Dados inválidos!")
        
        main.deposito(email, valor)
    
    elif opcao.lower() == "e":
        try:
            email = input("Insira o email: ")
        except:
            print("Dados inválidos!")
        
        main.extrato(email)
        
    elif opcao == "q":
        break
    
    else:
        print("Opção inválida.")