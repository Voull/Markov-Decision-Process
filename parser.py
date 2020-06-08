#no bugs
import sys

states = []
actions = []
costs = []
initialState = ""
goalState = ""

def parse_file(path):
    nonlocal states
    nonlocal costs
    nonlocal initialState
    nonlocal goalState

    with open(path, "r") as file:
        current_block = None
        current_action_pos = -1 #   ??
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
                    actions.append([line[1]])
            elif current_block == "states":
                states = line.split(", ")
            elif current_block == "action":
                actions[-1].append(gerarTransicao(line))
            elif current_block == "costs":
                costs.append(gerarCusto(line))
            elif current_block == "initialstate":
                initialState = line
            elif current_block == "goalstate":
                goalState = line


def gerarTransicao(line):
    line = line.split(" ")
    transicao = Transicao()
    transicao.estadoInit = line[0]
    transicao.estadoSuc = line[1]
    transicao.probabilidade = line[2]
    transicao.descartar = line[3]

    return transicao

def gerarCusto(line):
    line = line.split(" ")
    custo = Custo()
    custo.estadoAtual = line[0]
    custo.acao = line[1]
    custo.valorCusto = line[2]

    return custo


class Transicao:
    estadoInit = ""
    estadoSuc = ""
    probabilidade = 0.0
    descartar = 0.0


class Custo:
    estadoAtual = ""
    acao = ""
    valorCusto = 0.0

# parse_file("TestesGrid/FixedGoalInitialState/navigation_1.net")
# print("Finish")






