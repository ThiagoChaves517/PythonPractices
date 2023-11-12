from algoritmosBusca import algoritmo_A_Estrela
from labirintos import geraLabirinto, gerarPontoDePartida, gerarSaidaLabirinto
import tkinter as tk

# -------------------------------------------------------------------------------------------------

#   Este código gera um labirinto aleatório toda vez que o programa for aberto.
#   Feche e abra o programa para ter diversos labirintos diferentes.

# -------------------------------------------------------------------------------------------------

def pintarCaminho(matrizLabirinto, canvas, tamanhoQuadrado, personagem, pF, corredores):
    x1, y1, x2, y2 = canvas.coords(personagem)
    x = round(x1/tamanhoQuadrado)
    y = round(y1/tamanhoQuadrado)

    # Reescreve a matriz para a sua forma original, isso se o caminho para pF já tivesse pintado antes:
    for ponto in corredores:
        if(ponto != (y, x)):
            canvas.create_rectangle(ponto[1]*tamanhoQuadrado, ponto[0]*tamanhoQuadrado, ponto[1]*tamanhoQuadrado+tamanhoQuadrado, ponto[0]*tamanhoQuadrado+tamanhoQuadrado, fill="white")

    # A variável caminhoParaSaida contém o caminho mais curto até a saída do labirinto (do ponto atual até o ponto pF).
    # A função algoritmo_A_Estrela() retorna este caminho.
    # Se não ouver caminho possível, o ponto (0,0) será retornado... mas isso não é para acontecer, de qualquer forma.
    caminhoParaSaida = algoritmo_A_Estrela((y,x), pF, matrizLabirinto)
    for ponto in caminhoParaSaida:
        if(ponto != (y, x)):
            canvas.create_rectangle(ponto[1]*tamanhoQuadrado, ponto[0]*tamanhoQuadrado, ponto[1]*tamanhoQuadrado+tamanhoQuadrado, ponto[0]*tamanhoQuadrado+tamanhoQuadrado, fill="red")


# Função que desenha uma janela indicando que o nosso jogador ganhou.
def pintarVoceGanhou(canvas):
    canvas.create_rectangle(300, 300, 900, 500, fill="green")
    canvas.create_text(600, 400, text="VOCÊ VENCEU!", fill="yellow", font=("Times", 50))

# Função para mover o personagem
def mover_personagem(event, canvas, personagem, matrizLabirinto, tamanhoQuadrado, pontoFinal):
    x1, y1, x2, y2 = canvas.coords(personagem)
    x = round(x1/tamanhoQuadrado)
    y = round(y1/tamanhoQuadrado)

    #Se a tecla "seta de cima" for pressionada e o personagem nos limites da matriz, o persongem anda para cima.
    if event.keysym == 'Up' and y > 0 and matrizLabirinto[y-1][x] == 0:
        canvas.move(personagem, 0, -tamanhoQuadrado)
    
    #Se a tecla "seta de baixo" for pressionada e o personagem nos limites da matriz, o persongem anda para baixo.
    elif event.keysym == 'Down' and y < len(matrizLabirinto) - 1 and matrizLabirinto[y+1][x] == 0:
        canvas.move(personagem, 0, tamanhoQuadrado)

    #Se a tecla "seta da esquerda" for pressionada e o personagem nos limites da matriz, o persongem vai para a esquerda.
    elif event.keysym == 'Left' and x > 0 and matrizLabirinto[y][x-1] == 0:
        canvas.move(personagem, -tamanhoQuadrado, 0)
    
    #Se a tecla "seta da direita" for pressionada e o personagem nos limites da matriz, o persongem vai para a direita.
    elif event.keysym == 'Right' and x < len(matrizLabirinto[0]) - 1 and matrizLabirinto[y][x+1] == 0:
        canvas.move(personagem, tamanhoQuadrado, 0)

    if((y,x) == pontoFinal):
        pintarVoceGanhou(canvas)
    
    # Torna o personagem visível sobre qualquer outra peça do labirinto.
    # Isto é necessário porque este labirinto é desenhado de quadrado a quadrado
    # e também porque, no TkInter, as peças (quadrados) mais novas são aqueles
    # que irão aparecer mais a cima na pilha de visibilidade.
    # Logo, a função tag_raise() coloca o personagem no topo dessa fila.
    canvas.tag_raise(personagem)

def main():
    # As interfaces do TkInter são inicializadas através das variáveis canvas e window.
    window = tk.Tk()
    window.configure(background="grey")
    canvas = tk.Canvas(window, width=1200, height=1000, background="grey")
    window.geometry('1200x1000')
    tamanhoQuadrado = 38 # Contém o tamanho que cada bloco do labirinto terá.

    matrizLabirintoDeBools = [] # Matriz onde o labirinto será formado é iniciada.
    linhas = 19
    colunas = 23
    corredores = [] # Recebe todos os corredores "0" do labirinto a medida em que o labirinto é criado
                    # na função geraLabirinto(). Por isso é passado como parâmetro. 

    # São gerados o labirinto, o ponto de partida de Codibentinho e a saída da armadilha mortal:
    geraLabirinto(matrizLabirintoDeBools, linhas, colunas, corredores)
    p0 = gerarPontoDePartida(corredores)
    pF = gerarSaidaLabirinto(matrizLabirintoDeBools, linhas, colunas, corredores)
    
    for i in range(linhas): 
        for j in range(colunas):
            # Se o ponto for uma parede... 
            if matrizLabirintoDeBools[i][j] == 1:
                canvas.create_rectangle(j*tamanhoQuadrado, i*tamanhoQuadrado, j*tamanhoQuadrado+tamanhoQuadrado, i*tamanhoQuadrado+tamanhoQuadrado, fill="black")
            # Se o ponto for um corredor...
            else:  
                canvas.create_rectangle(j*tamanhoQuadrado, i*tamanhoQuadrado, j*tamanhoQuadrado+tamanhoQuadrado, i*tamanhoQuadrado+tamanhoQuadrado, fill="white")

    # O personagem principal, Codibentinho, é desenhado, tendo em conta que será desenhado no ponto p0: 
    personagem = canvas.create_rectangle(p0[1]*tamanhoQuadrado, p0[0]*tamanhoQuadrado, p0[1]*tamanhoQuadrado+tamanhoQuadrado, p0[0]*tamanhoQuadrado+tamanhoQuadrado, fill="green")

    # É criado do um título para o jogo:
    canvas.create_text(1037, 100, text="Labirinto do Codibentinho", fill="blue4", font=("Times", 19, "bold"))
    canvas.create_text(1040, 127, text="Deluxe Premiun XZ", fill="blue4", font=("Times", 19, "bold"))
    canvas.create_text(1040, 154, text="Mega Edition", fill="blue4", font=("Times", 19, "bold"))

    # É criado um botão que mostrará o caminho
    botao = tk.Button(window, text="FIND ANSWER", command=lambda: pintarCaminho(matrizLabirintoDeBools, canvas, tamanhoQuadrado, personagem, pF, corredores), width=15, height=13, background="grey", bd=5)
    botao.place(x=980,y=300) # Escolhe as coordenadas onde o botão deverá ser colocado.

    # O labirinto completo e a interface do programa são desenhados:
    canvas.pack()

    # O sistema de movimentação do personagem é acionado:
    window.bind_all('<Key>', lambda event: mover_personagem(event, canvas, personagem, matrizLabirintoDeBools, tamanhoQuadrado, pF))

    window.mainloop() # Mantém a janela do aplicativo aberta.

main()


