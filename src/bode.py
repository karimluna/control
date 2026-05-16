import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from utils import _set_style

_set_style()
# Sistema: G(s) = 1/((s+1)(s+2))
num = [1]
den = [1, 3, 2]   # s^2 + 3s + 2
G = signal.TransferFunction(num, den)

w = np.logspace(-2, 2, 1000)

w, mag, phase = signal.bode(G, w)

plt.figure(figsize=(4, 4.5))
plt.subplot(2,1,1)
plt.semilogx(w, mag)
plt.grid(True, alpha=0.2)
plt.ylabel('Magnitude (dB)')
plt.title('Bode Diagram G(s)=1/((s+1)(s+2))')

plt.subplot(2,1,2)
plt.semilogx(w, phase)
plt.grid(True, alpha=0.2)
plt.ylabel(r'$\angle$ Phase')
plt.xlabel('Frequency (rad/s)')
plt.savefig('./figures/bode.pdf', dpi=120)
plt.show()