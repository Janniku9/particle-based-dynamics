import taichi as ti
import numpy as np
from src.Simulation import Simulation
from src.objects.Sphere import Sphere
from src.objects.Box import Box
from src.objects.Plane import Plane
from src.clothes.GridCloth import GridCloth

sim = Simulation("test", res=(1600, 900), dt=0.01, MODE=ti.cpu, iterations=5, gravity=-0.9, rotateCamera=0, selfCollision=False)

camera_angle = 1.6
sim.set_camera((-2 * ti.cos(camera_angle), 2 * ti.sin(camera_angle), 0.5), (0, 0, 0))
sim.add_light((2, 0, 10), (0.8, 0.8, 0.8))
sim.add_light((2, 0, 10), (0.8, 0.8, 0.8))

c1 = GridCloth(N=(48, 48), S=(0.5, 0.5), KS=1, KB=0.4, KC=1, center=ti.Vector([0.5, 0, 0.01]), KL=0, KD=0)
sim.add_cloth(c1)

c2 = GridCloth(N=(48, 48), S=(0.5, 0.5), KS=0.7, KB=0.4, KC=1, center=ti.Vector([-0.5, 0, 0.01]), KL=0, KD=0)
sim.add_cloth(c2)

sradius = 0.1
s1 = Sphere(ti.Vector([0.5, 0, -sradius]), sradius, color=(0, 0.8, 0.8), drest=0.01)
sim.add_object(s1)

s2 = Sphere(ti.Vector([-0.5, 0, -sradius]), sradius, color=(0.8, 0, 0.8), drest=0.01)
sim.add_object(s2)


sim.make_video("stretching_sphere")
sim.run()