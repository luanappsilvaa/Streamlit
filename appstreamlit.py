import streamlit as st
import random

def jogar_adedonha():
    st.title("Jogo da Adedonha")

    categorias = {
        "Nome": ["Alice", "Bruno", "Carla", "Daniel", "Eva"],
        "Animal": ["Cachorro", "Gato", "Elefante", "Pássaro", "Cobra"],
        "Fruta": ["Maçã", "Banana", "Uva", "Abacaxi", "Morango"],
        "Cor": ["Azul", "Vermelho", "Verde", "Amarelo", "Roxo"],
        "Minha sogra é": ["Paciente", "Engraçada", "Trabalhadora", "Carinhosa", "Inteligente"]
    }

    categoria_escolhida = st.selectbox("Escolha uma categoria:", list(categorias.keys()))

    palavra = random.choice(categorias[categoria_escolhida])

    st.write(f"A palavra escolhida é da categoria '{categoria_escolhida}':")
    st.write("_ " * len(palavra))

    tentativas_restantes = 3
    letras_descobertas = ["_"] * len(palavra)

    palpite = st.text_input("Digite uma letra ou a palavra completa:").upper()

    while tentativas_restantes > 0 and "_" in letras_descobertas:
        if len(palpite) == 1:
            if palpite in palavra:
                st.write("Letra correta!")
                for i in range(len(palavra)):
                    if palavra[i] == palpite:
                        letras_descobertas[i] = palpite
            else:
                st.write("Letra incorreta!")
                tentativas_restantes -= 1
        elif palpite == palavra:
            st.write("Parabéns! Você acertou a palavra!")
            break
        else:
            st.write("Palavra incorreta!")
            tentativas_restantes -= 1

    if "_" not in letras_descobertas:
        st.write("Parabéns! Você descobriu a palavra!")
    else:
        st.write("Suas tentativas acabaram. A palavra era:", palavra)

jogar_adedonha()
