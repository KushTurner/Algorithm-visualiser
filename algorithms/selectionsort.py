import pygame
from settings import screen, BLUE, WHITE, GREEN

def selection(arr):
        W = 10
        H = 8
        X = 15
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