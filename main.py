from world import World
from ant import Ant

swiat=World()
ants = [Ant(swiat) for k in range(50)]

for i in range(10):
    for a in ants:
        a.move()

print("End")
