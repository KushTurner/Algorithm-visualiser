from netrc import netrc
import pygame,sys,random
import algorithms.algs as algs
from settings import *
from list import arr

# change sort variable to "bubble" or "selection"

sort = "selection"

if sort.lower() == "bubble sort" or sort.lower() == "bubble":
    alg = algs.bubble(arr)
    FPS=60
elif sort.lower() == "selection sort" or sort.lower() == "selection":
    alg = algs.selection(arr)
    FPS = 15

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

