import taichi as ti

from src.Simulation import Simulation
from src.objects.Box import Box
from src.objects.Sphere import Sphere
from src.clothes.GridCloth import GridCloth

sim = Simulation("test", res=(1600, 900))
sim.set_camera((0.4, -1, 0.3), (0, 0, 0))
sim.add_light((0, 1, 2), (1, 1, 1))

c = GridCloth(N=(10, 10))
sim.add_cloth(c)

b = Box(ti.Vector([0, 0, -0.2]), ti.Vector([0.4, 0.4, 0.4]), color=(0, 0, 0.7))
sim.add_object(b)

#s = Sphere(ti.Vector([0, 0, 0]), 0.3, color=(1, 0, 0))
#sim.add_object(s)

sim.run()