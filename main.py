import numpy as np
import pandas as pd
import pygame 

a = np.array([1, 2, 3])

b = np.array([50, 534, 2])

c = a + b
print(a * b)
print(c)


print("another fucking version")
print("GG")

window = pygame.display.set_mode((400, 400))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill((255, 55 ,255))
    pygame.display.flip()
