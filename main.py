import pygame
pygame.init()
x=400
y=300
velocidade = 10
timer = 0
tempo_segundo = 0
fundo = pygame.image.load('22432be137df445-removebg-preview.png')
carro = pygame.image.load('download-removebg-preview (1).png')

font = pygame.font.SysFont('arial black',30)
texto = font.render("Tempo: ", True,(255, 255,255),(0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jogo em python")

janela_aberta = True

while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y-= velocidade
    if comandos[pygame.K_DOWN]:
        y+= velocidade
    if comandos[pygame.K_LEFT]:
        x-= velocidade
    if comandos[pygame.K_RIGHT]:
        x+= velocidade
    if (timer <20):
        timer +=1
    else:
        tempo_segundo +=1
        texto = font.render("Tempo: "+str(tempo_segundo), True, (255, 255, 255), (0, 0, 0))
        timer = 0


    janela.blit(fundo, (160, 50))
    janela.blit(carro, (x, y))
    janela.blit(texto, pos_texto)
    pygame.display.update()


pygame.quit()