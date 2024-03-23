import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 452))
    pygame.display.set_caption("A Relic of a Bygone Era")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill("darkslategray")
    background = pygame.image.load("cityscape.png")
    dvd = pygame.image.load("dvd.png")
    dvd = dvd.convert_alpha()
    dvd = pygame.transform.scale(dvd, (100, 100))
    dvd_x = 0
    dvd_y = 200
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        dvd_x += 5
        dvd_y += 5
        if dvd_x > screen.get_width():
            background = pygame.image.load("cityscape.png")
            dvd_x = 0
      
        if dvd_y > screen.get_height():
            background = pygame.image.load("smogcity.png")
            dvd_y = 200
        
        screen.blit(background, (0, 0))
        screen.blit(dvd, (dvd_x, dvd_y))
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    main()