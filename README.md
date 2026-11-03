# Calculadora com GitHub Actions

![Testes](../../actions/workflows/tests.yml/badge.svg)

Calculadora simples em Python (`+`, `-`, `*` e `/`) usada para explorar o
GitHub Actions: os testes rodam a cada commit em **Ubuntu, macOS e Windows**
e em **Python 3.11, 3.12 e 3.13**.

## Uso

```bash
python calculadora.py 6 + 3
python calculadora.py 6 "*" 3   # aspas evitam que o shell expanda o *
python calculadora.py 1 / 0     # Erro: Não é possível dividir por zero.
```

## Testes

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -v
```
