import random

def jogar_adedonha():
    print("Bem-vindo ao jogo da Adedonha!")
    categorias = {
        "Nome": ["Alice", "Bruno", "Carla", "Daniel", "Eva"],
        "Animal": ["Cachorro", "Gato", "Elefante", "Pássaro", "Cobra"],
        "Fruta": ["Maçã", "Banana", "Uva", "Abacaxi", "Morango"],
        "Cor": ["Azul", "Vermelho", "Verde", "Amarelo", "Roxo"],
        "Minha sogra é": ["Paciente", "Engraçada", "Trabalhadora", "Carinhosa", "Inteligente"]
    }
    
    categoria = random.choice(list(categorias.keys()))
    palavra = random.choice(categorias[categoria])
    
    print(f"A categoria escolhida é: {categoria}")
    print("A palavra tem", len(palavra), "letras.")
    
    tentativas = 3
    letras_descobertas = []
    for letra in palavra:
        letras_descobertas.append("_")
    
    while tentativas > 0:
        print("Palavra atual:", " ".join(letras_descobertas))
        palpite = st.text_input("Digite uma letra ou a palavra completa: ").upper()
        
        if len(palpite) == 1:
            if palpite in palavra:
                print("Letra correta!")
                for i in range(len(palavra)):
                    if palavra[i] == palpite:
                        letras_descobertas[i] = palpite
            else:
                print("Letra incorreta!")
                tentativas -= 1
        elif palpite == palavra:
            print("Parabéns! Você acertou a palavra!")
            break
        else:
            print("Palavra incorreta!")
            tentativas -= 1
        
        if "_" not in letras_descobertas:
            print("Parabéns! Você descobriu a palavra!")
            break
    
    if tentativas == 0:
        print("Suas tentativas acabaram. A palavra era:", palavra)

jogar_adedonha()
