"""Calculadora simples com as quatro operações básicas (+, -, * e /).

Uso pela linha de comando (aspas protegem o * e o / do shell):

    python calculadora.py 6 + 3
    python calculadora.py 6 "*" 3
"""

from __future__ import annotations

import argparse
from typing import Callable, Sequence

Numero = int | float


def somar(a: Numero, b: Numero) -> Numero:
    """Retorna a soma de a e b."""
    return a + b


def subtrair(a: Numero, b: Numero) -> Numero:
    """Retorna a diferença entre a e b."""
    return a - b


def multiplicar(a: Numero, b: Numero) -> Numero:
    """Retorna o produto de a e b."""
    return a * b


def dividir(a: Numero, b: Numero) -> Numero:
    """Retorna a divisão de a por b.

    Levanta ZeroDivisionError se b for zero.
    """
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b


OPERACOES: dict[str, Callable[[Numero, Numero], Numero]] = {
    "+": somar,
    "-": subtrair,
    "*": multiplicar,
    "/": dividir,
}


def calcular(a: Numero, operador: str, b: Numero) -> Numero:
    """Aplica o operador ('+', '-', '*' ou '/') sobre a e b.

    Levanta ValueError se o operador não for suportado.
    """
    try:
        operacao = OPERACOES[operador]
    except KeyError:
        raise ValueError(f"Operador inválido: {operador!r}.") from None
    return operacao(a, b)


def main(argv: Sequence[str] | None = None) -> int:
    """Ponto de entrada da linha de comando. Retorna o código de saída."""
    parser = argparse.ArgumentParser(description="Calculadora simples.")
    parser.add_argument("a", type=float, help="primeiro número")
    parser.add_argument("operador", choices=OPERACOES, help="+, -, * ou /")
    parser.add_argument("b", type=float, help="segundo número")
    args = parser.parse_args(argv)

    try:
        resultado = calcular(args.a, args.operador, args.b)
    except ZeroDivisionError as erro:
        print(f"Erro: {erro}")
        return 1

    print(f"{args.a:g} {args.operador} {args.b:g} = {resultado:g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
