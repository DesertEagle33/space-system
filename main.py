import pygame
import numpy as np
import objects
screen = pygame.display.set_mode((1920, 1000))

rocket = objects.Rocket('spaceship.png', size = (55, 55), spawn_coords = (700, 500), spawn_velocity=(0,1))


planets = [objects.Planet('sun.png', (960,500), ang_vel=0, mass = 1),
          # objects.Planet('mercury.png', (960, 500), ang_vel = 0.01, radius_orbit = 100, size =(45, 35), mass = 0.5),
          # objects.Planet('venus.png', (960, 500), (35, 25), 150, 0.01, 150, mass = 0.2),
           #objects.Planet('earth.png', (960, 500), size = (60, 50), start_ang_pos = 250, radius_orbit = 250, ang_vel= 0.01, mass = 0.3 )
]

#earth = planets[3]

#moon = objects.Planet('moon.png', earth.get_coords(), ang_vel = 0.01, radius_orbit = 50, size =(15, 15))

red = (255, 0, 0)
screen = pygame.display.set_mode((1920, 1000))
space = pygame.image.load('space.png')
space = pygame.transform.scale(space, (1920, 1000))


x = 0
pos = [0, 0, 150, 150]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.time.delay(10)
    #satelites = [objects.satelites('moon.png', (10, 10), start_ang_pos=(100), ang_vel=0.001, radius_orbit=10).blit(space, space.get_rect(center=(960, 500)))

    screen.blit(space, space.get_rect(center = (960, 500)))

    for planet in planets:
        planet.draw(screen)
        planet.update()

    rocket.get_acceleration(planets = planets, G = 1000)
    rocket.draw(screen)
    print(rocket.energy(planets = planets, G = 1000))

   # moon.draw(screen)
   # moon.update(earth_coords = earth.get_coords())

    pygame.display.update()
    #print(earth.get_coords())
