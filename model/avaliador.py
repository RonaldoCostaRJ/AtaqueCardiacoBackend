from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from model.modelo import Model

class Avaliador:
#classe utilizada no teste do modelo.
    def avaliar(model, X_test, Y_test):
        """ Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
        avaliação, entre outros.
        """
        predicoes = Model.preditor(model, X_test)
        

        return accuracy_score(Y_test, predicoes)
                
