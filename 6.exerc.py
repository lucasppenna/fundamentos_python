#Utilizando o input(), peça ao usuário para informar a posição de um jogador. As opções esperadas são:

#goleiro
#defesa
#meio
#ataque
#Armazene a resposta em uma variável chamada posicao.

#Depois, utilize match case para verificar a posição informada 
#e mostrar uma mensagem correspondente à função daquele jogador em campo.

#Por exemplo: Digite a posição do jogador: ataque

#Saída esperada: Responsável principalmente pela criação e finalização das jogadas ofensivas.

#Crie também um caso para quando o usuário digitar uma posição diferente das opções esperadas. 
#Nesse caso, mostre: Posição inválida.

posicao = input("Digite a posicao do jogador: ")

match posicao:
    case "ataque":
        print("Responsável principalmente pela criação e finalização das jogadas ofensivas.")

    case "goleiro":
        print("Apenas defende, e não deve sair do gol.")    

    case "defesa":
        print("Fica no campo de defesa")

    case "meio":
        print("Arma as jogadas")

    case _:
        print("Posição inválida...reescreva")



