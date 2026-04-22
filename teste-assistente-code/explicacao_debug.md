# Análise de Erros - debug.py

## Erros Identificados

### 1. ❌ Erro de Sintaxe - Aspas Faltantes (Linha 5)
**Código com erro:**
```python
item1 = float(input(Preço do item 1? ))
```

**Problema:** A string `"Preço do item 1?"` não está entre aspas.

**Correção:**
```python
item1 = float(input("Preço do item 1? "))
```

---

### 2. ❌ Erro de Formatação - F-string Faltando (Linha 21)
**Código com erro:**
```python
print(" Item 2:        R$ {total_item2:.2f}")
```

**Problema:** Falta o prefixo `f` antes da string para que a interpolação de variáveis funcione. Sem o `f`, a string é interpretada literalmente.

**Correção:**
```python
print(f" Item 2:        R$ {total_item2:.2f}")
```

---

### 3. ❌ Erro de Tipo - String vs Número (Linha 30)
**Código com erro:**
```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
if desconto_cupom > 0:
```

**Problema:** A função `input()` retorna uma string, não um número. Não é possível comparar uma string diretamente com um inteiro usando `>`.

**Correção:**
```python
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
if desconto_cupom > 0:
```

---

### 4. ❌ Erro de Indentação (Linha 31)
**Código com erro:**
```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

**Problema:** O `print()` não está indentado corretamente. Em Python, o bloco dentro do `if` deve estar indentado.

**Correção:**
```python
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

---

## Resumo dos Erros

| Linha | Tipo de Erro | Severidade |
|-------|-------------|-----------|
| 5 | Sintaxe - Aspas faltantes | 🔴 Crítico |
| 21 | Formatação - F-string faltando | 🔴 Crítico |
| 30-31 | Tipo de dados + Indentação | 🔴 Crítico |

Todos os erros **impedem a execução** do programa.
