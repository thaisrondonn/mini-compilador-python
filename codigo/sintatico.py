# Expressão esperada: NUM PLUS NUM

def parser(tokens):
    if len(tokens) != 3:
        raise ValueError("Expressão inválida.")

    if tokens[0][0] != "NUM":
        raise ValueError("A expressão deve começar com um número.")

    if tokens[1][0] != "PLUS":
        raise ValueError("Falta o operador '+'.")

    if tokens[2][0] != "NUM":
        raise ValueError("A expressão deve terminar com um número.")

    return "Expressão sintaticamente válida!"
