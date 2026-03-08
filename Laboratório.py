print("Hello,Matheus Henrique da Silva!")
idade = 21
ID = "2524MTH"
nome = "Matheus"
estudante = True

print (idade)
print (ID)
print (nome)
print (estudante)

print(int(input("Digite sua idade: ")))
print(str(input("Digite seu ID: ")))
print(str(input("Digite seu nome: ")))
print(bool(input("Digite seu status: ")))
if idade >=50:
    print("Apto para aposentadoria")
else:
    print("Inapto para aposentadoria")
avaliacao_1 = 100
avaliacao_2 = 80
avaliacao_3 = 70
avaliacao_4 = 60

Primeiro_valor = int(input("Digite o primeiro número:"))
Segundo_valor =  int(input("Digite o segundo número:"))

resultado = Primeiro_valor + Segundo_valor

print(f"A soma é: {resultado}")

if resultado >=120:
    print("Parabéns")
elif resultado >=100:
    print("Otimo")
else:
    print("Pessimo")

idade_aposentadoria = 65

if idade >= idade_aposentadoria:
    print(f"\nParabéns,{nome}!Você já está apto para a aposentadoria")
else:
    anos_faltantes = idade_aposentadoria - idade
    print(f"\n{nome},você ainda não está apto para a aposentadoria")
    print(f"Faltam {anos_faltantes} anos para atingir {idade_aposentadoria}anos")

# Lista
sorvete = ["baunilha","chocolate","morango","uva"]

while True:
    print("\n---Gerenciador de compras---")
    print("Sua lista atual:",sorvete)
    print("\n Escolha uma opção:")
    print("1:Adicionar sorvete")
    print("2:Remover sorvete")
    print("3:Listar/Visualizar sorvete")
    print("4:Consumir")
    print("5:Sair")

# Coleta: escolha do usuário
    Escolha = input("Digite o número da sua escolha (1,2,3,4,5):")
    if Escolha == "1":
        novo_item = input("Digite o nome do sorvete:").lower()
        sorvete.append(novo_item)
        print(f"{novo_item} item adicionado com sucesso!")
    elif Escolha == "2":
        item_a_remover = input ("Digite o nome do sorvete:").lower()
        if item_a_remover in sorvete:
            sorvete.remove(item_a_remover)
            print(f"{item_a_remover} com sucesso!")
        else:
            print(f"Erro: {item_a_remover} não está na lista")

    elif Escolha == "3":
        if sorvete:
            print("\n---Itens na sua lista---")
            for i, item in enumerate(sorvete):
                print(f"{i+1}. {item.title}")
            else:
                print("Sua lista está vazia")
    elif Escolha == "4":
        if sorvete:
            consumido = sorvete.pop(0)
            print(f"Você consumiu: {consumido}")
        else:
            print("Não há sorvetes para consumir")
    elif Escolha == "5":
         print("Sair do programa")
         break
    else:
        print("Opção inválida. Tente novamente.")


Lista_supermercado = ["Maça","Leite","Ovos"]
Lista_supermercado.append("Morango")
Lista_supermercado.remove("Maça")
print(Lista_supermercado)