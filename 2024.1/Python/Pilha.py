def push(pilha,valor):
    #adiciona um elemento no fim do array
    pilha.append(valor)

def pop(pilha):
    #remove o ultimo elemento
    pilha.pop()

def showStack(pilha):
    print(pilha[-1])

    pilha = []
    push(pilha, 10)
    push(pilha, 20)
    push(pilha, 30)

    pop(pilha)
    showStack(pilha)