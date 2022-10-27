import pygame
from settings import screen, GREEN, WHITE, RED, BLUE


W=10
X = 15
H=8

def bubble(arr):
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


def selection(arr):
        for i in range(len(arr)):
            cur_min_idx = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[cur_min_idx]:
                    cur_min_idx = j
            h2 = arr[cur_min_idx] * H
            rec = pygame.draw.rect(screen, BLUE, (cur_min_idx*X, 500-h2, W, h2))
            pygame.display.update(rec)
            rec = pygame.draw.rect(screen, WHITE, (cur_min_idx*X, 500-h2, W, h2))
            pygame.display.update(rec)
            h1 = arr[i] * H
            rec2 = pygame.draw.rect(screen, GREEN, (i*X, 500-h1, W, h1))
            pygame.display.update(rec)
            rec2 = pygame.draw.rect(screen, WHITE, (i*X, 500-h1, W, h1))
            pygame.display.update(rec)
            arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]
            yield arr