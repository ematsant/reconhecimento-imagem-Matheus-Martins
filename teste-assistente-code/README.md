# Teste Assistente Code - Exemplos Python

Coleção de exemplos práticos de Python focados em **debugging**, **Clean Code** e **refatoração**, com análises detalhadas para aprendizado.

## 📋 Estrutura

```
teste-assistente-code/
├── README.md                    # Este arquivo
├── debug.py                     # Código com erros (exercício)
├── explicacao_debug.md          # Análise de erros em debug.py
├── num_primos.py               # Verificador de primos (Clean Code)
├── explicacao_num_primo.md     # Análise técnica de números primos
├── refatoracao.py              # Análise estatística (código refatorado)
└── explicacao-refatoracao.md   # Explicação de refatoração
```

---

## 🐛 1. Debug e Tratamento de Erros

### debug.py

**Objetivo**: Exercício prático de identificação e correção de erros.

Um programa que simula um **sistema de faturamento** com múltiplos itens, cálculo de impostos e descontos.

**Funcionalidades**:
- Entrada de dados do cliente
- Cálculo de preço para 3 itens diferentes
- Aplicação de imposto (10%)
- Aplicação de desconto via cupom
- Exibição formatada do recibo

**Exemplo de Uso**:
```
Cliente: João Silva
Item 1: R$ 50.00
Item 2: R$ 30.00
Item 3: R$ 20.00
Subtotal: R$ 100.00
Imposto: R$ 10.00
Total: R$ 110.00
```

### ❌ Erros a Encontrar

Ver [explicacao_debug.md](explicacao_debug.md) para análise completa.

**Resumo dos Erros**:

| Erro | Linha | Tipo | Severidade |
|------|-------|------|-----------|
| Aspas faltantes em string | 5 | Sintaxe | 🔴 Crítico |
| F-string não inicializada | 21 | Formatação | 🔴 Crítico |
| Comparação string vs número | 30 | Tipo de Dados | 🔴 Crítico |
| Indentação incorreta | 31 | Sintaxe | 🔴 Crítico |

### ✅ Como Usar

1. Abra `debug.py` em um editor Python
2. Execute para ver os erros
3. Identifique cada um seguindo `explicacao_debug.md`
4. Corrija os erros
5. Teste novamente

---

## 🔢 2. Números Primos (Clean Code)

### num_primos.py

**Objetivo**: Demonstrar **Clean Code principles** e otimização de algoritmos.

Implementação profissional de um verificador de números primos com:
- Validação robusta de entrada
- Algoritmo otimizado (complexidade O(√n))
- Type hints e type checking
- Docstrings descritivas
- Suite de testes

### Arquitetura

**Classe Principal: `PrimeChecker`**

```python
class PrimeChecker:
    """Verificador de números primos com algoritmo otimizado."""
    
    MINIMUM_PRIME_CANDIDATE = 2
    FIRST_ODD_PRIME = 3
    
    @staticmethod
    def validate_input(number: int) -> None
        """Valida se a entrada é um inteiro não-negativo."""
    
    @staticmethod
    def is_even(number: int) -> bool
        """Verifica se um número é par."""
    
    @staticmethod
    def has_divisor_in_range(number, start, end, step=1) -> bool
        """Verifica se há divisores no intervalo."""
    
    @classmethod
    def is_prime(cls, number: int) -> bool
        """Verifica se um número é primo (O(√n))."""
```

**Classe de Testes: `PrimeTester`**

```python
class PrimeTester:
    """Suite de testes para PrimeChecker."""
    
    def run_basic_tests()
    def run_edge_case_tests()
    def run_performance_test()
    def run_error_handling_tests()
```

### Princípios de Clean Code

✅ **Nomes Significativos**
- `n` → `number`
- `eh_primo` → `is_prime`
- Constantes explícitas

✅ **Funções Pequenas e Focadas**
- `validate_input()`: apenas valida
- `is_even()`: apenas verifica paridade
- `has_divisor_in_range()`: abstrai loop

✅ **Type Hints**
```python
def is_prime(cls, number: int) -> bool:
```

✅ **Documentação**
- Docstrings para cada função
- Explicação de complexidade
- Exemplos de uso

✅ **Tratamento de Erros**
```python
if not isinstance(number, int):
    raise TypeError("O número deve ser um inteiro")
if number < 0:
    raise ValueError("O número deve ser não-negativo")
```

### Complexidade de Tempo

- **Algoritmo Ingênuo**: O(n) - muito lento
- **Implementação**: O(√n) - até **100x mais rápido**

Exemplo: Para verificar se 1.000.000 é primo:
- Ingênuo: ~1.000.000 iterações
- Otimizado: ~1.000 iterações

### ✅ Como Usar

```bash
python num_primos.py
```

**Saída Esperada**:
```
=== TESTES BÁSICOS ===
✓ 2 é primo
✓ 3 é primo
✓ 4 não é primo
✓ 11 é primo
✓ 100 não é primo

=== TESTES DE CASOS EXTREMOS ===
✓ 0 não é primo
✓ 1 não é primo
✓ Número negativo levanta ValueError

=== TESTE DE PERFORMANCE ===
Números primos até 1000: 168
Tempo: 0.XXs

=== TRATAMENTO DE ERROS ===
✓ String levanta TypeError
✓ Float levanta TypeError
```

