import csv
import os

filename = 'registros.csv'

if not os.path.exists(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nome', 'Protocolo', 'Número Ticket', 'Data de Abertura', 'Status', 'Data da Última Consulta'])
        print(f"Arquivo {filename} criado com sucesso!")

def incluir_registro():
    nome = input("Nome: ")
    protocolo = input("Protocolo: ")
    num_ticket = input("Número do Ticket: ")
    data_abertura = input("Data de Abertura: ")
    status = input("Status: ")
    data_ultima_consulta = input("Data da Última Consulta: ")

    with open('registros.csv', mode='a', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([nome, protocolo, num_ticket, data_abertura, status, data_ultima_consulta])

def listar_registros():
    with open('registros.csv', mode='r') as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            print(linha)

def excluir_registro():
    nome = input("Digite o nome do registro a ser excluído: ")
    registros = []
    with open('registros.csv', mode='r') as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            registros.append(linha)
    with open('registros.csv', mode='w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        for linha in registros:
            if linha[0] != nome:
                writer.writerow(linha)

def editar_registro():
    nome = input("Digite o nome do registro a ser editado: ")
    registros = []
    with open('registros.csv', mode='r') as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            registros.append(linha)
    with open('registros.csv', mode='w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        for linha in registros:
            if linha[0] == nome:
                linha[1] = input("Protocolo: ")
                linha[2] = input("Número do Ticket: ")
                linha[3] = input("Data de Abertura: ")
                linha[4] = input("Status: ")
                linha[5] = input("Data da Última Consulta: ")
            writer.writerow(linha)

while True:
    print("1-Incluir")
    print("2-Editar")
    print("3-Listar")
    print("4-Excluir")
    print("5-Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        incluir_registro()
    elif opcao == "2":
        editar_registro()
    elif opcao == "3":
        listar_registros()
    elif opcao == "4":
        excluir_registro()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")