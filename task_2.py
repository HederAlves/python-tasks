# EXIGÊNCIA DE CÓDIGO 1 
# Mensagem de boas-vindas com meu nome
print("Bem-vindo(a) ao sistema de pedidos! Desenvolvido por Heder Alves.\n")

# Cardápio
print("--------------------Cardápio------------------------")
print("----------------------------------------------------")
print("---| Tamanho |   Cupuaçu (CP)   |   Açaí (AC)   |---")
print("----------------------------------------------------")
print("---|    P    |      R$ 9,00     |    R$ 11,00   |---")
print("---|    M    |     R$ 14,00     |    R$ 16,00   |---")
print("---|    G    |     R$ 18,00     |    R$ 20,00   |---")
print("----------------------------------------------------")

# Inicialização do acumulador de valor total
total = 0.0

# EXIGÊNCIA DE CÓDIGO 7
# Uso de while
while True:
    # EXIGÊNCIA DE CÓDIGO 2 
    # Input do sabor com verificação
    sabor = input("Digite o sabor desejado (CP para Cupuaçu / AC para Açaí):").strip().upper()
    if sabor != "CP" and sabor != "AC":
      # EXIGÊNCIA DE SAÍDA DE CONSOLE 2
        print("Sabor inválido. Tente novamente.\n")  
        continue  # EXIGÊNCIA DE CÓDIGO 7 
                  # uso do continue

    # EXIGÊNCIA DE CÓDIGO 3 
    # Input do tamanho com verificação
    tamanho = input("Digite o tamanho desejado (P/M/G): ").strip().upper()
    if tamanho not in ["P", "M", "G"]:
        # EXIGÊNCIA DE SAÍDA DE CONSOLE 3
        print("Tamanho inválido. Tente novamente.\n")
        continue  # volta para o início do laço

    # EXIGÊNCIA DE CÓDIGO 4 
    # if aninhado para verificar os preços
    preco = 0.0
    if sabor == "CP":
        if tamanho == "P":
            preco = 9.0
        elif tamanho == "M":
            preco = 14.0
        elif tamanho == "G":
            preco = 18.0
    elif sabor == "AC":
        if tamanho == "P":
            preco = 11.0
        elif tamanho == "M":
            preco = 16.0
        elif tamanho == "G":
            preco = 20.0
            
    # Traduz a sigla para o nome completo
    if sabor == "CP":
       nome_sabor = "Cupuaçu"
    elif sabor == "AC":
      nome_sabor = "Açaí"

    # EXIGÊNCIA DE CÓDIGO 5 Acumulador
    total += preco
    print(f"Pedido adicionado: {nome_sabor} tamanho {tamanho} por R${preco:.2f}.\n")

    # EXIGÊNCIA DE CÓDIGO 6 
    # Pergunta se deseja pedir mais
    mais = input("Deseja pedir mais alguma coisa? (S/N): ").strip().upper()
    if mais != "S":
        print() 
        break  # EXIGÊNCIA DE CÓDIGO 7 
               # uso do break

# Impressão do valor total dos pedidos
print(f"Valor total do pedido: R${total:.2f}")