import pygame
import numpy as np



class Planet:
    def __init__(self, file_name, start_coords, size = (200, 200), start_ang_pos = 0, ang_vel = 0, radius_orbit = 0, mass = 1 ):

        self.file_name = file_name
        self.image = pygame.transform.scale(pygame.image.load(self.file_name), size)
        self.coords = start_coords
        self.ang_pos = start_ang_pos
        self.ang_vel = ang_vel
        self.center_orbit_coords = start_coords
        self.radius_orbit = radius_orbit
        self.mass = mass


    def draw(self, screen):
        screen.blit(self.image, self.image.get_rect(center =self.coords))



    def update(self, dt = 1, earth_coords = (960, 500)):
        """""
        :rtype: object
        """""
        self.ang_pos += self.ang_vel*dt

        self.center_orbit_coords = earth_coords

        x = self.center_orbit_coords[0] + self.radius_orbit * np.cos(self.ang_pos)
        y = self.center_orbit_coords[1] + self.radius_orbit * np.sin(self.ang_pos)

        self.coords = (x, y)


    def get_coords(self):
        return self.coords

#class Satellites(Planet):
   # def __init__(self, file_name, start_coords, size=(200, 200), start_ang_pos=0, ang_vel=0, radius_orbit=0):


class Rocket:
    def __init__ (self, file_name, spawn_coords = (500, 400), spawn_velocity = (0, 0), size = (100, 100)):
        self.file_name = file_name
        self.size = size


        self.coords = np.array(spawn_coords).astype(np.double)
        self.velocity = np.array(spawn_velocity).astype(np.double)


        self.image = pygame.transform.scale(pygame.image.load(self.file_name), size)
        self.acceleration = np.zeros(2)  #np.array((0,0))



   # def update(self, dt = 1):

        #self.coords += self.velocity*dt
       # self.velocity += self.acceleration*dt

    def get_coords(self):
        return self.coords


    def get_acceleration(self, planets = [], dt = 1, G = 1):

        self.acceleration = np.zeros(2)

        for the_planet in planets:
            planet_coords = np.array(the_planet.get_coords())

            rocket_coords = np.array(self.get_coords())

            vec_r = rocket_coords - planet_coords

            #R = np.sqrt(vec_r[0]**2 + vec_r[1]**2)
            R = np.sqrt(np.sum(np.square(vec_r)))

            self.acceleration -= G*the_planet.mass/R**3*vec_r



        self.coords += self.velocity*dt
        self.velocity += self.acceleration*dt

    def energy(self, planets = [], G = 1):

        energy = 0

        for the_planet in planets:
            planet_coords = np.array(the_planet.get_coords())

            rocket_coords = np.array(self.get_coords())

            vec_r = rocket_coords - planet_coords

            R = np.sqrt(np.sum(np.square(vec_r)))

            energy -= G*the_planet.mass/R #Calculation of the potential energy



        energy += np.sum(np.square(self.velocity))/2    #Calcilation of the kinetic energy

        return energy

    def draw(self, screen):

        screen.blit(self.image, self.image.get_rect(center = np.array(self.coords)))

