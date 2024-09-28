
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import *
from logger import logger
from schemas import *
from flask_cors import CORS

############################################################################################################
# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

############################################################################################################
# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
paciente_tag = Tag(name="Pacientes", description="Adição, visualização, remoção e predição de ataque cardiaco em pacientes")

# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

##########################################################################################################
# Rota de listagem de pacientes
##########################################################################################################
@app.get('/pacientes', tags=[paciente_tag],
         responses={"200": ListaPacientesSchema, "404": ErrorSchema})
def get_pacientes():
   
    logger.debug("Coletando dados sobre todos os pacientes")
    # Criando conexão com a base
    session = Session()
    # Buscando todos os pacientes
    pacientes = session.query(Paciente).all()
    
    if not pacientes:
        # Se não houver pacientes
        return {"pacientes xxx": []}, 200
    else:
        logger.debug(f"%d pacientes econtrados" % len(pacientes))
        print(pacientes)
        return apresenta_pacientes(pacientes), 200

#########################################################################################################
# Rota de adição de paciente
#########################################################################################################
@app.post('/paciente', tags=[paciente_tag],
          responses={"200": PacienteViewSchema, "400": ErrorSchema, "409": ErrorSchema})

def predict(form: PacienteSchema):
    """Adiciona um novo paciente à base de dados
    Retorna uma representação dos pacientes e diagnósticos associados.
    """
        
    ########################
    # Recuperando dados do formulario
    ########################
    age = form.age
    sex = form.sex
    cp = form.cp
    trtbps = form.trtbps
    chol = form.chol
    fbs = form.fbs
    restecg = form.restecg
    thalachh = form.thalachh
    exng = form.exng
    oldpeak = form.oldpeak
    slp = form.slp
    caa = form.caa
    thall = form.thall
    
    ########################
    # Realizando a Predição do Paciente
    ########################
    # Preparando os dados para o modelo
    X_input = PreProcessador.preparar_form(form)
    # Padronização nos dados de entrada usando o scaler utilizado em X
    rescaledEntradaX = PreProcessador.scaler(X_input)
    # Carregando modelo  
    model_path = './MachineLearning/models/knn_heart_attack_classifier.pkl'
    modelo = Model.carrega_modelo(model_path)  
    # Realizando a predição
    output = int(Model.preditor(modelo, rescaledEntradaX)[0])
    ########################
    # Persistindo o Paciente
    ########################
    paciente = Paciente(
        age = age,
        sex = sex,
        cp = cp,
        trtbps = trtbps,
        chol = chol,
        fbs = fbs,
        restecg = restecg,
        thalachh = thalachh,
        exng = exng,
        oldpeak = oldpeak,
        slp = slp,
        caa = caa,
        thall = thall,
        output=output       
    )
    #logger.debug(f"Adicionando paciente de id: '{paciente.id}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se paciente já existe na base
       # if session.query(Paciente).filter(Paciente.id == form.id).first():
        #    error_msg = "Paciente já existente na base :/"
         #   logger.warning(f"Erro ao adicionar paciente '{paciente.id}', {error_msg}")
          #  return {"message": error_msg}, 409
        
        # Adicionando paciente
        session.add(paciente)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado paciente id: '{paciente.id}'")
        return apresenta_paciente(paciente), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar paciente '{paciente.id}', {error_msg}")
        return {"message": error_msg}, 400
    

##########################################################################################################
# Rota de busca de paciente por id
@app.get('/paciente', tags=[paciente_tag],
         responses={"200": PacienteViewSchema, "404": ErrorSchema})
def get_paciente(query: PacienteBuscaSchema):    
       
    paciente_id = query.id
    logger.debug(f"Coletando dados sobre paciente #{paciente_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    paciente = session.query(Paciente).filter(Paciente.id == paciente_id).first()
    
    if not paciente:
        # se o paciente não foi encontrado
        error_msg = f"Paciente {paciente_id} não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{paciente_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Paciente econtrado: '{paciente.id}'")
        # retorna a representação do paciente
        return apresenta_paciente(paciente), 200
   
#################################################################################################    
# Rota de remoção de paciente por id
@app.delete('/paciente', tags=[paciente_tag],
            responses={"200": PacienteViewSchema, "404": ErrorSchema})
def delete_paciente(query: PacienteBuscaSchema):
  
    paciente_id = query.id
    logger.debug(f"Deletando dados sobre paciente #{paciente_id}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando paciente
    paciente = session.query(Paciente).filter(Paciente.id == paciente_id).first()
    
    if not paciente:
        error_msg = "Paciente não encontrado na base :/"
        logger.warning(f"Erro ao deletar paciente '{paciente_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(paciente)
        session.commit()
        logger.debug(f"Deletado paciente #{paciente_id}")
        return {"message": f"Paciente {paciente_id} removido com sucesso!"}, 200
    
if __name__ == '__main__':
    app.run(debug=True)