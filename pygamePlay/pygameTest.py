import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
eTime = 0 #using this to explore changing the background after a second
color1 = "purple"
color2 = pygame.Color(23, 190, 209)
currColor = color1

#playerPos will hold the location of the player circle. Starts in the middle
playerPos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
dt = 0 #delta time


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    eTime += clock.get_time() #just adding up how much time has passed
    if (eTime >= 1000):
        currColor = color2
        if (eTime >= 2000):
            eTime = 0
            currColor = color1
    screen.fill(currColor)
    pygame.draw.circle(screen,"white", playerPos, 60)

    #listen for input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerPos.y -= 300 * dt #moves the player position up
    if keys[pygame.K_a]:
        playerPos.x -= 300 * dt # left
    if keys[pygame.K_s]:
        playerPos.y += 300 * dt # down
    if keys[pygame.K_d]:
        playerPos.x += 300 * dt # right
    #render the screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000


pygame.quit()
