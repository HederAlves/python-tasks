# 📘 Exercícios Python – App de Vendas e Gerenciamento

Este repositório contém quatro exercícios práticos desenvolvidos em Python. Cada exercício simula um sistema real com foco em lógica de programação e interação com o usuário.

---

## ✅ Questão 1 – App de Vendas com Desconto por Faixa de Valor

### 💡 Enunciado

Você é responsável por desenvolver parte do sistema de vendas de uma empresa que vende em atacado. O sistema oferece **descontos progressivos conforme o valor total da compra**.

### 🧮 Tabela de Desconto

| Valor Total da Compra     | Desconto |
| ------------------------- | -------- |
| Menor que R$ 2.500        | 0%       |
| De R$ 2.500 a R$ 5.999,99 | 4%       |
| De R$ 6.000 a R$ 9.999,99 | 7%       |
| A partir de R$ 10.000     | 11%      |

### 🎯 Objetivos do Código

- Mensagem de boas-vindas com nome e sobrenome
- Input do valor unitário e quantidade
- Cálculo do valor total sem e com desconto
- Aplicação correta de `if`, `elif` e `else`
- Comentários explicativos no código

### 📤 Exigências de Saída no Console

- Exibir mensagem de boas-vindas com nome
- Exibir um pedido com valor total maior ou igual a R$ 2.500 (com desconto aplicado)

---

## 🍧 Questão 2 – App de Pedidos de Açaí e Cupuaçu

### 💡 Enunciado

Você ficou responsável pela interface de retirada de pedidos em uma loja que vende Açaí e Cupuaçu, com diferentes tamanhos e preços.

### 💰 Tabela de Preços

| Tamanho | Cupuaçu (CP) | Açaí (AC) |
| ------- | ------------ | --------- |
| P       | R$ 9         | R$ 11     |
| M       | R$ 14        | R$ 16     |
| G       | R$ 18        | R$ 20     |

### 🎯 Objetivos do Código

- Mensagem de boas-vindas com nome e sobrenome
- Validação do sabor (CP ou AC), com mensagem de erro
- Validação do tamanho (P, M ou G), com mensagem de erro
- Estrutura condicional aninhada com `if`, `elif`, `else`
- Acumulador para somar valores dos pedidos
- Loop com `while`, uso de `break` e `continue`
- Comentários explicativos

### 📤 Exigências de Saída no Console

- Mensagem de boas-vindas com nome
- Pedido com erro de sabor
- Pedido com erro de tamanho
- Pedido com dois sabores e tamanhos diferentes

---

## 🖨️ Questão 3 – Sistema de Cobrança da Copiadora

### 💡 Enunciado

Você irá programar a interface de atendimento de uma copiadora que realiza digitalização, impressão e encadernação, com diferentes preços e regras de desconto.

### 📄 Serviços e Preços

| Código | Serviço                  | Preço por página |
| ------ | ------------------------ | ---------------- |
| DIG    | Digitalização            | R$ 1,10          |
| ICO    | Impressão Colorida       | R$ 1,00          |
| IPB    | Impressão Preto e Branco | R$ 0,40          |
| FOT    | Fotocópia                | R$ 0,20          |

### 🎁 Encadernações

| Código | Tipo             | Valor Extra |
| ------ | ---------------- | ----------- |
| 0      | Sem encadernação | R$ 0        |
| 1      | Simples          | R$ 15       |
| 2      | Capa Dura        | R$ 40       |

### 🎯 Objetivos do Código

- Mensagem de boas-vindas
- Função `escolha_servico()` com validação de entrada
- Função `num_pagina()` com desconto aplicado e validação com `try/except`
- Função `servico_extra()` com validação
- Cálculo principal no corpo do programa (fora das funções)
- Comentários relevantes no código

### 📤 Exigências de Saída no Console

- Mensagem de boas-vindas com nome
- Erro ao digitar serviço inválido
- Erro ao ultrapassar o limite de páginas (≥ 20000)
- Pedido completo com serviço, número de páginas e extra válidos

---

## 📚 Questão 4 – Sistema de Gerenciamento de Livros

### 💡 Enunciado

Você foi contratado para desenvolver um sistema de cadastro, consulta e remoção de livros para uma pequena empresa. O sistema deve funcionar via menu interativo.

### 📋 Funcionalidades do Menu

1. Cadastrar Livro
2. Consultar Livro
   - Consultar Todos
   - Consultar por ID
   - Consultar por Autor
   - Retornar ao Menu
3. Remover Livro
4. Encerrar Programa

### 🎯 Objetivos do Código

- Mensagem de boas-vindas
- Lista vazia `lista_livro` e variável `id_global = 0`
- Função `cadastrar_livro(id)` com entrada e dicionário
- Função `consultar_livro()` com submenus e validação
- Função `remover_livro()` com verificação de ID
- Menu principal com controle de fluxo
- Lista de dicionários
- Comentários explicativos

### 📤 Exigências de Saída no Console

- Mensagem de boas-vindas com nome
- Cadastro de 3 livros (2 com mesmo autor)
- Consulta geral de todos os livros
- Consulta por ID
- Consulta por autor (com múltiplos livros)
- Remoção de livro seguida de nova consulta

---

## 🛠️ Requisitos Técnicos Gerais

- Python 3.x
- Uso de:
  - `input()` e `print()`
  - Estruturas condicionais: `if`, `elif`, `else`
  - Loops: `while`, `break`, `continue`
  - Funções
  - `try/except` para tratamento de exceções
  - Listas, dicionários, e listas de dicionários
  - Comentários explicativos

---
