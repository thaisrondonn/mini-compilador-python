from lexico import lexer
from sintatico import parser

codigo_fonte = "23 + 7"

print("Código fonte:", codigo_fonte)

tokens = lexer(codigo_fonte)
print("Tokens:", tokens)

resultado = parser(tokens)
print("Parser:", resultado)
