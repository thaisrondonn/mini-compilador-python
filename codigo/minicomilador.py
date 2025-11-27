# minicompilador.py

from lexico import lexer
from sintatico import parser

def interpretador(tokens):
    """Executa NUM + NUM + NUM ..."""
    resultado = int(tokens[0][1])  # primeiro número

    i = 1
    while i < len(tokens):
        op = tokens[i][1]          # '+'
        num = int(tokens[i+1][1])  # número seguinte

        if op == "+":
            resultado += num

        i += 2

    return resultado

if __name__ == "__main__":
    exp = input("Digite expressão: ")

    try:
        tokens = lexer(exp)
        print("Tokens:", tokens)

        parser(tokens)
        print("Expressão válida!")

        res = interpretador(tokens)
        print("Resultado:", res)

    except Exception as e:
        print("Erro:", e)
