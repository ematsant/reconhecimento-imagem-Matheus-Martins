# Explicação do Código - Análise Estatística de Lista

## Visão Geral
O código implementa uma função que calcula estatísticas básicas de uma lista de números (soma, média, máximo e mínimo).

## Análise Detalhada

### Função `c(l)`
```python
def c(l):
```
Define uma função chamada `c` que recebe como parâmetro uma lista `l`.

### Cálculo da Soma
```python
    t=0
    for i in range(len(l)):
        t=t+l[i]
    m=t/len(l)
```
- `t=0`: Inicializa a variável `t` (total) com 0
- Loop percorre cada elemento da lista pelo índice
- `t=t+l[i]`: Soma cada elemento à variável `t`
- `m=t/len(l)`: Calcula a média dividindo a soma pela quantidade de elementos

### Encontrando Máximo e Mínimo
```python
    mx=l[0]
    mn=l[0]
    for i in range(len(l)):
        if l[i]>mx:
            mx=l[i]
        if l[i]<mn:
            mn=l[i]
```
- `mx` e `mn` são inicializados com o primeiro elemento da lista
- Loop compara cada elemento com os valores atuais de máximo e mínimo
- Se encontra um valor maior que `mx`, atualiza `mx`
- Se encontra um valor menor que `mn`, atualiza `mn`

### Retorno
```python
    return t,m,mx,mn
```
Retorna uma tupla contendo:
- `t`: soma total
- `m`: média
- `mx`: valor máximo
- `mn`: valor mínimo

## Execução do Programa
```python
x=[23,7,45,2,67,12,89,34,56,11]
a,b,c2,d=c(x)
```
- Cria uma lista `x` com 10 números
- Chama a função `c(x)` e desempacota os resultados nas variáveis `a`, `b`, `c2` e `d`

### Saída
```
total: 346
media: 34.6
maior: 89
menor: 2
```

## Resumo
O código calcula e exibe quatro estatísticas de uma lista:
- **Total**: Soma de todos os números (346)
- **Média**: Valor médio dos números (34.6)
- **Maior**: Valor máximo encontrado (89)
- **Menor**: Valor mínimo encontrado (2)
