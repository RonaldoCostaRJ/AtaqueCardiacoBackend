from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union
from  model import Base

class Paciente(Base):
    ###################################################################################################
    #Classe com dados de um Paciente.
    __tablename__ = 'pacientes'

    id = Column(Integer, primary_key=True)
    age = Column("Age", Integer)
    sex = Column("Sex", Integer)
    cp = Column("Cp", Integer)
    trtbps = Column("Trtbps", Integer)
    chol = Column("Chol", Integer)
    fbs = Column("Fbs", Integer)
    restecg = Column("Restecg", Integer)
    thalachh = Column("Thala", Integer)
    exng = Column("Exng", Float)
    oldpeak = Column("Oldpeak", Float)
    slp = Column("Slp", Integer)
    caa = Column("Caa", Integer)
    thall = Column("Thall", Integer)
    output = Column("Diagnostic", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    #############################################################################################
    def __init__(self, age:int, sex:int, cp:int, trtbps:int, chol:int, fbs:int, restecg:int,
                 thalachh:int, exng:float, oldpeak:int, slp:int, caa:int, thall:int, output:int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Armazena os dados necessários para prover um diagnóstico de um Paciente 

        Argumentos:

        age      : Idade
        sex      : Sexo (sex = 0 female, sex = 1 male)
        cp       : Tipo de dor no peito ( Value 1: typical angina , Value 2: atypical angina, Value 3: non-anginal pain, Value 4: asymptomatic)
        trtbps   : pressão arterial em repouso (in mm Hg)
        chol     : colestoral em mg/dl obtido através do sensor de IMC
        fbs      : (açúcar no sangue em jejum > 120 mg/dl) (1 = true; 0 = false)
        restecg  : resultados eletrocardiográficos em repouso (Value 0: normal, Value 1: ter anormalidade da onda ST-T (inversões da onda T e/ou elevação ou depressão do segmento ST > 0,05 mV)
                   Value 2: mostrando hipertrofia ventricular esquerda provável ou definitiva pelos critérios de Estes)
        thalachh : frequência cardíaca máxima alcançada
        exng     : angina induzida por exercício? (1 = yes ; 0 = no)
        old peak : Depressão do segmento ST induzida por exercício em relação ao repouso
        slp      : slope
        caa      : number of major vessels (0-3)
        thall    : thall rate
        output   : target variable (target : 0= less chance of heart attack 1= more chance of heart attack)
        """
        self.age=age
        self.sex = sex
        self.cp = cp
        self.trtbps = trtbps
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalachh = thalachh
        self.exng = exng
        self.oldpeak = oldpeak
        self.slp = slp
        self.caa = caa
        self.thall = thall
        self.output = output

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao