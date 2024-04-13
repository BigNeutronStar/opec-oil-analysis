import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append('./Work/Library')

from databases import productions, years

fig, axs = plt.subplots(1, len(years))
plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.1)

for i in range(len(years)):
    data = np.array([prd[i] for prd in productions.values()])

plt.show()