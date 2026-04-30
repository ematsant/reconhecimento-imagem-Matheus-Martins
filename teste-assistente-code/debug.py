#                                      CÓDIGO COM ERROS                           
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

# Nota: Estrutura com 3 itens fixos. Para escalar, considere usar listas/loops
qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
# Imposto fixo em 10% - valor configurável que poderia ser parametrizado
imposto = subtotal * 0.10

# DESCONTO
# Cupom aplicado como percentual - se 0, nenhum desconto é concedido
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
# Desconto calculado sobre o subtotal (antes do imposto)
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
# Ordem das operações: subtotal + imposto - desconto
# O imposto é aplicado ao subtotal completo, e o desconto reduz o total final
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

# Exibe desconto apenas se o cupom for válido (maior que 0)
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
# round(total, 2) garante que possíveis erros de ponto flutuante sejam corrigidos
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)