### 📖 Análise Técnica Detalhada

Ver [explicacao_num_primo.md](explicacao_num_primo.md)

---

## 📈 3. Análise Estatística (Refatoração)

### refatoracao.py

**Objetivo**: Demonstrar boas práticas de estruturação e refatoração de código.

Programa que calcula **estatísticas básicas** de uma lista de números.

### Funções

**1. `calcular_estatisticas(numeros)`**
```python
def calcular_estatisticas(numeros):
    """
    Calcula estatísticas básicas de uma lista de números.
    
    Args:
        numeros (list): Lista de números para análise
        
    Returns:
        tuple: (soma, média, máximo, mínimo)
    """
```

**Cálculos**:
- `soma`: Soma de todos os valores
- `media`: Média aritmética
- `maximo`: Maior valor
- `minimo`: Menor valor

**Usa**: Built-in functions Python (`sum()`, `max()`, `min()`)

**2. `exibir_resultado(soma, media, maximo, minimo)`**
```python
def exibir_resultado(soma, media, maximo, minimo):
    """Exibe os resultados de forma formatada."""
```

Separação de responsabilidades:
- Cálculos em uma função
- Exibição em outra

**3. `main()`**
```python
def main():
    """Função principal que executa o programa."""
```

Ponto de entrada que orquestra:
1. Entrada de dados
2. Cálculos
3. Exibição

### ✅ Como Usar

```bash
python refatoracao.py
```

**Saída Esperada**:
```
Total: 356
Média: 35.6
Maior: 89
Menor: 2
```

### Boas Práticas Implementadas

✅ **Separação de Responsabilidades**
- Cada função faz uma coisa bem

✅ **Docstrings**
- Documentação clara de cada função

✅ **Type Hints (Implícitos)**
- Nomes claros indicam tipos esperados

✅ **Reutilização de Built-ins**
- Usar `sum()`, `max()`, `min()` ao invés de loops

✅ **Ponto de Entrada Explícito**
```python
if __name__ == "__main__":
    main()
```

### 📖 Análise Detalhada

Ver [explicacao-refatoracao.md](explicacao-refatoracao.md)

---

## 🎯 Fluxo de Aprendizado

### 1️⃣ Começar pelo Debug
- Execute `debug.py` e veja os erros
- Leia `explicacao_debug.md`
- Identifique e corrija cada erro
- Teste novamente

### 2️⃣ Estudar Clean Code
- Analise a estrutura de `num_primos.py`
- Leia `explicacao_num_primo.md`
- Entenda os princípios aplicados
- Compare com código não otimizado

### 3️⃣ Entender Refatoração
- Execute `refatoracao.py`
- Leia `explicacao-refatoracao.md`
- Veja como código pode ser melhorado
- Compare versão original vs refatorada

---

## 🛠️ Requisitos

- **Python**: 3.7 ou superior
- **Bibliotecas**: Apenas standard library
  - `math` (números primos)
  - `typing` (type hints)

### Instalação

```bash
# Não requer instalação de dependências!
python num_primos.py
python refatoracao.py
```

---

## 📚 Conceitos-Chave

### Clean Code
- Nomes significativos
- Funções pequenas e focadas
- Type hints
- Docstrings
- Tratamento robusto de erros

### Otimização
- Complexidade de tempo O(√n)
- Redução de iterações
- Uso de built-in functions

### Refatoração
- Extrair funções
- Separação de responsabilidades
- Melhorar legibilidade
- Facilitar testes

### Debugging
- Identificar erros de sintaxe
- Erros de tipo de dados
- Erros de indentação
- Testes e validação

---

## 📖 Recursos Internos

- [debug.py](debug.py) - Código com erros
- [explicacao_debug.md](explicacao_debug.md) - Análise de erros
- [num_primos.py](num_primos.py) - Implementação Clean Code
- [explicacao_num_primo.md](explicacao_num_primo.md) - Análise técnica
- [refatoracao.py](refatoracao.py) - Código refatorado
- [explicacao-refatoracao.md](explicacao-refatoracao.md) - Explicação de refatoração

---

## 🎓 Objetivos de Aprendizado

Após trabalhar com esses exemplos, você será capaz de:

✅ Identificar e corrigir erros comuns em Python  
✅ Escrever código seguindo Clean Code principles  
✅ Otimizar algoritmos para melhor performance  
✅ Aplicar type hints para melhor qualidade de código  
✅ Estruturar programas em funções bem definidas  
✅ Documentar código de forma profissional  
✅ Refatorar código existente  
✅ Testar e validar suas implementações  

---

## 💡 Dicas de Estudo

1. **Execute primeiro** - Veja o código rodar
2. **Leia as explicações** - Entenda o "porquê"
3. **Modifique o código** - Experimente mudanças
4. **Crie testes** - Valide suas alterações
5. **Refatore** - Melhore o que aprendeu

---

**Desenvolvido para aprendizado de Python, Clean Code e Engenharia de Software** ❤️
