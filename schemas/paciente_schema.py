from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente
import json
import numpy as np

class PacienteSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """
    age: int = 52
    sex: int = 1
    cp: int = 3 
    trtbps: int = 145
    chol:int = 233 
    fbs: int = 1
    restecg: int = 1
    thalachh: float = 150
    exng: float = 1 
    oldpeak: float = 3.5
    slp: int = 1
    caa: int = 2
    thall: int = 2 
    

class PacienteViewSchema(BaseModel):
    """Define como um paciente será retornado
    """
    id: int = 1
    age: int = 52
    sex: int = 1
    cp: int = 3 
    trtbps: int = 145
    chol:int = 233 
    fbs: int = 1
    restecg: int = 1
    thalachh: float = 150
    exng: float = 1 
    oldpeak: float = 3.5
    slp: int = 1
    caa: int = 2
    thall: int = 2 
    output: int = None
    
class PacienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no id do paciente.
    """
    id: int = 1

class ListaPacientesSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    pacientes: List[PacienteViewSchema]

    
class PacienteDelSchema(BaseModel):
    """Define como um paciente para deleção será representado
    """
    id: int = 1
    
# Apresenta apenas os dados de um paciente    
def apresenta_paciente(paciente: Paciente):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "id": paciente.id,
        "age": paciente.age,
        "sex": paciente.sex,
        "cp": paciente.cp,
        "trtbps": paciente.trtbps,
        "chol": paciente.chol,
        "fbs": paciente.fbs,
        "restecg": paciente.restecg,
        "thalachh": paciente.thalachh,
        "exng": paciente.exng,
        "oldpeak": paciente.oldpeak,
        "slp": paciente.slp,
        "caa": paciente.caa,
        "thall": paciente.thall,
        "output": paciente.output
    }
    
# Apresenta uma lista de pacientes
def apresenta_pacientes(pacientes: List[Paciente]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    result = []
    for paciente in pacientes:
        result.append({
        "id": paciente.id,
        "age": paciente.age,
        "sex": paciente.sex,
        "cp": paciente.cp,
        "trtbps": paciente.trtbps,
        "chol": paciente.chol,
        "fbs": paciente.fbs,
        "restecg": paciente.restecg,
        "thalachh": paciente.thalachh,
        "exng": paciente.exng,
        "oldpeak": paciente.oldpeak,
        "slp": paciente.slp,
        "caa": paciente.caa,
        "thall": paciente.thall,
        "output": paciente.output        
        })
    return {"pacientes": result}

