from lexico import lexer

def parser(tokens):
    if len(tokens) != 3:
        return "Erro sintático: expressão deve ter NUM + NUM"

    if tokens[0][0] != "NUM":
        return "Erro sintático: expressão deve começar com número"

    if tokens[1][0] != "PLUS":
        return "Erro sintático: operador inválido (esperado '+')"

    if tokens[2][0] != "NUM":
        return "Erro sintático: expressão deve terminar com número"

    return "Expressão sintaticamente válida!"


if __name__ == "__main__":
    texto = input("Digite a expressão: ")
    tokens = lexer(texto)
    print("Tokens:", tokens)

    resultado = parser(tokens)
    print("Resultado do parser:", resultado)
