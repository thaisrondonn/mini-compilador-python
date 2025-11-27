
import re

TOKEN_REGEX = [
    ("NUM", r"\d+"),
    ("PLUS", r"\+"),
    ("SPACE", r"[ \t]+"),     # ignorado
]

COMPILED = [(name, re.compile(pattern)) for name, pattern in TOKEN_REGEX]

def lexer(texto: str):
    tokens = []
    i = 0
    n = len(texto)

    while i < n:
        match = None
        for token_type, regex in COMPILED:
            m = regex.match(texto, i)
            if m:
                lexema = m.group(0)
                if token_type != "SPACE":
                    tokens.append((token_type, lexema))
                i = m.end()
                match = True
                break
        if not match:
            raise ValueError(f"Token inválido em '{texto[i:]}' no índice {i}")

    return tokens

if __name__ == "__main__":
    print(lexer(input("Digite expressão: ")))
    return tokens


if __name__ == "__main__":
    print(lexer("12+34 + 5"))
