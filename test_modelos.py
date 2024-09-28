from model import *

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
#avaliador = Avaliador()

# Parâmetros    
url_dados = "./MachineLearning/data/test_heart.csv"
colunas = ['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg', 'thalachh', 'exng','oldpeak', 'slp', 'caa', 'thall','output' ]

# Carga dos dados
dataset = Carregador.carregar_dados(url_dados, colunas)
array = dataset.values
X = array[:,0:-1]
y = array[:,-1]
 
# Método para testar o modelo Knn a partir do arquivo correspondente

def test_modelo_lr():  
    # Importando o modelo KNN
    knn_path = './MachineLearning/models/knn_heart_attack_classifier.pkl'
    modelo_knn = Model.carrega_modelo(knn_path)

    # Obtendo as métricas do KNN
    acuracia_knn = Avaliador.avaliar(modelo_knn, X, y)
    
    # Testando as métricas do knn
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_knn >= 0.77 
    # assert recall_lr >= 0.5 
    # assert precisao_lr >= 0.5 
    # assert f1_lr >= 0.5 
 