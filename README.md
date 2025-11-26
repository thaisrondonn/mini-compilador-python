# Mini Compilador em Python  
Este repositório contém um mini compilador simples desenvolvido em Python, utilizando os conceitos apresentados no artigo **"Compiladores e sua Relação com Linguagens Formais"**.

O compilador possui duas etapas principais:

- **Analisador Léxico (Lexer)** → responsável por transformar o texto em tokens.  
- **Analisador Sintático (Parser)** → confere se a expressão segue a forma:  


Também está incluso o artigo original em PDF.

---

## ▶️ Como executar

Abra o terminal dentro da pasta `codigo/` e execute:

```bash
python minicomilador.py


Código fonte: 23 + 7
Tokens: [('NUM', '23'), ('PLUS', '+'), ('NUM', '7')]
Parser: Expressão sintaticamente válida!



---

# ✅ **📂 2. PASTA `codigo/`**

Crie uma pasta chamada:




E dentro dela crie os três arquivos seguintes:

---

## 📌 **codigo/lexico.py**

```python
import re

# Definição dos padrões (linguagens regulares)
TOKEN_REGEX = [
    ("NUM", r"\d+"),
    ("PLUS", r"\+"),
    ("SPACE", r"[ \t]+"),  # ignorar espaços
]

def lexer(texto):
    tokens = []
    i = 0
    while i < len(texto):
        match = None
        for token_type, pattern in TOKEN_REGEX:
            regex = re.compile(pattern)
            match = regex.match(texto, i)
            if match:
                lexema = match.group(0)
                if token_type != "SPACE":
                    tokens.append((token_type, lexema))
                i = match.end(0)
                break
        if not match:
            raise ValueError(f"Símbolo inválido na posição {i}: {texto[i]}")
    return tokens


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


from lexico import lexer
from sintatico import parser

codigo_fonte = "23 + 7"

print("Código fonte:", codigo_fonte)

tokens = lexer(codigo_fonte)
print("Tokens:", tokens)

resultado = parser(tokens)
print("Parser:", resultado)
