from sklearn import tree
import random


nomes = [
    "Ana Silva", "Caneta Azul", "Mariana Oliveira", "João Pereira", "Luisa Rodrigues",
    "Pedro Alves", "Sofia Vieira", "Rafael Gomes", "Laura Fernandes", "Lucas Martins",
    "Isabela Barbosa", "Gustavo Sousa", "Manuela Costa", "Matheus Ferreira", "Clara Santos",
    "Davi Rodrigues", "Valentina Almeida", "Enzo Lima", "Beatriz Pereira", "Gabriel Rocha",
    "Sophia Castro", "Lorenzo Ribeiro", "Olivia Cardoso", "Lucas Araujo", "Helena Lima",
    "Pedro Rocha", "Isabella Carvalho", "Guilherme Fernandes", "Laura Barbosa", "Matheus Gomes",
    "Julia Silva", "Arthur Almeida", "Lara Oliveira", "Bernardo Sousa", "Valentina Ribeiro",
    "Heitor Martins", "Manuela Santos", "Davi Pereira", "Marina Vieira", "Théo Oliveira",
    "Alice Pereira", "Lorenzo Almeida", "Mariana Fernandes", "Enzo Rodrigues", "Maria Lima",
    "Gustavo Castro", "Clara Ribeiro", "Pedro Sousa", "Antonella Santos", "Leonardo Vieira",
    "Isabella Gomes", "Nicolas Pereira", "Helena Almeida", "Benjamin Silva", "Valentina Fernandes",
    "Samuel Oliveira", "Valentina Sousa", "Arthur Costa", "Lara Ribeiro", "Eduardo Gomes",
    "Yasmin Fernandes", "Luiz Felipe Alves", "Maria Eduarda Lima", "Lucas Pereira", "Heloísa Castro",
    "Davi Almeida", "Lorena Santos", "Lorenzo Martins", "Sophia Rodrigues", "Vinícius Vieira",
    "Antonella Pereira", "Felipe Fernandes", "Mariana Costa", "Henrique Sousa", "Laura Rodrigues",
    "Eduardo Gomes", "Clara Alves", "Lucca Ribeiro", "Isabella Lima", "Manoel Gomes",
    "Larissa Oliveira", "Rafael Vieira", "Marina Costa", "Enzo Castro", "Beatriz Fernandes",
    "Luiz Miguel Gomes", "Luiza Ribeiro", "Cauã Almeida", "Amanda Pereira", "Henrique Santos",
    "Isis Fernandes", "Luiz Fernando Oliveira", "Luana Carvalho", "Pedro Henrique Sousa", "Marina Pereira",
    "Anthony Martins", "Sophia Barbosa", "Enzo Almeida", "Lorena Fernandes", "José Silva"
]

campo_amostral = []

for i in range(100):
    nome = random.choice(nomes)
    idade = random.randint(0, 100)
    entrada = [nome, idade]
    campo_amostral.append(entrada)

def classificar_pessoas(x):
    # Defina as faixas etárias originais
    X_idade = [[0], [3], [13], [26], [61]]
    Y_idade = ["Bebê", "Criança", "Jovem", "Adulto", "Idoso"]
    
    clf_idade = tree.DecisionTreeClassifier().fit(X_idade, Y_idade)
    
    # Defina os intervalos de idade e as atividades correspondentes
    X_atividade = [[0], [10], [20], [30], [40], [50], [60], [70], [80], [90], [100]]
    Y_atividade = [
        "Brincar",
        "Esportes",
        "Atividades Recreativas",
        "Jantar Fora",
        "Dança",
        "Caminhadas",
        "Voluntariado",
        "Ioga",
        "Socialização",
        "Apreciar Cultura",
        "Massagem"
    ]

    clf_atividade = tree.DecisionTreeClassifier().fit(X_atividade, Y_atividade)

    # Adicione a classificação de faixa etária e a atividade recomendada ao campo_amostral
    for pessoa in x:
        idade = pessoa[1]
        theidade = [[idade]]
        faixa_etaria = clf_idade.predict(theidade)[0]
        atividade_recomendada = clf_atividade.predict(theidade)[0]
        pessoa.extend([faixa_etaria, atividade_recomendada])

    return x

campo_amostral_classificado = classificar_pessoas(campo_amostral)

for pessoa in campo_amostral_classificado:
    print(f"{pessoa[0]} ({pessoa[1]} anos) - {pessoa[2]}, Recomendado: {pessoa[3]}")