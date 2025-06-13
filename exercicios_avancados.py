"""
Exercícios Avançados de Programação em Python
Este arquivo contém uma coleção de exercícios avançados de programação,
incluindo algoritmos, estruturas de dados e problemas práticos.
"""

# 22. Detectar Ciclo em Grafo
def tem_ciclo(grafo):
    """
    Detecta se há ciclos em um grafo direcionado representado por um dicionário.
    """
    visitado = set()
    em_recursao = set()

    def visitar(no):
        if no in em_recursao:
            return True
        if no in visitado:
            return False
        visitado.add(no)
        em_recursao.add(no)
        for vizinho in grafo.get(no, []):
            if visitar(vizinho):
                return True
        em_recursao.remove(no)
        return False

    return any(visitar(no) for no in grafo)

# Exemplo de uso:
grafo = {'A': ['B'], 'B': ['C'], 'C': ['A']}
print("22. Detectar Ciclo em Grafo:")
print(f"Grafo {grafo} tem ciclo: {tem_ciclo(grafo)}")

# 23. Busca Binária Recursiva
def busca_binaria(lista, alvo, inicio, fim):
    """
    Realiza busca binária recursiva em uma lista ordenada de inteiros.
    """
    if inicio > fim:
        return -1
    meio = (inicio + fim) // 2
    if lista[meio] == alvo:
        return meio
    elif lista[meio] > alvo:
        return busca_binaria(lista, alvo, inicio, meio - 1)
    else:
        return busca_binaria(lista, alvo, meio + 1, fim)

# Exemplo de uso:
lista = [1, 3, 5, 7, 9, 11, 13, 15]
print("\n23. Busca Binária Recursiva:")
print(f"Posição do número 7 na lista {lista}: {busca_binaria(lista, 7, 0, len(lista)-1)}")

# 24. Conversor Infixa para Pós-fixa
def prioridade(op):
    return {'+': 1, '-': 1, '*': 2, '/': 2}.get(op, 0)

def infixa_para_posfixa(expr):
    """
    Converte uma expressão matemática infixa para a notação pós-fixa (RPN).
    """
    resultado = []
    pilha = []
    for c in expr:
        if c.isalnum():
            resultado.append(c)
        elif c in "+-*/":
            while pilha and prioridade(c) <= prioridade(pilha[-1]):
                resultado.append(pilha.pop())
            pilha.append(c)
        elif c == '(':
            pilha.append(c)
        elif c == ')':
            while pilha and pilha[-1] != '(':
                resultado.append(pilha.pop())
            pilha.pop()
    while pilha:
        resultado.append(pilha.pop())
    return ''.join(resultado)

# Exemplo de uso:
print("\n24. Conversor Infixa para Pós-fixa:")
print(f"Expressão 'a+b*(c-d)' em pós-fixa: {infixa_para_posfixa('a+b*(c-d)')}")

# 25. Balanceador de Parênteses
def balanceado(expressao):
    """
    Verifica se os parênteses de uma expressão estão balanceados corretamente.
    """
    pilha = []
    for c in expressao:
        if c == '(':
            pilha.append(c)
        elif c == ')':
            if not pilha:
                return False
            pilha.pop()
    return len(pilha) == 0

# Exemplo de uso:
print("\n25. Balanceador de Parênteses:")
print(f"'(1+(2*3))' está balanceado: {balanceado('(1+(2*3))')}")
print(f"'(1+2*(3)' está balanceado: {balanceado('(1+2*(3)')}")

# 26. Validador de Sudoku
def valido(grupo):
    return sorted(grupo) == list(range(1, 10))

def validar_sudoku(tabuleiro):
    """
    Verifica se uma grade 9x9 de Sudoku está corretamente preenchida.
    """
    for linha in tabuleiro:
        if not valido(linha):
            return False
    for col in zip(*tabuleiro):
        if not valido(col):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            bloco = [tabuleiro[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not valido(bloco):
                return False
    return True

# Exemplo de uso:
sudoku = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]
print("\n26. Validador de Sudoku:")
print(f"Tabuleiro de Sudoku é válido: {validar_sudoku(sudoku)}")

# 27. Sistema de Login com Tentativas
def sistema_login():
    """
    Sistema de login simples com no máximo 3 tentativas para acertar a senha.
    """
    senha_correta = "1234"
    tentativas = 3

    while tentativas > 0:
        entrada = input("Digite a senha: ")
        if entrada == senha_correta:
            print("Acesso permitido")
            break
        else:
            tentativas -= 1
            print(f"Tentativas restantes: {tentativas}")
    else:
        print("Acesso bloqueado")

# 28. Agrupador de Pares e Ímpares
def agrupar_pares_impares(lista):
    """
    Recebe uma lista de inteiros e separa os pares dos ímpares.
    """
    pares = [n for n in lista if n % 2 == 0]
    impares = [n for n in lista if n % 2 != 0]
    return pares, impares

# Exemplo de uso:
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = agrupar_pares_impares(lista)
print("\n28. Agrupador de Pares e Ímpares:")
print(f"Lista original: {lista}")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")

# 29. Contador de Palavras
from collections import Counter

def contar_palavras(texto):
    """
    Conta quantas vezes cada palavra aparece em um texto.
    """
    palavras = texto.split()
    return Counter(palavras)

# Exemplo de uso:
texto = "o sol brilha e o sol aquece a terra"
print("\n29. Contador de Palavras:")
print(f"Texto: {texto}")
print(f"Contagem: {contar_palavras(texto)}")

# 30. Validador de Palíndromos
import re

def eh_palindromo(frase):
    """
    Verifica se uma frase é um palíndromo, desconsiderando espaços e pontuação.
    """
    frase = re.sub(r'[^a-zA-Z0-9]', '', frase).lower()
    return frase == frase[::-1]

# Exemplo de uso:
print("\n30. Validador de Palíndromos:")
print(f"'A base do teto desaba' é palíndromo: {eh_palindromo('A base do teto desaba')}")

# 31. Validador de CPF
def validar_cpf(cpf):
    """
    Valida se um número de CPF é válido com base nos dígitos verificadores.
    """
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    for j in [9, 10]:
        soma = sum(int(cpf[i]) * ((j + 1) - i) for i in range(j))
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        if digito != int(cpf[j]):
            return False
    return True

# Exemplo de uso:
print("\n31. Validador de CPF:")
print(f"CPF '12345678909' é válido: {validar_cpf('12345678909')}")

# Função principal para testar todos os exercícios
def main():
    print("Testando todos os exercícios...")
    # Aqui você pode adicionar chamadas para testar cada exercício
    pass

if __name__ == "__main__":
    main() 