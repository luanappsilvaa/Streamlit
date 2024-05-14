import streamlit as st
import random

def jogar_adedonha():
    categorias = {
        'A': 'Nome próprio',
        'B': 'País',
        'C': 'Fruta',
        'D': 'Animal',
        'E': 'Cor',
        # Adicione mais categorias conforme desejado
    }

    jogador = st.text_input("Digite o nome do jogador: ")
    rodadas = int(st.text_input("Quantas rodadas você deseja jogar? "))

    pontos_jogador = 0

    for _ in range(rodadas):
        letra = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        print("\nLetra sorteada:", letra)

        for categoria_letra, categoria_descricao in categorias.items():
            resposta = input(f"Digite uma {categoria_descricao} que comece com a letra {letra}: ").capitalize()

            if resposta.startswith(letra):
                pontos_jogador += 1
                print("Resposta válida! +1 ponto!")
            else:
                print("Resposta inválida! 0 pontos.")

    print(f"\nO jogador {jogador} fez {pontos_jogador} pontos em {rodadas} rodadas.")

if __name__ == "__main__":
    print("Bem-vindo ao Jogo da Adedonha!")
    jogar_adedonha()
