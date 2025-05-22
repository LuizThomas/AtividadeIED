pessoas = []

while True:
    tem_transporte = input("Você tem transporte? (sim/não): ")

    if tem_transporte == "sim":
        print("Bem-vindo!\n")
    elif tem_transporte == "não":
        nome = input("Digite seu nome: ")
        idade = input("Digite sua idade: ")
        pessoas.append({"nome": nome, "idade": idade})
        print("Pessoa adicionada!\n")
    else:
        print("Resposta inválida.\n")
        continue

    continuar = input("Deseja continuar? (sim/não/sair): ")
    if continuar == "não":
        break
    elif continuar == "sair":
        print("Programa encerrado.")
        break
    elif continuar != "sim":
        print("Resposta inválida.")
