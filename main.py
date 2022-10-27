from netrc import netrc
import pygame,sys,random
import algorithms.algs as algs
from settings import *
from list import arr

# change sort variable to "bubble" or "selection"

sort = "bubble"

if sort.lower() == "bubble sort" or sort.lower() == "bubble":
    FPS=60
    alg = algs.bubble(arr)
elif sort.lower() == "selection sort" or sort.lower() == "selection":
    FPS = 15
    alg = algs.selection(arr)
    

pygame.init()


def scr(lst):
    for idx, val in enumerate(lst):
            x = idx * 15
            h = val * 8
            y = 500 - h
            w = 10
            pygame.draw.rect(screen, WHITE, (x, y, w, h))
    pygame.display.update()



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
                next(alg)
                screen.fill((0,0,0))
                scr(arr)
            except StopIteration:
                sorting = False
        else:
            scr(arr)
        


    pygame.quit()

if __name__ == "__main__":
    main()

