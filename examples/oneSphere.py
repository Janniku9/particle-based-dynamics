import taichi as ti

from src.Simulation import Simulation
from src.objects.Sphere import Sphere
from src.clothes.GridCloth import GridCloth

sim = Simulation("one Sphere", res=(1600, 900), dt=0.01, MODE=ti.cpu, iterations=5, gravity=-1)
sim.set_camera((2, 2, 1), (0, 0, 0))
sim.add_light((1, 1, 10), (1, 1, 1))

c = GridCloth(N=(48, 48), center=ti.Vector([0.2, 0, 0.01]), S=(0.5, 0.5), KS=1, KB=0.4, KC=1)
sim.add_cloth(c)

s = Sphere(ti.Vector([0, 0, -0.11]), 0.1, color=(1, 0, 0))
sim.add_object(s)

#sim.make_video("one sphere")
sim.run()