#Exercício 3 – Trabalhando com operadores

#Considere:

#pontos = 7
#vitorias = 2
#saldo_gols = 4

#Crie expressões que respondam às seguintes perguntas:


#1. A seleção possui mais de 5 pontos?
#2. A seleção possui exatamente 3 vitórias?
#3. O saldo de gols é maior ou igual a 0?
#4. A seleção possui mais de 5 pontos e saldo de gols positivo?
#5. A seleção possui 3 vitórias ou mais de 6 pontos?

pontos = 7
vitorias = 2
saldo_gols = 4

if pontos > 5:
    print(f"Passou de 5...Já está com {pontos}")

if vitorias == 3:
    print(f"ainda não...está com apenas {vitorias}")

if saldo_gols >=0:
    print(f"saldo de gols já em {saldo_gols}")

if pontos > 5 and saldo_gols >=0:
    print("pontos maior q 5, e saldo de gols positivo")

if pontos >= 6 or vitorias ==3:
    print("possui mais de 6 pontos ou tem 3 vitórias")