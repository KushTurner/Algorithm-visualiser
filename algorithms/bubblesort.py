import pygame
from settings import screen, GREEN, WHITE, RED


def bubble(arr):
    W=10
    X = 15
    H=8
    length = len(arr)
    for i in range(length-1):
        for j in range(0, length-i-1):
            if arr[j] > arr[j+1]:
                h1 = arr[j] * H
                h2 = arr[j+1] * H
                rec1 = pygame.draw.rect(screen, GREEN, (j*X, 500-h1, W, h1))
                rec2 = pygame.draw.rect(screen, RED, ((j+1)*X, 500-h2, W, h2))
                pygame.display.update(rec1)
                pygame.display.update(rec2)
                rec1 = pygame.draw.rect(screen, WHITE, (j*X, 500-h1, W, h1))
                rec2 = pygame.draw.rect(screen, WHITE, ((j+1)*X, 500-h2, W, h2))
                pygame.display.update(rec1)
                pygame.display.update(rec2)
                rec1 = pygame.draw.rect(screen, RED, (j*X, 500-h1, W, h1))
                rec2 = pygame.draw.rect(screen, GREEN, ((j+1)*X, 500-h2, W, h2))
                pygame.display.update(rec1)
                pygame.display.update(rec2)
                rec1 = pygame.draw.rect(screen, WHITE, (j*X, 500-h1, W, h1))
                rec2 = pygame.draw.rect(screen, WHITE, ((j+1)*X, 500-h2, W, h2))
                pygame.display.update(rec1)
                pygame.display.update(rec2)
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr


