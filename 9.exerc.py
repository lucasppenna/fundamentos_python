#Exercício 9 – Continue até o usuário decidir parar

#Crie um programa que permaneça em execução enquanto o usuário responder: "sim"

#A cada repetição, mostre: "Treino iniciado!"

#Depois, pergunte novamente: "Deseja realizar outro treino?"

#Quando a resposta for diferente de sim, o while deve terminar 
#e o programa deve mostrar: "Treino encerrado."

#Não é necessário trabalhar com números neste exercício. 
#Utilize a resposta do input() como texto.

treinamento = input("deseja continuar?")

while treinamento == "sim":
    print("Treino iniciado!")
    treinamento = input("deseja continuar?")

print("Treino encerrado")
