# 📘 Mini Compilador em Python  
Um mini compilador educacional desenvolvido em Python, baseado nos conceitos apresentados no artigo  
**“Compiladores e sua Relação com Linguagens Formais e Autômatos”**.

O objetivo deste projeto é demonstrar, de forma simples e prática, como funcionam as duas primeiras etapas de um compilador:

- **🔹 Análise Léxica (Lexer)** — reconhece padrões como números e operadores.  
- **🔹 Análise Sintática (Parser)** — valida se a estrutura segue a gramática definida.

Este mini compilador interpreta expressões no formato:



Exemplo válido: `23 + 7`

---

## 📂 Estrutura do Projeto

mini-compilador-python/
│
├── Artigo/
│ └── Artigo - Compiladores e sua Relação com Linguagens Formais.pdf
│
└── codigo/
├── lexico.py
├── sintatico.py
└── minicomilador.py



---

## ⚙️ Como funciona cada parte

### ✔ **1. Analisador Léxico (Lexer)**
- Lê o código fonte caractere por caractere.
- Usa expressões regulares para identificar:
  - `NUM` → números inteiros  
  - `PLUS` → símbolo `+`  
  - `SPACE` → espaços em branco (ignorados)
- Gera uma lista de tokens, por exemplo:



---

### ✔ **2. Analisador Sintático (Parser)**
Verifica se a sequência de tokens segue a regra:



Se estiver correta → retorna "Expressão sintaticamente válida!"  
Se estiver errada → lança uma mensagem de erro clara.

---

## ▶️ Como executar o mini compilador

1. Abra o terminal na pasta **codigo/**  
2. Execute:

```bash
python minicomilador.py


Código fonte: 23 + 7
Tokens: [('NUM', '23'), ('PLUS', '+'), ('NUM', '7')]
Parser: Expressão sintaticamente válida!


