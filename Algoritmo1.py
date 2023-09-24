from sklearn import tree

def classificar_faixa_etaria(x):
    X = [[1], [5], [15], [30], [70]]  # Faixa Etária (Anos)
    Y = ["Bebê", "Criança", "Jovem", "Adulto", "Idoso"]  # Designação

    clf = tree.DecisionTreeClassifier()  # Instânciamento de Árvore para Classificação
    clf = clf.fit(X, Y)  # Treinando o Computador

    theidade = [[x]]

    previsao = clf.predict(theidade)  # Pedindo para o Computador Classificar

    return previsao[0]

idade = input("Digite a idade em Anos da Pessoa: ")
faixa_etaria = classificar_faixa_etaria(int(idade))  # Converte a entrada para um número inteiro

print(f"A classificação de {idade} anos é: {faixa_etaria}")