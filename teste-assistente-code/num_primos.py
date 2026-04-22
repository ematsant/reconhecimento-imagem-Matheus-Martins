"""
Módulo para verificação de números primos.

Este módulo implementa algoritmos eficientes para determinar se um número
é primo, seguindo os princípios de Clean Code.
"""

import math
from typing import List


class PrimeChecker:
    """
    Classe responsável por verificar se números são primos.

    Implementa algoritmos otimizados com complexidade O(√n).
    """

    # Constantes para melhorar legibilidade
    MINIMUM_PRIME_CANDIDATE = 2
    FIRST_ODD_PRIME = 3

    @staticmethod
    def validate_input(number: int) -> None:
        """
        Valida a entrada do usuário.

        Args:
            number (int): Número a ser validado

        Raises:
            TypeError: Se o número não for inteiro
            ValueError: Se o número for negativo
        """
        if not isinstance(number, int):
            raise TypeError("O número deve ser um inteiro")
        if number < 0:
            raise ValueError("O número deve ser não-negativo")

    @staticmethod
    def is_even(number: int) -> bool:
        """
        Verifica se um número é par.

        Args:
            number (int): Número a ser verificado

        Returns:
            bool: True se o número for par
        """
        return number % 2 == 0

    @staticmethod
    def has_divisor_in_range(number: int, start: int, end: int, step: int = 1) -> bool:
        """
        Verifica se o número tem divisores no intervalo especificado.

        Args:
            number (int): Número a ser verificado
            start (int): Início do intervalo
            end (int): Fim do intervalo (inclusivo)
            step (int): Passo do intervalo

        Returns:
            bool: True se encontrar um divisor
        """
        for divisor in range(start, end + 1, step):
            if number % divisor == 0:
                return True
        return False

    @classmethod
    def is_prime(cls, number: int) -> bool:
        """
        Verifica se um número é primo usando algoritmo otimizado.

        Complexidade: O(√n)
        Otimizações:
        - Eliminação de candidatos pares
        - Verificação apenas até √n
        - Tratamento especial para casos extremos

        Args:
            number (int): Número a ser verificado

        Returns:
            bool: True se o número for primo, False caso contrário

        Raises:
            TypeError: Se o número não for inteiro
            ValueError: Se o número for negativo

        Examples:
            >>> PrimeChecker.is_prime(2)
            True
            >>> PrimeChecker.is_prime(4)
            False
            >>> PrimeChecker.is_prime(17)
            True
        """
        cls.validate_input(number)

        # Casos base otimizados
        if number < cls.MINIMUM_PRIME_CANDIDATE:
            return False

        if number == cls.MINIMUM_PRIME_CANDIDATE:
            return True

        if cls.is_even(number):
            return False

        # Verifica divisores ímpares até a raiz quadrada
        sqrt_limit = int(math.sqrt(number))
        return not cls.has_divisor_in_range(
            number,
            cls.FIRST_ODD_PRIME,
            sqrt_limit,
            step=2  # Pula números pares
        )


class PrimeTester:
    """
    Classe responsável por executar testes da funcionalidade de verificação de primos.
    """

    # Conjuntos de teste bem definidos
    PRIME_NUMBERS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    COMPOSITE_NUMBERS = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21]

    @staticmethod
    def run_basic_tests() -> None:
        """
        Executa testes básicos de funcionalidade.
        """
        print("🧪 Executando testes básicos de números primos...")
        print()

        # Testa números primos
        print("✅ Testando números primos:")
        for prime in PrimeTester.PRIME_NUMBERS:
            result = PrimeChecker.is_prime(prime)
            status = "✅" if result else "❌"
            print(f"  {status} {prime} é primo? {result}")

        print()

        # Testa números compostos
        print("❌ Testando números compostos:")
        for composite in PrimeTester.COMPOSITE_NUMBERS:
            result = PrimeChecker.is_prime(composite)
            status = "❌" if not result else "✅"
            print(f"  {status} {composite} é primo? {result}")

        print()

    @staticmethod
    def run_edge_case_tests() -> None:
        """
        Executa testes de casos extremos.
        """
        print("🔍 Testando casos extremos...")

        test_cases = [
            (-1, "número negativo"),
            (0, "zero"),
            (1, "um"),
            (2, "dois (único primo par)"),
            (3, "três (menor primo ímpar)"),
            (1000003, "número maior (primo)"),
        ]

        for number, description in test_cases:
            try:
                result = PrimeChecker.is_prime(number)
                print(f"  ✅ {number} ({description}): {result}")
            except (TypeError, ValueError) as e:
                print(f"  ⚠️  {number} ({description}): Erro - {e}")

        print()

    @staticmethod
    def run_performance_test(limit: int = 10000) -> None:
        """
        Executa teste de performance verificando primos até um limite.

        Args:
            limit (int): Limite superior para teste
        """
        print(f"⚡ Testando performance até {limit}...")

        import time
        start_time = time.time()

        prime_count = sum(1 for i in range(2, limit + 1) if PrimeChecker.is_prime(i))

        end_time = time.time()
        elapsed = end_time - start_time

        print(f"  📊 Encontrados {prime_count} primos até {limit}")
        print(f"  ⏱️  Tempo: {elapsed:.4f}s")
        print()

    @staticmethod
    def run_error_handling_tests() -> None:
        """
        Testa o tratamento de erros.
        """
        print("🚨 Testando tratamento de erros...")

        error_cases = [
            (3.14, "número float"),
            ("17", "string"),
            (None, "None"),
            ([17], "lista"),
        ]

        for invalid_input, description in error_cases:
            try:
                PrimeChecker.is_prime(invalid_input)
                print(f"  ❌ {description}: Deveria ter falhado!")
            except (TypeError, ValueError) as e:
                print(f"  ✅ {description}: Corretamente rejeitado - {type(e).__name__}")

        print()


def main() -> None:
    """
    Função principal que executa todos os testes.
    """
    print("🔢 Verificador de Números Primos - Suite de Testes")
    print("=" * 50)
    print()

    PrimeTester.run_basic_tests()
    PrimeTester.run_edge_case_tests()
    PrimeTester.run_performance_test()
    PrimeTester.run_error_handling_tests()

    print("🎉 Todos os testes foram executados!")
    print()
    print("💡 Dicas de uso:")
    print("  from num_primos import PrimeChecker")
    print("  print(PrimeChecker.is_prime(17))  # True")


# Função de compatibilidade para uso legado
def eh_primo(n: int) -> bool:
    """
    Função legada para compatibilidade.

    Args:
        n (int): Número a ser verificado

    Returns:
        bool: True se for primo
    """
    return PrimeChecker.is_prime(n)


if __name__ == "__main__":
    main()