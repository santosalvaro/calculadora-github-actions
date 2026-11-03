"""Testes de unidade da calculadora."""

import pytest

from calculadora import (
    calcular,
    dividir,
    main,
    multiplicar,
    somar,
    subtrair,
)


@pytest.mark.parametrize(
    "a, b, esperado",
    [(2, 3, 5), (-1, 1, 0), (0.5, 0.25, 0.75), (0, 0, 0)],
)
def test_somar(a, b, esperado):
    assert somar(a, b) == esperado


@pytest.mark.parametrize(
    "a, b, esperado",
    [(5, 3, 2), (3, 5, -2), (1.5, 0.5, 1.0), (0, 0, 0)],
)
def test_subtrair(a, b, esperado):
    assert subtrair(a, b) == esperado


@pytest.mark.parametrize(
    "a, b, esperado",
    [(4, 3, 12), (-2, 3, -6), (5, 0, 0), (0.5, 4, 2.0)],
)
def test_multiplicar(a, b, esperado):
    assert multiplicar(a, b) == esperado


@pytest.mark.parametrize(
    "a, b, esperado",
    [(6, 3, 2), (7, 2, 3.5), (-8, 2, -4), (0, 5, 0)],
)
def test_dividir(a, b, esperado):
    assert dividir(a, b) == esperado


def test_dividir_por_zero_levanta_erro():
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)


@pytest.mark.parametrize(
    "a, operador, b, esperado",
    [(2, "+", 3, 5), (2, "-", 3, -1), (2, "*", 3, 6), (6, "/", 3, 2)],
)
def test_calcular_com_cada_operador(a, operador, b, esperado):
    assert calcular(a, operador, b) == esperado


def test_calcular_com_operador_invalido():
    with pytest.raises(ValueError):
        calcular(1, "%", 2)


def test_main_exibe_resultado(capsys):
    assert main(["6", "*", "3"]) == 0
    assert capsys.readouterr().out.strip() == "6 * 3 = 18"


def test_main_divisao_por_zero_retorna_erro(capsys):
    assert main(["1", "/", "0"]) == 1
    assert "dividir por zero" in capsys.readouterr().out
