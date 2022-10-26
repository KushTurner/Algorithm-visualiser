from netrc import netrc
import pygame,sys,random

#    pygame.draw.rect(screen, BLACK, (0, 400, 100, 100))
#    pygame.draw.rect(screen, BLACK, (200, 300, 100, 200))
#    pygame.draw.rect(screen, BLACK, (400, 200, 100, 300))
#    pygame.draw.rect(screen, BLACK, (600, 100, 100, 400))
#    pygame.draw.rect(screen, BLACK, (800, 0, 100, 500))

pygame.init()

FPS = 15
WIDTH, HEIGHT = 900, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visualiser")

def makelst(num):
    lst = [*range(1, num+1)]
    random.shuffle(lst)
    return lst

x = makelst(100)

def scr(lst):
    for idx, val in enumerate(lst):
            x = idx * 5
            h = val * 5
            y = 500 - h
            w = 5
            pygame.draw.rect(screen, WHITE, (x, y, w, h))
    pygame.display.update()

def sort():
        for i in range(len(x)):
            cur_min_idx = i
            for j in range(i+1, len(x)):
                if x[j] < x[cur_min_idx]:
                    cur_min_idx = j
            h2 = x[cur_min_idx] * 5
            rec = pygame.draw.rect(screen, BLUE, (cur_min_idx*5, 500-h2, 5, h2))
            pygame.display.update(rec)
            rec = pygame.draw.rect(screen, WHITE, (cur_min_idx*5, 500-h2, 5, h2))
            pygame.display.update(rec)
            h1 = x[i] * 5
            rec = pygame.draw.rect(screen, GREEN, (i*5, 500-h1, 5, h1))
            pygame.display.update(rec)
            rec = pygame.draw.rect(screen, WHITE, (i*5, 500-h1, 5, h1))
            pygame.display.update(rec)
            x[i], x[cur_min_idx] = x[cur_min_idx], x[i]
            yield x

a = sort()

def main():
    clock = pygame.time.Clock()
    run = True
    sorting = True
    while run:
        clock.tick(FPS) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if sorting:     
            try:
                next(a)
                screen.fill((0,0,0))
                scr(x)
            except StopIteration:
                sorting = False
        else:
            scr(a)
        


    pygame.quit()

if __name__ == "__main__":
    main()

