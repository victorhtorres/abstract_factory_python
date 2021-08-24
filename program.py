import ast
from factory.look import Look
from factory.light_color_cold_and_casual_day import LightColorColdAndCasualDay
from factory.dark_color_warm_semi_formal_day import DarkColorWarmSemiFormalDay

g1: Look = Look(LightColorColdAndCasualDay())
g1.dress()
g2: Look = Look(DarkColorWarmSemiFormalDay())
g2.dress()
print(g1 == g2)
print(g2 > g1)

with open('virtual_wardrobe.txt') as f:
    data = f.read()
wardrobe = ast.literal_eval(data)
print(wardrobe)

wardrobe[g1.factory.get_name] = g1.factory.get_formality
wardrobe[g2.factory.get_name] = g2.factory.get_formality
print(wardrobe)

with open('virtual_wardrobe.txt', 'w') as v_wardrobe:
    v_wardrobe.write(str(wardrobe))
v_wardrobe.close()
