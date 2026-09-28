strawberry=5
rapsberry=10
blueberry=15
def fantome(points):
    return points * 2
points=7*strawberry+4*rapsberry
points=fantome(points)
points+=10*rapsberry+blueberry
for i in range (3):
    points=fantome(points)
print(f"Mon génial score est de {points} points !")
