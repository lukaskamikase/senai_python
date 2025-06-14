import pygame

pygame.init()

screen = pygame.display.set_mode((400,300))

done = False
azul = True
x = 30 
y = 30

frame = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        azul = not azul

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3

        if azul:
                color = (0, 128, 255)
        else: 
                color = (255, 100, 0)
      
        pygame.draw.circle(screen, color,(x, y),40.0)
    
        pygame.display.flip()
        frame.tick(200)