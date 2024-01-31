heads = int(input())
legs = int(input())
def solve(numheads, numlegs):
    y = numlegs - (numheads * 4)
    x = y / (-2)
    return int(x)
chiken = solve(heads, legs)
rabbit = heads - chiken
print("Number of chikens = {}, number of rabbits = {}".format(chiken,rabbit) )
