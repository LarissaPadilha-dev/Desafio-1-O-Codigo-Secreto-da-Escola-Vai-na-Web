#📌Desafio 1: O Código Secreto da Escola Vai na Web

#Missão 1: Restaurando as Regras Escolares 📝
    #O vírus apagou os critérios de aprovação dos alunos! Para ajudar o Professor Byte a organizar o sistema, sua tarefa é criar um programa que verifique se um aluno foi aprovado (nota maior ou igual à 5) ou reprovado (nota menor ou igual à 5).
    
nota = float(input('Digite a nota do aluno: '))

if nota >= 6:  
    print('Parabéns 😊! você foi aprovado.')  
else:  
    print('Sinto muito 😔, você foi reprovado!')
    
#Missão 2: O Sistema Eleitoral Secreto 📝
    #O grêmio estudantil da escola realiza votações para decidir melhorias e inovações, mas o vírus desativou a verificação de elegibilidade para votar! Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).
    
idade =int(input ("Qual sua idade: ")) 

if idade >=16:
    print('O aluno pode votar!')
else:  
    print('O aluno não idade pra votar!')

#Missão 3: Recuperando o Sistema de Notas 📊
    #As classificações das provas desapareceram! Agora os alunos não sabem se tiraram um não sabem se tiraram um A, B, C, D ou F . Antes que o pânico se espalhe, sua tarefa é criar um programa que peça a nota do aluno e imprima sua classificação conforme a escala:

    #- A (90-100) – "Parabéns, você tirou A!"
    #- B (80-89) – "Muito bem, você tirou B."
    #- C (70-79) – "Bom trabalho, você tirou C."
    #- D (60-69) – "Fique atento, você tirou D."
    #- F (menos de 60) – "Estude um pouco mais, você tirou F."
    
nota = float(input("Digite sua nota: "))
if 90 <= nota <= 100:
    print("Parabéns, você tirou A!")
elif 80 <= nota < 90:
    print("Muito bem, você tirou B.")
elif 70 <= nota < 80:
    print("Bom trabalho, você tirou C.")
elif 60 <= nota < 70:
    print("Fique atento, você tirou D.")
else:
    print("Estude um pouco mais, você tirou F.")

#Missão 4: Restaurando a Identificação de Números ⚖️
    #Os robôs da escola precisam identificar padrões numéricos para resolver cálculos e otimizar os sistemas. No entanto, o vírus bagunçou os algoritmos e agora eles não conseguem mais somar corretamente!
    #Crie um programa que peça dois números ao usuário e exiba a soma deles.
    
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print(f"A soma dos números é: {num1 + num2}")

#Missão 5: Recuperando o Cofre de Segurança 🔒
    #O cofre da biblioteca guarda códigos raros de programação, mas o vírus resetou a senha! Agora, apenas quem souber a combinação correta poderá acessá-lo.
    #Crie um programa que solicite ao usuário uma senha e verifique se ela está correta. A senha correta é "Python123".
    
senha = input("Digite a senha: ")
if senha == "Python123":
    print("Acesso concedido!")
else:
    print("Senha incorreta!")

#Missão 6: Reforçando a Segurança e a Contagem do Sistema 💾
    #O vírus está comprometendo o sistema de segurança e a contagem de registros! Para restaurar o funcionamento correto, você precisa reforçar as verificações e garantir que os dados sejam processados corretamente.
    #Exiba os números de 1 a 10 usando um loop while. 
     
num = 1
while num <= 10:
    print(num)
    num += 1
    
#Missão 7: Organizando a Lista📋
    #Os números estão misturados e precisam ser organizados! 
    #Para resolver isso, você deve pegar os seguintes números: 8, 3, 10, 1 e 5, armazená-los em uma lista e depois exibi-los em ordem crescente. Isso ajudará a colocar tudo em ordem corretamente!  
    
numeros = [ 8, 3, 10, 1,5]
numeros.sort()
print("Números em ordem crescente: !", numeros)

#Missão 8: Acessando os Registros de Alunos 🏷️
    #O sistema de alunos está desordenado! Para acessar as informações corretamente, você precisa organizar os dados.
    #Crie uma tupla com os seguintes nomes: Ana, Bruno, Carla, Daniel, Eduardo e exiba o primeiro e o último nome.  
    
alunos = [" Ana", "Bruno", " Carla", "Daniel"," Eduardo"]

print("Primeiro nome:", alunos[0])
print("Último nome:", alunos[-1])

#Missão 9: Calculando Dobro de um Número 🛠️
    #Os alunos precisam de um programa que ajude em cálculos rápidos. 
    #Sua tarefa é criar uma função que receba um número e retorne o dobro do seu valor.
    #➡️ Exemplo: dobro(5)
    #➡️ Saída: "O dobro de 5 é 10"
    
def dobro(num):
    return f"O dobro de {num} é {num * 2}"
print(dobro(18))

#Missão 10: Contando Letras 🔄
    #O sistema precisa contar quantas letras há em um nome.
    #➡️ Crie uma função que receba um nome e diga quantas letras esse nome tem.
    #➡️ Exemplo: contar_letras("Ana")
    #➡️ Saída:" O nome Ana tem 3 letras"
    
def contar_letras(nome):
    return f"O nome {nome} tem {len(nome)} letras"

print(contar_letras("Larissa"))

#🔹 Você restaurou a escola Vai na Web! 🎉 Com cada desafio superado, você ajudou a salvar o sistema. Agora, você se tornou um(a) verdadeiro(a) programador(a) FullStack lendário(a)!!! 🚀