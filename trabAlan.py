vetor = []
for i in range(1, 1001):
    vetor.append(i)

def b_linear(alvo, vetor):
    comp_b_linear = 0
    for i in range(0, 1000):
        comp_b_linear += 1
        if vetor[i] == alvo:
            print("Valor encontrado na posicao:", i)
            print("Numero de comparacoes:", comp_b_linear)
        if i > 1000:
            print("Valor nao encontrado!")
            return -1

def b_binaria(alvo, vetor, menor, maior, comp_b_binaria):
    if menor > maior:
        print("Valor nao encontrado!")
        return -1
    meio = (maior + menor) / 2
    meio = int(meio)
    if vetor[meio] < alvo:
        comp_b_binaria += 1
        b_binaria(alvo, vetor, meio+1, maior, comp_b_binaria)
    elif vetor[meio] > alvo:
        comp_b_binaria += 1
        b_binaria(alvo, vetor, menor, meio-1, comp_b_binaria)
    else:
        print("Valor encontrado na posicao:", meio)
        print("Numero de comparacoes:", comp_b_binaria)

frequencia = {}
def b_tabela(alvo, vetor):
    for i in vetor:
        if i in frequencia:
            frequencia[i] += 1
        else:
            frequencia[i] = 1
    if alvo in frequencia.keys():
        print("Verdadeiro")
    else:
        print("Falso")

print("\nBusca Linear")
b_linear(500, vetor)
print("----------------")
print("\nBusca Binaria")
b_binaria(500, vetor, 0, 999, 0)
print("----------------")
print("\nBusca por Tabela de Frequencia")
b_tabela(500, vetor)
print("----------------")

print("\nBusca Linear")
b_linear(200, vetor)
print("----------------")
print("\nBusca Binaria")
b_binaria(200, vetor, 0, 999, 0)
print("----------------")
print("\nBusca por Tabela de Frequencia")
b_tabela(200, vetor)
print("----------------")

print("\nBusca Linear")
b_linear(1001, vetor)
print("----------------")
print("\nBusca Binaria")
b_binaria(1001, vetor, 0, 999, 0)
print("----------------")
print("\nBusca por Tabela de Frequencia")
b_tabela(1001, vetor)
print("----------------")