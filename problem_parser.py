#no bugs HAHAHAHAH
from typing import List

# states = []
# actions = []
# costs = []
# initialState = ""
# goalState = ""


class Transicao:
    estadoInit = ""
    estadoSuc = ""
    probabilidade = 0.0
    descartar = 0.0

class Acao:
    def __init__(self, nomeAcao: str="", transicoes: List[Transicao]=[]):
        self.nome = nomeAcao
        self.transicoes = transicoes

    def novaTransicao(self, transicao: Transicao) -> None:
        self.transicoes.append(transicao)

    def getTransicoes(self) -> List[Transicao]:
        return self.transicoes

class Custo:
    estadoAtual = ""
    acao = ""
    valorCusto = 0.0

class Estado:
    def __init__(self, estado: str = "", valorBellman: float = 0.0):
        self.estado = estado
        self.valorBellman = valorBellman


class Problema:
    def __init__(self, estados: List[Estado]=[], acoes: List[Acao]=[], custos: List[Custo]=[], estadoInicial: str="", estadoObjetivo: str=""):
        self.estados = estados
        self.acoes = acoes
        self.custos = custos
        self.estadoInicial = estadoInicial
        self.estadoObjetivo = estadoObjetivo




def gerarTransicao(line: str) -> Transicao:
    line = line.split(" ")
    transicao = Transicao()
    transicao.estadoInit = line[0]
    transicao.estadoSuc = line[1]
    transicao.probabilidade = line[2]
    transicao.descartar = line[3]

    return transicao


def gerarCusto(line: str) -> Custo:
    line = line.split(" ")
    custo = Custo()
    custo.estadoAtual = line[0]
    custo.acao = line[1]
    custo.valorCusto = line[2]

    return custo


def gerarProblema(estados: List[str], acoes: List[Acao], custos: List[Custo], estadoInicial: str, estadoObjetivo: str) -> Problema:

    return Problema(estados, acoes, custos, estadoInicial, estadoObjetivo)


def parse_file(path: str) -> Problema:
    # nonlocal states
    # nonlocal costs
    # nonlocal initialState
    # nonlocal goalState

    actions = []
    costs = []

    with open(path, "r") as file:
        current_block = None
        for line in file:
            line = line.strip()
            if not line: #if vazia
                continue
            elif line.startswith("end"):
                current_block = None
                continue
            elif line.startswith("Grid"):
                break
            if current_block is None:
                line = line.split(" ")
                current_block = line[0]
                if current_block == "action":
                    actions.append(Acao(line[1]))
            elif current_block == "states":
                states = []
                for state in line.split(", "):
                    states.append(Estado(state))
            elif current_block == "action":
                actions[-1].novaTransicao(gerarTransicao(line))
            elif current_block == "cost":
                costs.append(gerarCusto(line))
            elif current_block == "initialstate":
                initialState = line
            elif current_block == "goalstate":
                goalState = line

    return gerarProblema(states, actions, costs, initialState, goalState)

# parse_file("TestesGrid/FixedGoalInitialState/navigation_1.net")
# print("Finish")






