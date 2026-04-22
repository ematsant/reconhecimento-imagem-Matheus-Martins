def calcular_estatisticas(numeros):
    """
    Calcula estatísticas básicas de uma lista de números.
    
    Args:
        numeros (list): Lista de números para análise
        
    Returns:
        tuple: Tupla contendo (soma, média, máximo, mínimo)
    """
    soma = sum(numeros)
    media = soma / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    
    return soma, media, maximo, minimo


def exibir_resultado(soma, media, maximo, minimo):
    """
    Exibe os resultados das estatísticas de forma formatada.
    
    Args:
        soma (float): Soma dos valores
        media (float): Média dos valores
        maximo (float): Valor máximo
        minimo (float): Valor mínimo
    """
    print(f"Total: {soma}")
    print(f"Média: {media}")
    print(f"Maior: {maximo}")
    print(f"Menor: {minimo}")


def main():
    """Função principal que executa o programa."""
    numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    soma, media, maximo, minimo = calcular_estatisticas(numeros)
    exibir_resultado(soma, media, maximo, minimo)


if __name__ == "__main__":
    main()