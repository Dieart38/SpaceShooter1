import pygame


pygame.init()
# Criando a janela de jogo
print("Setup Start")
window = pygame.display.set_mode(size = (800, 600)) # passa o tamanho da tela do jogo
clock = pygame.time.Clock()
print("Setup End")

print("Loop Start")
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close Window
            print('quit game')
            quit() # end pygame
            
