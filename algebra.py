import numpy as np

m1 = np.random.randint(0, 10, (3, 2))
m2 = np.random.randint(0, 10, (2, 3))

print(f"{m1}\n\n{m2}\n\n")

mp = m1 @ m2 

print(mp)