import csv
import random

def carregar_perguntas(nome_arquivo):
    with open(nome_arquivo, newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile, delimiter=';')
        quiz = list(leitor)
    return quiz

def fazer_questionario(quiz):
    pontuacao = 0
    num_perguntas = len(quiz)
    random.shuffle(quiz)
    for idx, (pergunta, *opcoes, resposta) in enumerate(quiz[:10], start=1):
        print(f"{idx}. {pergunta}")
        for i, opcao in enumerate(opcoes):
            print(f"   {chr(65 + i)}. {opcao}")
        resposta_usuario = input("> Escolha uma opcao: ").strip().upper()
        if resposta_usuario == resposta.strip():
            print("> Resposta correta!\n")
            pontuacao += 1
        else:
            print(f"> Resposta incorreta! A resposta correta era {resposta}.\n")
    print(f"> Sua pontuacao final foi {pontuacao}/10.")
    if pontuacao == 10:
        print("> Parabens! Voce acertou todas as questoes!")

def print_divisao():
    print("----------------------------------------------")

def print_bem_vindo():
    print_divisao()
    print("*                                            *") 
    print("*         Bem-vindo ao Questionario!         *")
    print("*                                            *")

def print_menu():
    print_divisao()
    print("> Escolha o tipo de questionario:")
    print("  [1] Prova 1 (Listas, Pilhas, Filas e Deques)")
    print("  [2] Prova 2 (Pesquisa, Ordenacao e Arvores)")
    print("  [0] Sair")
    print("")

if __name__ == "__main__":
    print_bem_vindo()

    while True:
        print_menu()
        escolha = input("> Escolha uma opcao: ")

        if escolha == "1":
            print_divisao()
            print("> Perguntas sobre a Prova 1:\n")
            quiz = carregar_perguntas("questoes_p1.csv")
            fazer_questionario(quiz)
        elif escolha == "2":
            print_divisao()
            print("> Perguntas sobre a Prova 2:\n")
            quiz = carregar_perguntas("questoes_p2.csv")
            fazer_questionario(quiz)
        elif escolha == "0":
            print("> Programa finalizado com sucesso!")
            print_divisao()
            break
        else:
            print("> Opcao invalida!")