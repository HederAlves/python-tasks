# EXIGÊNCIA DE CÓDIGO E CONSOLE 1 
# Mensagem de boas-vindas com meu nome
print("Bem-vindo(a) ao sistema de copiadoras! Desenvolvido por Heder Alves.\n")

# EXIGÊNCIA DE CÓDIGO 2
# Função para escolher o serviço desejado
def escolha_servico():
    while True:
        print("Escolha o serviço desejado")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópiao")
        servico = input(">>").strip().lower()

        if servico == 'dig':
            return 1.10  # Digitalização
        elif servico == 'ico':
            return 1.00  # Impressão Colorida
        elif servico == 'ipb':
            return 0.40  # Impressão Preto e Branco
        elif servico == 'fot':
            return 0.20  # Fotocópia
        else:
            # EXIGÊNCIA DE SAÍDA DE CONSOLE 2
            print("Serviço inválido. Por favor, escolha entre: DIG, ICO, IPB ou FOT. \n")

# EXIGÊNCIA DE CÓDIGO 3
# Função para obter o número de páginas e aplicar desconto
def num_pagina():
    while True:
      # EXIGÊNCIA DE CÓDIGO 6
      # try
        try:
            paginas = int(input("Digite o número de páginas: "))
            print()
            if paginas >= 20000:
                # EXIGÊNCIA DE SAÍDA DE CONSOLE 3
                print("Não aceitamos tantas páginas de uma vez.")
                print("Por favor, entre com o número de páginas menor que 20000. \n")
                continue
            elif paginas >= 2000:
                return paginas * 0.75  # 25% de desconto
            elif paginas >= 200:
                return paginas * 0.80  # 20% de desconto
            elif paginas >= 20:
                return paginas * 0.85  # 15% de desconto
            elif paginas > 0:
                return paginas * 1.00  # Sem desconto
            else:
                print("Número de páginas deve ser maior que 0. \n")
      # EXIGÊNCIA DE CÓDIGO 6
      # except
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido. \n")

# EXIGÊNCIA DE CÓDIGO 4
# Função para escolher o serviço adicional
def servico_extra():
    while True:
        print("Deseja adicionar algum serviço?")
        print("1 - Encadernação Simples - R$ 15.00")
        print("2 - Encadernação Capa Dura - R$ 40.00")
        print("0 - Não desejo mais nada")
        extra = input(">>").strip()

        if extra == '1':
            return 15.00
        elif extra == '2':
            return 40.00
        elif extra == '0':
            return 0.00
        else:
            print("Opção inválida. Digite 1, 2 ou 0.")

# EXIGÊNCIA DE CÓDIGO 5
# Código principal (main)

# Escolha do serviço
valor_servico = escolha_servico()

# Número de páginas com desconto aplicado
quantidade_de_paginas = num_pagina()

# Serviço adicional escolhido
valor_extra = servico_extra()

# Cálculo do total a pagar
total = (valor_servico * quantidade_de_paginas) + valor_extra

# EXIGÊNCIA DE SAÍDA DE CONSOLE 4
print(f"Total R$: {total:.2f} (serviços: R$ {valor_servico:.2f} * páginas: {quantidade_de_paginas:.0f} + extra: {valor_extra:.2f})")