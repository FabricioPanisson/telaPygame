import pygame
pygame.init()
branco = (255,255,255)
tamanho = (600,400)
tela = pygame.display.set_mode( tamanho )
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            rodando = False
    tela.fill(branco)
    pygame.display.update()
pygame.quit()