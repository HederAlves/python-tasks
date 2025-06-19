# EXIGÊNCIA DE CÓDIGO 1
# Mensagem de boas-vindas com meu nome
print("Bem-vindo(a) ao sistema de compras! Desenvolvido por Heder Alves.\n")

# EXIGÊNCIA DE CÓDIGO 2
# Entrada do valor unitário e da quantidade do produto
valor_unitario = float(input("Digite o valor unitário do produto: R$ "))
quantidade = int(input("Digite a quantidade desejada: "))

# EXIGÊNCIA DE CÓDIGO 4
# Cálculo do valor total sem desconto
valor_total = valor_unitario * quantidade

# EXIGÊNCIA DE CÓDIGO 3 e 5
# Cálculo do desconto com base no valor total
if valor_total < 2500:
    desconto_percentual = 0
elif valor_total < 6000:
    desconto_percentual = 4
elif valor_total < 10000:
    desconto_percentual = 7
else:
    desconto_percentual = 11

# EXIGÊNCIA DE CÓDIGO 4
# Cálculo do valor do desconto e valor final com desconto
desconto_valor = (desconto_percentual / 100) * valor_total
valor_com_desconto = valor_total - desconto_valor

# Exibição dos resultados
print(f"\nResumo do pedido:")
print(f"Valor total SEM desconto: R$ {valor_total:.2f}")
print(f"Valor total COM desconto: R$ {valor_com_desconto:.2f}")

print(f"\nResumo do desconto:")
print(f"Desconto aplicado: {desconto_percentual}%")
print(f"Valor do desconto: R$ {desconto_valor:.2f}")